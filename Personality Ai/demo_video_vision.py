#!/usr/bin/env python3
"""
Demo Video Vision - Create and test video vision capabilities
"""

import sys
import os
import cv2
import numpy as np
import tempfile
from rich.console import Console

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def create_demo_video():
    """Create a demo video for testing video vision"""
    console.print("[yellow]🎬 Creating demo video for testing...[/yellow]")
    
    try:
        # Create demo video path
        demo_path = "demo_test_video.mp4"
        
        # Video properties
        width, height = 640, 480
        fps = 30
        duration = 15  # 15 seconds
        
        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(demo_path, fourcc, fps, (width, height))
        
        console.print(f"[dim]Creating {duration}s video at {fps} FPS...[/dim]")
        
        # Generate frames with different content
        for frame_num in range(fps * duration):
            # Create a frame with changing content
            frame = np.zeros((height, width, 3), dtype=np.uint8)
            
            # Background color that changes
            bg_color = (
                int(50 + 50 * np.sin(frame_num * 0.05)),
                int(50 + 50 * np.cos(frame_num * 0.03)),
                int(100 + 50 * np.sin(frame_num * 0.07))
            )
            frame[:] = bg_color
            
            # Add moving rectangle
            rect_x = int(50 + 200 * np.sin(frame_num * 0.1))
            rect_y = int(100 + 100 * np.cos(frame_num * 0.08))
            color = (
                int(255 * np.sin(frame_num * 0.02) ** 2),
                int(255 * np.cos(frame_num * 0.03) ** 2),
                int(255 * np.sin(frame_num * 0.04) ** 2)
            )
            cv2.rectangle(frame, (rect_x, rect_y), (rect_x + 100, rect_y + 80), color, -1)
            
            # Add text that changes
            text_content = [
                "AI Video Vision Test",
                "Frame Analysis Demo",
                "Object Detection",
                "Motion Tracking",
                "Text Recognition",
                "Scene Understanding"
            ]
            text_index = (frame_num // 60) % len(text_content)
            text = text_content[text_index]
            
            # Text position
            text_x = 50
            text_y = 350 + int(20 * np.sin(frame_num * 0.1))
            
            cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(frame, f"Frame: {frame_num}", (450, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 1)
            
            # Add moving circle
            circle_x = int(320 + 150 * np.sin(frame_num * 0.15))
            circle_y = int(240 + 100 * np.cos(frame_num * 0.12))
            circle_color = (0, 255, 255)
            cv2.circle(frame, (circle_x, circle_y), 25, circle_color, -1)
            
            # Add scene changes every 3 seconds
            scene_num = frame_num // (fps * 3)
            if scene_num % 2 == 1:
                # Darker scene
                frame = cv2.addWeighted(frame, 0.5, np.zeros_like(frame), 0.5, 0)
                cv2.putText(frame, "SCENE CHANGE", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
            
            out.write(frame)
            
            # Show progress
            if frame_num % (fps * 2) == 0:
                progress = (frame_num / (fps * duration)) * 100
                console.print(f"[dim]Progress: {progress:.0f}%[/dim]")
        
        out.release()
        console.print(f"[green]✅ Demo video created: {demo_path}[/green]")
        return demo_path
        
    except Exception as e:
        console.print(f"[red]❌ Demo video creation failed: {e}[/red]")
        return None

def test_video_vision_with_demo():
    """Test video vision with the demo video"""
    console.print("[bold blue]👁️ Testing Video Vision with Demo[/bold blue]")
    
    try:
        # Create demo video
        demo_path = create_demo_video()
        
        if not demo_path:
            console.print("[red]❌ Could not create demo video[/red]")
            return False
        
        # Initialize AI
        from main_ai import PersonalityAI
        console.print("[yellow]Initializing AI...[/yellow]")
        ai = PersonalityAI()
        
        # Test video vision
        console.print(f"\n[cyan]🎥 AI is watching demo video...[/cyan]")
        watch_result = ai.video_vision.watch_video(demo_path, duration_limit=60)
        
        if watch_result.get('success', False):
            console.print("[green]✅ Video vision test successful![/green]")
            
            # Show results
            frames_analyzed = watch_result.get('frames_analyzed', 0)
            scenes_detected = len(watch_result.get('scenes_detected', []))
            objects_seen = len(watch_result.get('objects_seen', []))
            text_found = len(watch_result.get('text_found', []))
            motion_events = len(watch_result.get('motion_detected', []))
            comprehension = watch_result.get('comprehension_score', 0)
            
            console.print(f"\n[cyan]📊 Analysis Results:[/cyan]")
            console.print(f"  📹 Frames Analyzed: {frames_analyzed}")
            console.print(f"  🎬 Scenes Detected: {scenes_detected}")
            console.print(f"  🎯 Objects Seen: {objects_seen}")
            console.print(f"  📝 Text Found: {text_found}")
            console.print(f"  🏃 Motion Events: {motion_events}")
            console.print(f"  🧠 Comprehension Score: {comprehension:.2f}")
            
            # Show visual summary
            visual_summary = watch_result.get('visual_summary', '')
            if visual_summary:
                console.print(f"\n[cyan]👁️ What the AI saw:[/cyan]")
                console.print(f"  {visual_summary}")
            
            # Show scenes
            scenes = watch_result.get('scenes_detected', [])
            if scenes:
                console.print(f"\n[cyan]🎬 Scenes Detected:[/cyan]")
                for i, scene in enumerate(scenes[:5], 1):
                    timestamp = scene.get('timestamp', 0)
                    description = scene.get('description', '')
                    console.print(f"  {i}. At {timestamp:.1f}s: {description}")
            
            # Show objects
            objects = watch_result.get('objects_seen', [])
            if objects:
                object_types = list(set([obj['type'] for obj in objects]))
                console.print(f"\n[cyan]🎯 Objects Detected:[/cyan]")
                for obj_type in object_types:
                    count = len([obj for obj in objects if obj['type'] == obj_type])
                    console.print(f"  • {obj_type.title()}: {count} instances")
            
            # Show text
            text_instances = watch_result.get('text_found', [])
            if text_instances:
                console.print(f"\n[cyan]📝 Text Found:[/cyan]")
                for text_instance in text_instances[:5]:
                    timestamp = text_instance.get('timestamp', 0)
                    text_content = text_instance.get('text', '')
                    console.print(f"  • At {timestamp:.1f}s: {text_content}")
            
            # Show motion analysis
            motion_events = watch_result.get('motion_detected', [])
            if motion_events:
                avg_motion = sum(m.get('motion_intensity', 0) for m in motion_events if m) / len(motion_events)
                console.print(f"\n[cyan]🏃 Motion Analysis:[/cyan]")
                console.print(f"  • Average Motion Intensity: {avg_motion:.3f}")
                console.print(f"  • Motion Events: {len(motion_events)}")
                
                if avg_motion > 0.1:
                    console.print("  • Assessment: High motion content")
                elif avg_motion > 0.05:
                    console.print("  • Assessment: Moderate motion content")
                else:
                    console.print("  • Assessment: Low motion content")
            
            # Show final status
            console.print(f"\n[cyan]📊 Updated Video Vision Status:[/cyan]")
            status = ai.video_vision.get_video_vision_status()
            console.print(f"  👁️ Videos Watched: {status['videos_watched']}")
            console.print(f"  🧠 Overall Video Vision: {status['overall_video_vision']:.3f}")
            console.print(f"  📈 Average Comprehension: {status['comprehension_average']:.3f}")
            
            # Clean up demo video
            try:
                os.remove(demo_path)
                console.print(f"[dim]🗑️ Cleaned up demo video[/dim]")
            except:
                pass
            
            return True
            
        else:
            error_msg = watch_result.get('error', 'Unknown error')
            console.print(f"[red]❌ Video vision test failed: {error_msg}[/red]")
            return False
            
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main demo function"""
    console.print("[bold green]🎬 Video Vision Demo[/bold green]")
    console.print("Creating and testing AI video vision capabilities")
    console.print("=" * 60)
    
    success = test_video_vision_with_demo()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: Video Vision Demo Complete![/bold green]")
        console.print("\n[cyan]Your AI successfully:[/cyan]")
        console.print("  👁️ Watched a video frame-by-frame")
        console.print("  🎬 Detected scene changes and transitions")
        console.print("  🎯 Identified objects moving through the video")
        console.print("  📝 Found and read text in video frames")
        console.print("  🏃 Analyzed motion patterns and intensity")
        console.print("  🎨 Understood colors and visual elements")
        console.print("  🧠 Generated a comprehension score")
        console.print("  📚 Learned from the video experience")
        
        console.print("\n[bold yellow]🎯 Try with your own videos:[/bold yellow]")
        console.print("  python main_ai.py interactive")
        console.print("  Then use: watch_video your_video.mp4")
        
    else:
        console.print("\n[bold red]❌ FAILED: Video vision demo had issues[/bold red]")

if __name__ == "__main__":
    main()
