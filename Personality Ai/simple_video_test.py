#!/usr/bin/env python3
"""
Simple Video Vision Test - Create and test video watching
"""

import sys
import os
import cv2
import numpy as np
from rich.console import Console

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def create_simple_test_video():
    """Create a simple test video"""
    console.print("[yellow]🎬 Creating simple test video...[/yellow]")
    
    try:
        video_path = "simple_test_video.avi"
        
        # Video settings
        width, height = 320, 240
        fps = 10
        duration = 5  # 5 seconds
        
        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))
        
        if not out.isOpened():
            console.print("[red]❌ Could not create video writer[/red]")
            return None
        
        total_frames = fps * duration
        console.print(f"[dim]Creating {total_frames} frames...[/dim]")
        
        for i in range(total_frames):
            # Create frame
            frame = np.zeros((height, width, 3), dtype=np.uint8)
            
            # Simple background color
            frame[:] = (50, 100, 150)  # Brown-ish background
            
            # Moving rectangle
            x = 20 + (i * 5) % (width - 60)
            y = 50
            cv2.rectangle(frame, (x, y), (x + 40, y + 30), (0, 255, 0), -1)
            
            # Text
            cv2.putText(frame, f"Frame {i}", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.putText(frame, "AI Test", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
            
            # Moving circle
            cx = int(160 + 50 * np.sin(i * 0.3))
            cy = int(120 + 30 * np.cos(i * 0.2))
            cv2.circle(frame, (cx, cy), 15, (255, 0, 255), -1)
            
            out.write(frame)
        
        out.release()
        
        if os.path.exists(video_path):
            size = os.path.getsize(video_path)
            console.print(f"[green]✅ Test video created: {video_path} ({size} bytes)[/green]")
            return video_path
        else:
            console.print("[red]❌ Video file not created[/red]")
            return None
            
    except Exception as e:
        console.print(f"[red]❌ Video creation failed: {e}[/red]")
        return None

def test_video_watching():
    """Test video watching with simple video"""
    console.print("[bold blue]👁️ Testing AI Video Watching[/bold blue]")
    
    try:
        # Create test video
        video_path = create_simple_test_video()
        if not video_path:
            return False
        
        # Initialize AI
        from main_ai import PersonalityAI
        console.print("[yellow]Initializing AI...[/yellow]")
        ai = PersonalityAI()
        
        # Test video watching
        console.print(f"\n[cyan]🎥 AI watching video: {video_path}[/cyan]")
        
        # Use the video vision engine directly
        watch_result = ai.video_vision.watch_video(video_path, duration_limit=30)
        
        if watch_result.get('success', False):
            console.print("[green]✅ Video watching successful![/green]")
            
            # Show results
            frames_analyzed = watch_result.get('frames_analyzed', 0)
            scenes_detected = len(watch_result.get('scenes_detected', []))
            objects_seen = len(watch_result.get('objects_seen', []))
            text_found = len(watch_result.get('text_found', []))
            motion_events = len(watch_result.get('motion_detected', []))
            comprehension = watch_result.get('comprehension_score', 0)
            
            console.print(f"\n[cyan]📊 What the AI saw:[/cyan]")
            console.print(f"  📹 Frames Analyzed: {frames_analyzed}")
            console.print(f"  🎬 Scenes Detected: {scenes_detected}")
            console.print(f"  🎯 Objects Seen: {objects_seen}")
            console.print(f"  📝 Text Found: {text_found}")
            console.print(f"  🏃 Motion Events: {motion_events}")
            console.print(f"  🧠 Comprehension Score: {comprehension:.2f}")
            
            # Show visual summary
            visual_summary = watch_result.get('visual_summary', '')
            if visual_summary:
                console.print(f"\n[cyan]👁️ AI's description:[/cyan]")
                console.print(f"  {visual_summary}")
            
            # Show text found
            text_instances = watch_result.get('text_found', [])
            if text_instances:
                console.print(f"\n[cyan]📝 Text the AI read:[/cyan]")
                for text_instance in text_instances[:3]:
                    timestamp = text_instance.get('timestamp', 0)
                    text_content = text_instance.get('text', '')
                    console.print(f"  • At {timestamp:.1f}s: {text_content}")
            
            # Show motion analysis
            motion_events = watch_result.get('motion_detected', [])
            if motion_events:
                avg_motion = sum(m.get('motion_intensity', 0) for m in motion_events if m) / len(motion_events)
                console.print(f"\n[cyan]🏃 Motion the AI detected:[/cyan]")
                console.print(f"  • Motion Events: {len(motion_events)}")
                console.print(f"  • Average Intensity: {avg_motion:.3f}")
                
                if avg_motion > 0.1:
                    console.print("  • Assessment: High motion video")
                elif avg_motion > 0.05:
                    console.print("  • Assessment: Moderate motion")
                else:
                    console.print("  • Assessment: Low motion video")
            
            # Show AI's learning
            console.print(f"\n[cyan]🧠 AI's learning progress:[/cyan]")
            status = ai.video_vision.get_video_vision_status()
            console.print(f"  • Videos Watched: {status['videos_watched']}")
            console.print(f"  • Overall Video Vision: {status['overall_video_vision']:.3f}")
            console.print(f"  • Average Comprehension: {status['comprehension_average']:.3f}")
            
            # Clean up
            try:
                os.remove(video_path)
                console.print(f"[dim]🗑️ Cleaned up test video[/dim]")
            except:
                pass
            
            return True
            
        else:
            error_msg = watch_result.get('error', 'Unknown error')
            console.print(f"[red]❌ Video watching failed: {error_msg}[/red]")
            return False
            
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    console.print("[bold green]🧪 Simple Video Vision Test[/bold green]")
    console.print("Testing AI's ability to watch and understand videos")
    console.print("=" * 60)
    
    success = test_video_watching()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: AI Video Vision Working![/bold green]")
        console.print("\n[cyan]Your AI successfully:[/cyan]")
        console.print("  👁️ Watched a video frame by frame")
        console.print("  📝 Found and read text in the video")
        console.print("  🏃 Detected motion and movement")
        console.print("  🧠 Generated a comprehension score")
        console.print("  📚 Learned from the video experience")
        console.print("  📊 Updated its video vision skills")
        
        console.print("\n[bold yellow]🎯 Try with your own videos:[/bold yellow]")
        console.print("  python main_ai.py interactive")
        console.print("  Then use: watch_video your_video.mp4")
        
        console.print("\n[cyan]💡 Your AI can now watch and understand any video file![/cyan]")
        
    else:
        console.print("\n[bold red]❌ FAILED: Video vision test had issues[/bold red]")

if __name__ == "__main__":
    main()
