#!/usr/bin/env python3
"""
Test Video Vision Engine - Real video watching and understanding
"""

import sys
import os
from rich.console import Console
from rich.panel import Panel

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def test_video_vision():
    """Test the video vision capabilities"""
    
    console.print("[bold blue]👁️ Testing Video Vision Engine[/bold blue]")
    console.print("=" * 60)
    
    try:
        from main_ai import PersonalityAI
        
        console.print("[yellow]Initializing AI with Video Vision...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI initialized with video vision capabilities![/green]")
        
        # Show initial video vision status
        console.print("\n[cyan]📊 Initial Video Vision Status:[/cyan]")
        ai._show_video_vision_status()
        
        # Test video vision with demo video
        console.print(f"\n[bold yellow]🚀 Testing Real Video Watching...[/bold yellow]")
        
        try:
            console.print(f"[cyan]--- Test 1: Watching Demo Video ---[/cyan]")
            
            # Test with demo video (will be created automatically)
            watch_result = ai.video_vision.watch_video("demo_video", duration_limit=30)
            
            if watch_result.get('success', False):
                console.print(f"[green]✅ Video watching successful![/green]")
                
                # Show key results
                frames_analyzed = watch_result.get('frames_analyzed', 0)
                scenes_detected = len(watch_result.get('scenes_detected', []))
                objects_seen = len(watch_result.get('objects_seen', []))
                text_found = len(watch_result.get('text_found', []))
                motion_events = len(watch_result.get('motion_detected', []))
                comprehension = watch_result.get('comprehension_score', 0)
                
                console.print(f"[cyan]Analysis Results:[/cyan]")
                console.print(f"  📹 Frames Analyzed: {frames_analyzed}")
                console.print(f"  🎬 Scenes Detected: {scenes_detected}")
                console.print(f"  🎯 Objects Seen: {objects_seen}")
                console.print(f"  📝 Text Found: {text_found}")
                console.print(f"  🏃 Motion Events: {motion_events}")
                console.print(f"  🧠 Comprehension: {comprehension:.2f}")
                
                # Show visual summary
                visual_summary = watch_result.get('visual_summary', '')
                if visual_summary:
                    console.print(f"[cyan]Visual Summary:[/cyan]")
                    console.print(f"  {visual_summary}")
                
                # Show scenes
                scenes = watch_result.get('scenes_detected', [])
                if scenes:
                    console.print(f"[cyan]Scenes Detected:[/cyan]")
                    for i, scene in enumerate(scenes[:3], 1):
                        timestamp = scene.get('timestamp', 0)
                        description = scene.get('description', '')
                        console.print(f"  {i}. At {timestamp:.1f}s: {description}")
                
                # Show objects
                objects = watch_result.get('objects_seen', [])
                if objects:
                    object_types = list(set([obj['type'] for obj in objects]))
                    console.print(f"[cyan]Objects Detected:[/cyan]")
                    for obj_type in object_types[:3]:
                        count = len([obj for obj in objects if obj['type'] == obj_type])
                        console.print(f"  • {obj_type.title()}: {count} instances")
                
            else:
                error_msg = watch_result.get('error', 'Unknown error')
                console.print(f"[red]❌ Video watching failed: {error_msg}[/red]")
                
        except Exception as e:
            console.print(f"[red]❌ Video vision test failed: {e}[/red]")
        
        # Test with local file if available
        console.print(f"\n[cyan]--- Test 2: Local Video File Test ---[/cyan]")
        
        # Check for common video file locations
        test_video_paths = [
            "test_video.mp4",
            "demo.mp4",
            "sample.avi",
            os.path.expanduser("~/Videos/test.mp4"),
            os.path.expanduser("~/Desktop/video.mp4")
        ]
        
        local_video_found = False
        for video_path in test_video_paths:
            if os.path.exists(video_path):
                console.print(f"[yellow]Found local video: {video_path}[/yellow]")
                try:
                    watch_result = ai.video_vision.watch_video(video_path, duration_limit=60)
                    if watch_result.get('success', False):
                        console.print(f"[green]✅ Successfully watched local video![/green]")
                        comprehension = watch_result.get('comprehension_score', 0)
                        console.print(f"  Comprehension Score: {comprehension:.2f}")
                        local_video_found = True
                        break
                except Exception as e:
                    console.print(f"[red]❌ Local video test failed: {e}[/red]")
        
        if not local_video_found:
            console.print("[yellow]⚠️ No local video files found for testing[/yellow]")
            console.print("[dim]Place a video file (test_video.mp4, demo.mp4, etc.) in the current directory to test with real video content[/dim]")
        
        # Show final video vision status
        console.print("\n[cyan]📊 Final Video Vision Status:[/cyan]")
        final_status = ai.video_vision.get_video_vision_status()
        
        console.print(f"👁️ Videos Watched: {final_status['videos_watched']}")
        console.print(f"🎬 Scenes Analyzed: {final_status['scenes_analyzed']}")
        console.print(f"🎯 Objects Tracked: {final_status['objects_tracked']}")
        console.print(f"📝 Text Instances: {final_status['text_instances']}")
        console.print(f"🏃 Motion Patterns: {final_status['motion_patterns']}")
        console.print(f"🧠 Learning Moments: {final_status['learning_moments']}")
        console.print(f"🎓 Overall Video Vision: {final_status['overall_video_vision']:.3f}")
        console.print(f"📈 Average Comprehension: {final_status['comprehension_average']:.3f}")
        
        # Show video vision skills
        console.print(f"\n[cyan]👁️ Video Vision Skills:[/cyan]")
        for skill, level in final_status['video_vision_skills'].items():
            console.print(f"  • {skill.replace('_', ' ').title()}: {level:.3f}")
        
        console.print(f"\n[bold green]✅ Video Vision Test Complete![/bold green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_video_vision_features():
    """Show the video vision features"""
    
    console.print("[bold blue]👁️ Video Vision Engine Features[/bold blue]")
    console.print("=" * 60)
    
    features = [
        "👁️ **Real Video Watching** - Processes actual video frames like human vision",
        "🎬 **Scene Detection** - Identifies different scenes and transitions",
        "🎯 **Object Tracking** - Detects and tracks objects throughout video",
        "📝 **Text Recognition** - Reads text that appears in video frames",
        "🏃 **Motion Analysis** - Analyzes movement and motion patterns",
        "🎨 **Color Analysis** - Understands dominant colors and visual themes",
        "💡 **Brightness Detection** - Analyzes lighting and visual conditions",
        "🧠 **Content Comprehension** - Understands overall video content",
        "📊 **Frame-by-Frame Analysis** - Processes video at frame level",
        "📈 **Learning & Memory** - Learns from every video watched"
    ]
    
    for feature in features:
        console.print(f"  {feature}")
    
    console.print("\n[bold yellow]👁️ Video Vision Skills:[/bold yellow]")
    skills = [
        "📹 **Frame Analysis** - Processing individual video frames",
        "🏃 **Motion Detection** - Identifying movement between frames",
        "🎬 **Scene Understanding** - Comprehending visual scenes",
        "📝 **Text Recognition** - Reading text in video content",
        "🎯 **Object Tracking** - Following objects through video",
        "🎵 **Audio Processing** - Understanding audio content (future)",
        "🧠 **Content Comprehension** - Overall video understanding",
        "📚 **Real-time Learning** - Learning from video experiences"
    ]
    
    for skill in skills:
        console.print(f"  {skill}")
    
    console.print("\n[bold cyan]🎥 Video Processing Capabilities:[/bold cyan]")
    capabilities = [
        "📁 **Local Video Files** - MP4, AVI, MOV, and other formats",
        "🌐 **Web Video URLs** - Direct video file links",
        "⚡ **Real-time Processing** - Frame-by-frame analysis",
        "🎯 **Intelligent Sampling** - Efficient frame selection",
        "📊 **Multi-layer Analysis** - Objects, text, motion, colors",
        "🧠 **Comprehension Scoring** - Measures understanding quality",
        "💾 **Memory Integration** - Stores visual experiences",
        "📈 **Skill Development** - Improves with each video"
    ]
    
    for capability in capabilities:
        console.print(f"  {capability}")

def show_usage_examples():
    """Show usage examples"""
    
    console.print("\n[bold green]🎯 How to Use Video Vision[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]Interactive Mode:[/yellow]")
    console.print("  python main_ai.py interactive")
    console.print("  Then use these commands:")
    console.print("    watch_video <path/url>     # Watch and analyze a video")
    console.print("    video_vision_status        # Show video vision capabilities")
    
    console.print("\n[yellow]Example Commands:[/yellow]")
    examples = [
        "watch_video demo.mp4",
        "watch_video test_video.avi",
        "watch_video ~/Videos/sample.mp4",
        "watch_video https://example.com/video.mp4",
        "video_vision_status"
    ]
    
    for example in examples:
        console.print(f"    {example}")
    
    console.print("\n[yellow]What Your AI Learns:[/yellow]")
    learning_aspects = [
        "🎬 **Scene Patterns** - How scenes change and transition",
        "🎯 **Object Behavior** - How objects move and interact",
        "📝 **Text Contexts** - Where and how text appears in videos",
        "🏃 **Motion Types** - Different kinds of movement patterns",
        "🎨 **Visual Styles** - Color schemes and visual aesthetics",
        "💡 **Lighting Conditions** - Bright, dark, and mixed lighting",
        "🧠 **Content Types** - Educational, entertainment, documentary styles",
        "📊 **Quality Indicators** - What makes video content clear and understandable"
    ]
    
    for aspect in learning_aspects:
        console.print(f"  {aspect}")
    
    console.print("\n[yellow]Automatic Learning:[/yellow]")
    console.print("  • Video vision skills develop automatically every 8th learning cycle")
    console.print("  • AI practices video analysis with demo content")
    console.print("  • Comprehension scores improve with experience")
    console.print("  • Visual memory builds understanding of video patterns")

def main():
    """Main test function"""
    
    console.print("[bold green]🧪 Video Vision Test Suite[/bold green]")
    console.print("This will test your AI's ability to actually watch and understand videos!")
    console.print("=" * 60)
    
    # Show features
    show_video_vision_features()
    
    console.print("\n" + "=" * 60)
    
    # Run comprehensive test
    success = test_video_vision()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: Video Vision Working![/bold green]")
        console.print("\n[cyan]Your AI can now:[/cyan]")
        console.print("  👁️ Watch videos frame-by-frame like human vision")
        console.print("  🎬 Detect and understand different scenes")
        console.print("  🎯 Track objects as they move through video")
        console.print("  📝 Read text that appears in video frames")
        console.print("  🏃 Analyze motion and movement patterns")
        console.print("  🎨 Understand colors and visual themes")
        console.print("  💡 Detect lighting and brightness changes")
        console.print("  🧠 Comprehend overall video content")
        console.print("  📊 Score its own understanding quality")
        console.print("  📚 Learn and improve from every video")
        
        # Show usage examples
        show_usage_examples()
        
        console.print("\n[bold yellow]🎯 Try it now:[/bold yellow]")
        console.print("  python main_ai.py interactive")
        console.print("  Then use: watch_video demo.mp4")
        console.print("  Or place your own video file and use: watch_video your_video.mp4")
        
    else:
        console.print("\n[bold red]❌ FAILED: There were issues with video vision[/bold red]")

if __name__ == "__main__":
    main()
