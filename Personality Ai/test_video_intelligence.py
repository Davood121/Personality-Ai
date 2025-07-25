#!/usr/bin/env python3
"""
Test Video Intelligence Engine - YouTube search and video analysis
"""

import sys
import os
from rich.console import Console
from rich.panel import Panel

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def test_video_intelligence():
    """Test the video intelligence capabilities"""
    
    console.print("[bold blue]🎥 Testing Video Intelligence Engine[/bold blue]")
    console.print("=" * 60)
    
    try:
        from main_ai import PersonalityAI
        
        console.print("[yellow]Initializing AI with Video Intelligence...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI initialized with video capabilities![/green]")
        
        # Show initial video status
        console.print("\n[cyan]📊 Initial Video Status:[/cyan]")
        ai._show_video_status()
        
        # Test video search
        console.print(f"\n[bold yellow]🚀 Testing Video Search...[/bold yellow]")
        
        test_queries = [
            "artificial intelligence tutorial",
            "machine learning explained",
            "python programming",
            "how AI works",
            "technology trends"
        ]
        
        for i, query in enumerate(test_queries, 1):
            console.print(f"\n[cyan]--- Test {i}: Searching '{query}' ---[/cyan]")
            
            try:
                # Test video search
                search_result = ai.video.search_videos(query, platform='all', max_results=5)
                
                if search_result.get('success', False):
                    videos = search_result.get('videos_found', [])
                    console.print(f"[green]✅ Found {len(videos)} videos[/green]")
                    
                    # Show sample results
                    for j, video in enumerate(videos[:2], 1):  # Show first 2
                        console.print(f"  {j}. {video.get('title', 'Unknown')}")
                        console.print(f"     Platform: {video.get('platform', 'unknown').title()}")
                        console.print(f"     Category: {video.get('category', 'general').title()}")
                    
                    # Show insights
                    insights = search_result.get('search_insights', [])
                    if insights:
                        console.print(f"  Insights: {insights[0]}")
                
                else:
                    console.print(f"[red]❌ Search failed: {search_result.get('error', 'Unknown error')}[/red]")
                    
            except Exception as e:
                console.print(f"[red]❌ Search test {i} failed: {e}[/red]")
        
        # Test video watching/analysis
        console.print(f"\n[bold yellow]🚀 Testing Video Analysis...[/bold yellow]")
        
        test_video = {
            'title': 'Introduction to Artificial Intelligence - Complete Tutorial',
            'channel': 'AI Academy',
            'platform': 'youtube',
            'duration': '25:30',
            'category': 'educational',
            'url': 'https://youtube.com/watch?v=test123'
        }
        
        try:
            console.print(f"[cyan]--- Analyzing Test Video ---[/cyan]")
            console.print(f"Title: {test_video['title']}")
            
            # Test video content analysis
            analysis_result = ai.video.analyze_video_content(test_video, searcher=ai.searcher)
            
            if analysis_result.get('success', False):
                console.print(f"[green]✅ Video analysis complete![/green]")
                
                # Show analysis results
                educational_value = analysis_result.get('educational_value', 0)
                console.print(f"Educational Value: {educational_value:.2f}")
                
                learning_insights = analysis_result.get('learning_insights', [])
                console.print(f"Learning Insights: {len(learning_insights)}")
                for insight in learning_insights[:2]:
                    console.print(f"  • {insight}")
                
                related_topics = analysis_result.get('related_topics', [])
                if related_topics:
                    console.print(f"Related Topics: {', '.join(related_topics[:3])}")
                
                web_research = analysis_result.get('web_research', {})
                if web_research:
                    console.print(f"Web Research: {web_research.get('definitions_found', 0)} definitions found")
            
            else:
                console.print(f"[red]❌ Analysis failed: {analysis_result.get('error', 'Unknown error')}[/red]")
                
        except Exception as e:
            console.print(f"[red]❌ Video analysis failed: {e}[/red]")
        
        # Show final video status
        console.print("\n[cyan]📊 Final Video Status:[/cyan]")
        final_status = ai.video.get_video_status()
        
        console.print(f"🎥 Videos Watched: {final_status['videos_watched']}")
        console.print(f"📂 Topics Explored: {final_status['topics_explored']}")
        console.print(f"📺 Channels Discovered: {final_status['channels_discovered']}")
        console.print(f"🔍 Searches Performed: {final_status['searches_performed']}")
        console.print(f"🧠 Overall Video Intelligence: {final_status['overall_video_intelligence']:.3f}")
        
        # Show video skills
        console.print(f"\n[cyan]🎥 Video Skills:[/cyan]")
        for skill, level in final_status['video_skills'].items():
            console.print(f"  • {skill.replace('_', ' ').title()}: {level:.3f}")
        
        console.print(f"\n[bold green]✅ Video Intelligence Test Complete![/bold green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_video_features():
    """Show the video intelligence features"""
    
    console.print("[bold blue]🎥 Video Intelligence Engine Features[/bold blue]")
    console.print("=" * 60)
    
    features = [
        "🎥 **Multi-Platform Video Search** - YouTube, Vimeo, Dailymotion",
        "🔍 **Intelligent Video Discovery** - Finds relevant videos across platforms",
        "📊 **Content Analysis** - Analyzes video metadata and characteristics",
        "🧠 **Learning Extraction** - Learns from video content and topics",
        "📚 **Educational Assessment** - Measures educational value of videos",
        "🌐 **Web Research Integration** - Researches video topics online",
        "📂 **Category Classification** - Automatically categorizes videos",
        "📺 **Channel Discovery** - Learns about content creators",
        "🎯 **Topic Exploration** - Tracks explored subjects and interests",
        "📈 **Skill Development** - 8 different video intelligence skills"
    ]
    
    for feature in features:
        console.print(f"  {feature}")
    
    console.print("\n[bold yellow]🎥 Video Skills Tracked:[/bold yellow]")
    skills = [
        "🔍 **Video Search** - Finding relevant videos across platforms",
        "📊 **Content Analysis** - Understanding video characteristics",
        "📚 **Topic Understanding** - Comprehending video subjects",
        "🧠 **Learning Extraction** - Extracting knowledge from videos",
        "📈 **Trend Analysis** - Understanding video trends and patterns",
        "⭐ **Quality Assessment** - Evaluating video quality and value",
        "🎯 **Recommendation** - Suggesting relevant content",
        "🔗 **Knowledge Synthesis** - Connecting video content with other knowledge"
    ]
    
    for skill in skills:
        console.print(f"  {skill}")
    
    console.print("\n[bold cyan]🌐 Supported Platforms:[/bold cyan]")
    platforms = [
        "📺 **YouTube** - World's largest video platform",
        "🎬 **Vimeo** - High-quality video platform",
        "🌍 **Dailymotion** - European video platform",
        "🔍 **Multi-Platform Search** - Search all platforms simultaneously"
    ]
    
    for platform in platforms:
        console.print(f"  {platform}")
    
    console.print("\n[bold green]📂 Video Categories:[/bold green]")
    categories = [
        "📚 **Educational** - Tutorials, courses, lessons, explanations",
        "💻 **Technology** - Programming, AI, tech reviews, coding",
        "🔬 **Science** - Physics, chemistry, biology, research",
        "🎨 **Creative** - Art, music, design, creative processes",
        "📖 **Documentary** - History, nature, culture, investigations",
        "🎪 **Entertainment** - Comedy, gaming, movies, fun content"
    ]
    
    for category in categories:
        console.print(f"  {category}")

def show_usage_examples():
    """Show usage examples"""
    
    console.print("\n[bold green]🎯 How to Use Video Intelligence[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]Interactive Mode:[/yellow]")
    console.print("  python main_ai.py interactive")
    console.print("  Then use these commands:")
    console.print("    search_videos <query>      # Search videos across platforms")
    console.print("    watch <query>              # Find and analyze a specific video")
    console.print("    video_status               # Show video intelligence status")
    
    console.print("\n[yellow]Example Commands:[/yellow]")
    examples = [
        "search_videos artificial intelligence",
        "search_videos python tutorial",
        "watch machine learning explained",
        "search_videos how AI works",
        "video_status"
    ]
    
    for example in examples:
        console.print(f"    {example}")
    
    console.print("\n[yellow]What Your AI Learns:[/yellow]")
    learning_aspects = [
        "📂 **Topics** - What subjects are being explored",
        "📺 **Channels** - Which content creators produce quality content",
        "🎯 **Categories** - What types of content are most valuable",
        "🌐 **Platforms** - Which platforms have the best content for each topic",
        "📚 **Educational Value** - How to identify high-quality learning content",
        "🔗 **Related Topics** - How different subjects connect to each other"
    ]
    
    for aspect in learning_aspects:
        console.print(f"  {aspect}")
    
    console.print("\n[yellow]Automatic Learning:[/yellow]")
    console.print("  • Video intelligence develops automatically every 7th learning cycle")
    console.print("  • AI explores educational videos on current learning topics")
    console.print("  • Skills improve with every video search and analysis")
    console.print("  • Knowledge about channels and topics grows continuously")

def main():
    """Main test function"""
    
    console.print("[bold green]🧪 Video Intelligence Test Suite[/bold green]")
    console.print("This will test your AI's ability to search, analyze, and learn from videos!")
    console.print("=" * 60)
    
    # Show features
    show_video_features()
    
    console.print("\n" + "=" * 60)
    
    # Run comprehensive test
    success = test_video_intelligence()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: Video Intelligence Working![/bold green]")
        console.print("\n[cyan]Your AI can now:[/cyan]")
        console.print("  🎥 Search videos across YouTube, Vimeo, and Dailymotion")
        console.print("  🔍 Find relevant educational and entertainment content")
        console.print("  📊 Analyze video metadata and characteristics")
        console.print("  📚 Assess educational value of video content")
        console.print("  🧠 Learn from video topics and content")
        console.print("  🌐 Research video topics using web search")
        console.print("  📂 Automatically categorize videos by content type")
        console.print("  📺 Discover and learn about content creators")
        console.print("  🎯 Track explored topics and interests")
        console.print("  📈 Develop 8 different video intelligence skills")
        
        # Show usage examples
        show_usage_examples()
        
        console.print("\n[bold yellow]🎯 Try it now:[/bold yellow]")
        console.print("  python main_ai.py interactive")
        console.print("  Then use: search_videos artificial intelligence")
        console.print("  Or use: watch python tutorial")
        
    else:
        console.print("\n[bold red]❌ FAILED: There were issues with video intelligence[/bold red]")

if __name__ == "__main__":
    main()
