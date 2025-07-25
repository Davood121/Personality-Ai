#!/usr/bin/env python3
"""
Real Video Test - Test AI video vision with actual video files
"""

import sys
import os
import glob
from rich.console import Console
from rich.panel import Panel

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def find_video_files():
    """Find real video files on the system"""
    console.print("[yellow]🔍 Searching for video files...[/yellow]")
    
    video_files = []
    
    # Search patterns for video files
    search_patterns = [
        "*.mp4", "*.avi", "*.mov", "*.mkv", "*.wmv", "*.flv", "*.webm",
        "**/*.mp4", "**/*.avi", "**/*.mov", "**/*.mkv", "**/*.wmv"
    ]
    
    # Search in common directories
    search_dirs = [
        ".",  # Current directory
        os.path.expanduser("~/Videos"),
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Downloads"),
        "C:/Users/Public/Videos" if os.name == 'nt' else "/home/*/Videos"
    ]
    
    for search_dir in search_dirs:
        if os.path.exists(search_dir):
            console.print(f"[dim]Searching in: {search_dir}[/dim]")
            
            for pattern in search_patterns:
                try:
                    files = glob.glob(os.path.join(search_dir, pattern), recursive=True)
                    for file_path in files:
                        if os.path.isfile(file_path) and os.path.getsize(file_path) > 1024:  # At least 1KB
                            video_files.append(file_path)
                            console.print(f"[dim green]Found: {os.path.basename(file_path)}[/dim green]")
                except:
                    continue
    
    # Remove duplicates
    video_files = list(set(video_files))
    
    console.print(f"[green]✅ Found {len(video_files)} video files[/green]")
    return video_files

def test_real_video_vision():
    """Test video vision with real video files"""
    console.print("[bold blue]👁️ Testing Real Video Vision[/bold blue]")
    console.print("=" * 60)
    
    try:
        # Find video files
        video_files = find_video_files()
        
        if not video_files:
            console.print("[red]❌ No video files found![/red]")
            console.print("\n[yellow]💡 To test video vision:[/yellow]")
            console.print("  1. Place a video file (MP4, AVI, MOV, etc.) in the current directory")
            console.print("  2. Or use a YouTube URL with: watch_video https://youtube.com/watch?v=...")
            console.print("  3. Or use a direct video URL: watch_video https://example.com/video.mp4")
            return False
        
        # Initialize AI
        from main_ai import PersonalityAI
        console.print("[yellow]Initializing AI with Real Video Vision...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI initialized![/green]")
        
        # Show initial status
        console.print("\n[cyan]📊 Initial Video Vision Status:[/cyan]")
        ai._show_video_vision_status()
        
        # Test with first video file
        test_video = video_files[0]
        console.print(f"\n[bold yellow]🚀 Testing with real video: {os.path.basename(test_video)}[/bold yellow]")
        console.print(f"[dim]File path: {test_video}[/dim]")
        console.print(f"[dim]File size: {os.path.getsize(test_video)} bytes[/dim]")
        
        # Watch the video
        watch_result = ai.video_vision.watch_video(test_video, duration_limit=60)
        
        if watch_result.get('success', False):
            console.print("[green]✅ Real video analysis successful![/green]")
            
            # Show comprehensive results
            frames_analyzed = watch_result.get('frames_analyzed', 0)
            video_duration = watch_result.get('video_duration', 0)
            scenes_detected = len(watch_result.get('scenes_detected', []))
            objects_seen = len(watch_result.get('objects_seen', []))
            text_found = len(watch_result.get('text_found', []))
            motion_events = len(watch_result.get('motion_detected', []))
            comprehension = watch_result.get('comprehension_score', 0)
            
            console.print(f"\n[cyan]📊 Real Video Analysis Results:[/cyan]")
            console.print(f"  🎬 Video Duration: {video_duration:.1f} seconds")
            console.print(f"  📹 Frames Analyzed: {frames_analyzed}")
            console.print(f"  🎭 Scenes Detected: {scenes_detected}")
            console.print(f"  🎯 Objects Seen: {objects_seen}")
            console.print(f"  📝 Text Found: {text_found}")
            console.print(f"  🏃 Motion Events: {motion_events}")
            console.print(f"  🧠 Comprehension Score: {comprehension:.2f}")
            
            # Show what the AI actually saw
            visual_summary = watch_result.get('visual_summary', '')
            if visual_summary:
                console.print(f"\n[cyan]👁️ What the AI saw in the real video:[/cyan]")
                console.print(f"  {visual_summary}")
            
            # Show detected scenes
            scenes = watch_result.get('scenes_detected', [])
            if scenes:
                console.print(f"\n[cyan]🎬 Real Scenes Detected:[/cyan]")
                for i, scene in enumerate(scenes[:5], 1):
                    timestamp = scene.get('timestamp', 0)
                    description = scene.get('description', '')
                    console.print(f"  {i}. At {timestamp:.1f}s: {description}")
            
            # Show detected objects
            objects = watch_result.get('objects_seen', [])
            if objects:
                object_types = list(set([obj['type'] for obj in objects]))
                console.print(f"\n[cyan]🎯 Real Objects Detected:[/cyan]")
                for obj_type in object_types:
                    count = len([obj for obj in objects if obj['type'] == obj_type])
                    console.print(f"  • {obj_type.title()}: {count} instances")
            
            # Show text found
            text_instances = watch_result.get('text_found', [])
            if text_instances:
                console.print(f"\n[cyan]📝 Real Text Found in Video:[/cyan]")
                for text_instance in text_instances[:5]:
                    timestamp = text_instance.get('timestamp', 0)
                    text_content = text_instance.get('text', '')
                    console.print(f"  • At {timestamp:.1f}s: {text_content}")
            
            # Show motion analysis
            motion_events = watch_result.get('motion_detected', [])
            if motion_events:
                avg_motion = sum(m.get('motion_intensity', 0) for m in motion_events if m) / len(motion_events)
                console.print(f"\n[cyan]🏃 Real Motion Analysis:[/cyan]")
                console.print(f"  • Motion Events: {len(motion_events)}")
                console.print(f"  • Average Intensity: {avg_motion:.3f}")
                
                if avg_motion > 0.1:
                    console.print("  • Assessment: High motion video (action, movement)")
                elif avg_motion > 0.05:
                    console.print("  • Assessment: Moderate motion (some activity)")
                else:
                    console.print("  • Assessment: Low motion (static, talking)")
            
            # Show updated AI status
            console.print(f"\n[cyan]📊 Updated AI Video Vision Status:[/cyan]")
            final_status = ai.video_vision.get_video_vision_status()
            console.print(f"  👁️ Videos Watched: {final_status['videos_watched']}")
            console.print(f"  🧠 Overall Video Vision: {final_status['overall_video_vision']:.3f}")
            console.print(f"  📈 Average Comprehension: {final_status['comprehension_average']:.3f}")
            
            # Show skill improvements
            console.print(f"\n[cyan]📈 Video Vision Skills:[/cyan]")
            for skill, level in final_status['video_vision_skills'].items():
                console.print(f"  • {skill.replace('_', ' ').title()}: {level:.3f}")
            
            return True
            
        else:
            error_msg = watch_result.get('error', 'Unknown error')
            console.print(f"[red]❌ Real video analysis failed: {error_msg}[/red]")
            return False
            
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_usage_instructions():
    """Show how to use real video vision"""
    console.print("\n[bold green]🎯 How to Use Real Video Vision[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]1. Local Video Files:[/yellow]")
    console.print("   Place video files in current directory or common folders:")
    console.print("   • Current directory: video.mp4")
    console.print("   • Videos folder: ~/Videos/movie.avi")
    console.print("   • Desktop: ~/Desktop/clip.mov")
    console.print("   • Downloads: ~/Downloads/video.mkv")
    
    console.print("\n[yellow]2. Interactive Mode:[/yellow]")
    console.print("   python main_ai.py interactive")
    console.print("   Then use:")
    console.print("   • watch_video video.mp4")
    console.print("   • watch_video ~/Videos/movie.avi")
    console.print("   • watch_video https://youtube.com/watch?v=...")
    console.print("   • watch_video https://example.com/video.mp4")
    console.print("   • video_vision_status")
    
    console.print("\n[yellow]3. Supported Formats:[/yellow]")
    console.print("   • MP4 (recommended)")
    console.print("   • AVI")
    console.print("   • MOV")
    console.print("   • MKV")
    console.print("   • WMV")
    console.print("   • WEBM")
    console.print("   • FLV")
    
    console.print("\n[yellow]4. Web Videos:[/yellow]")
    console.print("   • YouTube URLs (requires yt-dlp: pip install yt-dlp)")
    console.print("   • Direct video file URLs")
    console.print("   • Streaming video URLs")

def main():
    """Main test function"""
    console.print("[bold green]🧪 Real Video Vision Test[/bold green]")
    console.print("Testing AI's ability to watch and understand REAL videos")
    console.print("=" * 60)
    
    success = test_real_video_vision()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: Real Video Vision Working![/bold green]")
        console.print("\n[cyan]Your AI successfully:[/cyan]")
        console.print("  👁️ Watched a REAL video file frame by frame")
        console.print("  🎬 Analyzed actual video content and scenes")
        console.print("  🎯 Detected real objects in the video")
        console.print("  📝 Found and read actual text in video frames")
        console.print("  🏃 Analyzed real motion and movement patterns")
        console.print("  🧠 Generated comprehension score for real content")
        console.print("  📚 Learned from actual video experience")
        console.print("  📊 Updated video vision skills with real data")
        
        show_usage_instructions()
        
    else:
        console.print("\n[bold red]❌ FAILED: Real video vision test had issues[/bold red]")
        show_usage_instructions()

if __name__ == "__main__":
    main()
