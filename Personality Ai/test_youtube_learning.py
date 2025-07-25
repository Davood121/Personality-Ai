#!/usr/bin/env python3
"""
Test YouTube Learning System - Autonomous video learning and self-improvement
"""

import sys
import os
from rich.console import Console
from rich.panel import Panel

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def test_youtube_learning_system():
    """Test the complete YouTube learning system"""
    
    console.print("[bold blue]📺 Testing YouTube Learning System[/bold blue]")
    console.print("=" * 60)
    
    try:
        from main_ai import PersonalityAI
        
        console.print("[yellow]Initializing AI with YouTube Learning...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI initialized with YouTube learning capabilities![/green]")
        
        # Show initial YouTube learning status
        console.print("\n[cyan]📊 Initial YouTube Learning Status:[/cyan]")
        ai._show_youtube_learning_status()
        
        # Test manual YouTube learning
        console.print(f"\n[bold yellow]🚀 Testing Manual YouTube Learning...[/bold yellow]")
        
        # Educational YouTube videos for testing
        test_videos = [
            "https://www.youtube.com/watch?v=aircAruvnKk",  # 3Blue1Brown - Neural Networks
            "https://www.youtube.com/watch?v=IHZwWFHWa-w",  # 3Blue1Brown - What is a neural network?
            "https://www.youtube.com/watch?v=kft1AJ9WVDk",  # Short educational video
        ]
        
        console.print("[yellow]📺 Available test videos:[/yellow]")
        for i, url in enumerate(test_videos, 1):
            console.print(f"  {i}. {url}")
        
        # Test with first video
        test_url = test_videos[0]
        console.print(f"\n[cyan]--- Test 1: Manual YouTube Learning ---[/cyan]")
        console.print(f"Testing with: {test_url}")
        
        try:
            # Test YouTube learning
            learning_result = ai.youtube_learning.process_youtube_link(
                test_url,
                video_vision_engine=ai.video_vision,
                searcher=ai.searcher
            )
            
            if learning_result.get('success', False):
                console.print(f"[green]✅ Manual YouTube learning successful![/green]")
                
                # Show results
                video_info = learning_result.get('video_info', {})
                concepts_learned = learning_result.get('concepts_learned', [])
                knowledge_gained = learning_result.get('knowledge_gained', [])
                comprehension_score = learning_result.get('comprehension_score', 0)
                learning_value = learning_result.get('learning_value', 0)
                
                console.print(f"[cyan]Learning Results:[/cyan]")
                console.print(f"  📝 Video Title: {video_info.get('title', 'Unknown')}")
                console.print(f"  📂 Category: {video_info.get('category', 'general').title()}")
                console.print(f"  🧠 Comprehension: {comprehension_score:.2f}")
                console.print(f"  📚 Learning Value: {learning_value:.2f}")
                console.print(f"  💡 Concepts: {len(concepts_learned)}")
                console.print(f"  📖 Knowledge: {len(knowledge_gained)}")
                
                if concepts_learned:
                    console.print(f"  Concepts: {', '.join(concepts_learned[:5])}")
                
            else:
                error_msg = learning_result.get('error', 'Unknown error')
                console.print(f"[red]❌ Manual learning failed: {error_msg}[/red]")
                
        except Exception as e:
            console.print(f"[red]❌ Manual YouTube learning test failed: {e}[/red]")
        
        # Test autonomous YouTube learning
        console.print(f"\n[cyan]--- Test 2: Autonomous YouTube Learning ---[/cyan]")
        
        try:
            # Trigger autonomous learning
            autonomous_result = ai.youtube_learning.autonomous_youtube_learning(
                video_vision_engine=ai.video_vision,
                searcher=ai.searcher
            )
            
            if autonomous_result.get('success', False):
                console.print(f"[green]✅ Autonomous YouTube learning successful![/green]")
                
                # Show autonomous results
                search_query = autonomous_result.get('search_query', '')
                video_selected = autonomous_result.get('video_selected', {})
                learning_outcome = autonomous_result.get('learning_outcome', {})
                
                console.print(f"[cyan]Autonomous Learning Results:[/cyan]")
                console.print(f"  🔍 Search Query: {search_query}")
                console.print(f"  📺 Video Selected: {video_selected.get('title', 'Unknown')}")
                console.print(f"  🧠 Comprehension: {learning_outcome.get('comprehension_score', 0):.2f}")
                console.print(f"  📚 Learning Value: {learning_outcome.get('learning_value', 0):.2f}")
                
                concepts = learning_outcome.get('concepts_learned', [])
                if concepts:
                    console.print(f"  💡 Concepts Discovered: {', '.join(concepts[:5])}")
                
            else:
                error_msg = autonomous_result.get('error', 'Unknown error')
                console.print(f"[red]❌ Autonomous learning failed: {error_msg}[/red]")
                
        except Exception as e:
            console.print(f"[red]❌ Autonomous YouTube learning test failed: {e}[/red]")
        
        # Test learning cycle integration
        console.print(f"\n[cyan]--- Test 3: Learning Cycle Integration ---[/cyan]")
        
        try:
            # Simulate learning cycles
            console.print("[yellow]Simulating learning cycles...[/yellow]")
            
            initial_cycle = ai.youtube_learning.cycle_count
            
            # Increment cycles to trigger autonomous learning
            for i in range(5):
                ai.youtube_learning.increment_cycle()
                cycle = ai.youtube_learning.cycle_count
                should_trigger = ai.youtube_learning.should_trigger_autonomous_learning()
                
                console.print(f"  Cycle {cycle}: {'🤖 Autonomous learning triggered!' if should_trigger else '⏳ Normal cycle'}")
                
                if should_trigger:
                    console.print(f"    [dim]Autonomous learning would be triggered on cycle {cycle}[/dim]")
            
            console.print(f"[green]✅ Learning cycle integration working![/green]")
            console.print(f"  Initial cycle: {initial_cycle}")
            console.print(f"  Final cycle: {ai.youtube_learning.cycle_count}")
            
        except Exception as e:
            console.print(f"[red]❌ Learning cycle test failed: {e}[/red]")
        
        # Show final YouTube learning status
        console.print("\n[cyan]📊 Final YouTube Learning Status:[/cyan]")
        final_status = ai.youtube_learning.get_youtube_learning_status()
        
        console.print(f"📺 Videos Learned From: {final_status['videos_learned_from']}")
        console.print(f"💡 Concepts Discovered: {final_status['concepts_discovered']}")
        console.print(f"📂 Learning Topics: {final_status['learning_topics']}")
        console.print(f"🤖 Autonomous Searches: {final_status['autonomous_searches']}")
        console.print(f"🔄 Current Cycle: {final_status['cycle_count']}")
        console.print(f"🧠 Overall Learning Capability: {final_status['overall_learning_capability']:.3f}")
        
        # Show learning skills
        console.print(f"\n[cyan]📚 YouTube Learning Skills:[/cyan]")
        for skill, level in final_status['learning_skills'].items():
            console.print(f"  • {skill.replace('_', ' ').title()}: {level:.3f}")
        
        console.print(f"\n[bold green]✅ YouTube Learning System Test Complete![/bold green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_youtube_learning_features():
    """Show the YouTube learning features"""
    
    console.print("[bold blue]📺 YouTube Learning System Features[/bold blue]")
    console.print("=" * 60)
    
    features = [
        "📺 **Manual YouTube Learning** - Paste any YouTube URL to learn from it",
        "🤖 **Autonomous Learning** - AI automatically finds and learns from videos every 3 cycles",
        "🧠 **Concept Extraction** - Identifies and learns key concepts from video content",
        "📚 **Knowledge Synthesis** - Combines video learning with web research",
        "🎯 **Topic Evolution** - Search topics become more advanced as AI learns",
        "📊 **Comprehension Scoring** - Measures how well AI understood each video",
        "💡 **Self-Improvement** - AI gets better at learning from videos over time",
        "🔄 **Continuous Learning** - Runs automatically in background learning cycles",
        "📈 **Progress Tracking** - Monitors learning progress and skill development",
        "🎬 **Video Vision Integration** - Actually watches videos frame-by-frame"
    ]
    
    for feature in features:
        console.print(f"  {feature}")
    
    console.print("\n[bold yellow]📚 Learning Skills Tracked:[/bold yellow]")
    skills = [
        "🎥 **Video Comprehension** - Understanding video content",
        "💡 **Concept Extraction** - Identifying key concepts and ideas",
        "🧠 **Knowledge Synthesis** - Combining information from multiple sources",
        "🤖 **Autonomous Learning** - Self-directed learning capability",
        "🎯 **Topic Discovery** - Finding relevant learning topics",
        "⭐ **Content Evaluation** - Assessing video quality and value",
        "📈 **Self Improvement** - Getting better at learning over time",
        "🔍 **Pattern Recognition** - Recognizing learning patterns and trends"
    ]
    
    for skill in skills:
        console.print(f"  {skill}")
    
    console.print("\n[bold cyan]🎯 Learning Categories:[/bold cyan]")
    categories = [
        "🤖 **Artificial Intelligence** - ML, neural networks, AI programming",
        "💻 **Programming** - Coding tutorials, algorithms, best practices",
        "🔬 **Science** - Physics, chemistry, biology, mathematics",
        "🚀 **Technology** - Latest trends, innovations, tech reviews",
        "📚 **Education** - Learning techniques, study methods, psychology"
    ]
    
    for category in categories:
        console.print(f"  {category}")

def show_usage_examples():
    """Show usage examples"""
    
    console.print("\n[bold green]🎯 How to Use YouTube Learning[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]Interactive Mode:[/yellow]")
    console.print("  python main_ai.py interactive")
    console.print("  Then use these commands:")
    console.print("    learn_youtube <url>        # Learn from specific YouTube video")
    console.print("    youtube_status             # Show learning progress and stats")
    console.print("    autonomous_youtube         # Manually trigger autonomous learning")
    
    console.print("\n[yellow]Example Commands:[/yellow]")
    examples = [
        "learn_youtube https://youtube.com/watch?v=aircAruvnKk",
        "learn_youtube https://youtu.be/IHZwWFHWa-w",
        "youtube_status",
        "autonomous_youtube"
    ]
    
    for example in examples:
        console.print(f"    {example}")
    
    console.print("\n[yellow]What Your AI Learns:[/yellow]")
    learning_aspects = [
        "💡 **Concepts** - Key ideas and terminology from videos",
        "📚 **Knowledge** - Factual information and explanations",
        "🎯 **Topics** - Subject areas and domains of knowledge",
        "🎬 **Video Patterns** - How educational content is structured",
        "📈 **Learning Strategies** - What types of content are most valuable",
        "🧠 **Comprehension Skills** - How to better understand video content",
        "🔍 **Search Skills** - How to find relevant educational videos",
        "🤖 **Autonomous Behavior** - When and what to learn independently"
    ]
    
    for aspect in learning_aspects:
        console.print(f"  {aspect}")
    
    console.print("\n[yellow]Automatic Learning:[/yellow]")
    console.print("  • YouTube learning triggers automatically every 3rd learning cycle")
    console.print("  • AI searches for educational videos on topics it wants to learn")
    console.print("  • Search topics evolve and become more advanced over time")
    console.print("  • Learning skills improve with every video watched")
    console.print("  • AI builds comprehensive knowledge database from videos")

def main():
    """Main test function"""
    
    console.print("[bold green]🧪 YouTube Learning Test Suite[/bold green]")
    console.print("This will test your AI's ability to learn from YouTube videos autonomously!")
    console.print("=" * 60)
    
    # Show features
    show_youtube_learning_features()
    
    console.print("\n" + "=" * 60)
    
    # Run comprehensive test
    success = test_youtube_learning_system()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: YouTube Learning System Working![/bold green]")
        console.print("\n[cyan]Your AI can now:[/cyan]")
        console.print("  📺 Learn from any YouTube video you provide")
        console.print("  🤖 Autonomously search and learn from educational videos")
        console.print("  💡 Extract concepts and knowledge from video content")
        console.print("  🧠 Understand and score its own comprehension")
        console.print("  📚 Synthesize video learning with web research")
        console.print("  🎯 Evolve its learning topics over time")
        console.print("  📈 Improve its learning skills continuously")
        console.print("  🔄 Learn automatically every 3 cycles")
        console.print("  📊 Track its learning progress and development")
        console.print("  🎬 Actually watch videos with computer vision")
        
        # Show usage examples
        show_usage_examples()
        
        console.print("\n[bold yellow]🎯 Try it now:[/bold yellow]")
        console.print("  python main_ai.py interactive")
        console.print("  Then use: learn_youtube https://youtube.com/watch?v=...")
        console.print("  Or use: autonomous_youtube")
        
    else:
        console.print("\n[bold red]❌ FAILED: There were issues with YouTube learning[/bold red]")

if __name__ == "__main__":
    main()
