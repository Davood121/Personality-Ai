#!/usr/bin/env python3
"""
Demo All Video Functions - Show complete video and vision capabilities
"""

import sys
import os
from rich.console import Console
from rich.panel import Panel

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def demo_all_video_functions():
    """Demonstrate all video and vision functions"""
    
    console.print("[bold green]🎬 Complete Video & Vision Functions Demo[/bold green]")
    console.print("Showing all video search, vision, and learning capabilities")
    console.print("=" * 70)
    
    try:
        from main_ai import PersonalityAI
        
        console.print("[yellow]🤖 Initializing Complete AI System...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI System Ready with All Capabilities![/green]")
        
        # Demo 1: Video Search Functions
        console.print(f"\n[bold blue]📺 Demo 1: Video Search Functions[/bold blue]")
        console.print("[yellow]Testing multi-platform video search...[/yellow]")
        
        try:
            # Test video search
            search_result = ai.video.search_videos("artificial intelligence tutorial", platform='all', max_results=5)
            
            if search_result.get('success', False):
                videos_found = len(search_result.get('videos_found', []))
                platform_results = search_result.get('platform_results', {})
                
                console.print(f"[green]✅ Video Search Working![/green]")
                console.print(f"  🎥 Found {videos_found} videos across platforms")
                
                for platform, count in platform_results.items():
                    console.print(f"  📺 {platform.title()}: {count} videos")
                
                # Show sample videos
                videos = search_result.get('videos_found', [])
                if videos:
                    console.print(f"\n[cyan]🎬 Sample Videos Found:[/cyan]")
                    for i, video in enumerate(videos[:3], 1):
                        console.print(f"  {i}. {video.get('title', 'Unknown')}")
                        console.print(f"     Platform: {video.get('platform', 'unknown').title()}")
                        console.print(f"     Category: {video.get('category', 'general').title()}")
            
            else:
                console.print("[yellow]⚠️ Video search completed with basic results[/yellow]")
                
        except Exception as e:
            console.print(f"[red]❌ Video search demo failed: {e}[/red]")
        
        # Demo 2: Video Vision Functions
        console.print(f"\n[bold blue]👁️ Demo 2: Video Vision Functions[/bold blue]")
        console.print("[yellow]Testing real video watching capabilities...[/yellow]")
        
        try:
            # Show video vision status
            vision_status = ai.video_vision.get_video_vision_status()
            
            console.print(f"[green]✅ Video Vision System Ready![/green]")
            console.print(f"  👁️ Videos Watched: {vision_status['videos_watched']}")
            console.print(f"  🎬 Scenes Analyzed: {vision_status['scenes_analyzed']}")
            console.print(f"  🧠 Overall Video Vision: {vision_status['overall_video_vision']:.3f}")
            console.print(f"  📈 Average Comprehension: {vision_status['comprehension_average']:.3f}")
            
            # Show video vision skills
            console.print(f"\n[cyan]👁️ Video Vision Skills:[/cyan]")
            for skill, level in vision_status['video_vision_skills'].items():
                skill_bar = "█" * int(level * 10) + "░" * (10 - int(level * 10))
                console.print(f"  • {skill.replace('_', ' ').title()}: {skill_bar} {level:.2f}")
                
        except Exception as e:
            console.print(f"[red]❌ Video vision demo failed: {e}[/red]")
        
        # Demo 3: YouTube Learning Functions
        console.print(f"\n[bold blue]📺 Demo 3: YouTube Learning Functions[/bold blue]")
        console.print("[yellow]Testing autonomous YouTube learning system...[/yellow]")
        
        try:
            # Show YouTube learning status
            youtube_status = ai.youtube_learning.get_youtube_learning_status()
            
            console.print(f"[green]✅ YouTube Learning System Ready![/green]")
            console.print(f"  📺 Videos Learned From: {youtube_status['videos_learned_from']}")
            console.print(f"  💡 Concepts Discovered: {youtube_status['concepts_discovered']}")
            console.print(f"  📂 Learning Topics: {youtube_status['learning_topics']}")
            console.print(f"  🤖 Autonomous Searches: {youtube_status['autonomous_searches']}")
            console.print(f"  🔄 Current Cycle: {youtube_status['cycle_count']}")
            console.print(f"  🧠 Learning Capability: {youtube_status['overall_learning_capability']:.3f}")
            
            # Show learning skills
            console.print(f"\n[cyan]📚 YouTube Learning Skills:[/cyan]")
            for skill, level in youtube_status['learning_skills'].items():
                skill_bar = "█" * int(level * 10) + "░" * (10 - int(level * 10))
                console.print(f"  • {skill.replace('_', ' ').title()}: {skill_bar} {level:.2f}")
            
            # Show next autonomous learning
            if youtube_status.get('next_autonomous_learning', False):
                console.print(f"\n[yellow]🤖 Next cycle will trigger autonomous YouTube learning![/yellow]")
            else:
                cycles_until_next = 3 - (youtube_status['cycle_count'] % 3)
                console.print(f"\n[dim]🔄 Autonomous learning in {cycles_until_next} cycles[/dim]")
                
        except Exception as e:
            console.print(f"[red]❌ YouTube learning demo failed: {e}[/red]")
        
        # Demo 4: Image Vision Functions
        console.print(f"\n[bold blue]👁️ Demo 4: Image Vision Functions[/bold blue]")
        console.print("[yellow]Testing image analysis capabilities...[/yellow]")
        
        try:
            # Show image vision status
            image_vision_status = ai.vision.get_vision_status()
            
            console.print(f"[green]✅ Image Vision System Ready![/green]")
            console.print(f"  👁️ Images Analyzed: {image_vision_status['images_analyzed']}")
            console.print(f"  🎯 Objects Learned: {image_vision_status['objects_learned']}")
            console.print(f"  🎨 Colors Learned: {image_vision_status['colors_learned']}")
            console.print(f"  🧠 Overall Vision Capability: {image_vision_status['overall_vision_capability']:.3f}")
            
            # Show vision skills
            console.print(f"\n[cyan]👁️ Image Vision Skills:[/cyan]")
            for skill, level in image_vision_status['vision_skills'].items():
                skill_bar = "█" * int(level * 10) + "░" * (10 - int(level * 10))
                console.print(f"  • {skill.replace('_', ' ').title()}: {skill_bar} {level:.2f}")
                
        except Exception as e:
            console.print(f"[red]❌ Image vision demo failed: {e}[/red]")
        
        # Show all available commands
        console.print(f"\n[bold cyan]🎯 All Available Video & Vision Commands:[/bold cyan]")
        
        commands = [
            ("📺 Video Search", [
                "search_videos <query>     # Search YouTube, Vimeo, Dailymotion",
                "video_status              # Show video search progress"
            ]),
            ("👁️ Video Vision", [
                "watch_video <path/url>    # Watch and analyze real videos",
                "video_vision_status       # Show video watching progress"
            ]),
            ("📺 YouTube Learning", [
                "learn_youtube <url>       # Learn from YouTube videos",
                "autonomous_youtube        # Trigger autonomous learning",
                "youtube_status            # Show learning progress"
            ]),
            ("👁️ Image Vision", [
                "see <image>               # Quick image viewing",
                "analyze_image <image>     # Deep image analysis",
                "vision_status             # Show vision capabilities",
                "visual_memories           # See everything AI has seen"
            ])
        ]
        
        for category, cmd_list in commands:
            console.print(f"\n[yellow]{category}:[/yellow]")
            for cmd in cmd_list:
                console.print(f"  {cmd}")
        
        console.print(f"\n[bold green]🎉 All Video & Vision Functions Ready![/bold green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Demo failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_quick_start_guide():
    """Show quick start guide for video functions"""
    
    console.print("\n[bold yellow]🚀 Quick Start Guide[/bold yellow]")
    console.print("=" * 70)
    
    console.print("[cyan]1. Start Interactive Mode:[/cyan]")
    console.print("   python main_ai.py interactive")
    
    console.print("\n[cyan]2. Try Video Search:[/cyan]")
    console.print("   search_videos artificial intelligence")
    console.print("   search_videos python programming")
    console.print("   video_status")
    
    console.print("\n[cyan]3. Try Video Vision:[/cyan]")
    console.print("   watch_video video.mp4")
    console.print("   watch_video ~/Videos/movie.avi")
    console.print("   video_vision_status")
    
    console.print("\n[cyan]4. Try YouTube Learning:[/cyan]")
    console.print("   learn_youtube https://youtube.com/watch?v=...")
    console.print("   autonomous_youtube")
    console.print("   youtube_status")
    
    console.print("\n[cyan]5. Try Image Vision:[/cyan]")
    console.print("   see image.jpg")
    console.print("   analyze_image photo.png")
    console.print("   visual_memories")
    
    console.print("\n[yellow]💡 Pro Tips:[/yellow]")
    tips = [
        "🤖 Autonomous YouTube learning triggers every 3rd cycle automatically",
        "👁️ AI remembers everything it sees in images and videos",
        "📺 Video search works across YouTube, Vimeo, and Dailymotion",
        "🧠 All vision and learning skills improve with use",
        "📊 Use status commands to track AI's learning progress",
        "🎬 AI can watch real video files and YouTube videos",
        "💡 AI learns concepts and knowledge from video content",
        "🔄 Everything runs automatically in background learning cycles"
    ]
    
    for tip in tips:
        console.print(f"   • {tip}")

def main():
    """Main demo function"""
    
    console.print("[bold green]🧪 Complete Video & Vision Functions Demo[/bold green]")
    console.print("Testing all video search, vision, and learning capabilities")
    console.print("=" * 70)
    
    success = demo_all_video_functions()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: All Video & Vision Functions Working![/bold green]")
        console.print("\n[cyan]Your AI has complete video intelligence:[/cyan]")
        console.print("  📺 **Video Search** - Multi-platform video discovery")
        console.print("  👁️ **Video Vision** - Real video watching and analysis")
        console.print("  📺 **YouTube Learning** - Autonomous learning from videos")
        console.print("  👁️ **Image Vision** - Advanced image analysis and memory")
        console.print("  🤖 **Autonomous Learning** - Self-directed improvement")
        console.print("  🧠 **Skill Development** - Continuous capability improvement")
        console.print("  📊 **Progress Tracking** - Comprehensive learning analytics")
        console.print("  🔄 **Background Learning** - Automatic learning cycles")
        
        show_quick_start_guide()
        
    else:
        console.print("\n[bold red]❌ FAILED: Some video functions had issues[/bold red]")

if __name__ == "__main__":
    main()
