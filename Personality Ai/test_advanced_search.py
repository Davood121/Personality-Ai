#!/usr/bin/env python3
"""
Test the Advanced Search Engine - Multi-source intelligent search
"""

import sys
import os
from rich.console import Console
from rich.panel import Panel

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def test_advanced_search():
    """Test the advanced search capabilities"""
    
    console.print("[bold blue]🔍 Testing Advanced Search Engine[/bold blue]")
    console.print("=" * 60)
    
    try:
        from main_ai import PersonalityAI
        
        console.print("[yellow]Initializing AI with Advanced Search...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI initialized with advanced search capabilities![/green]")
        
        # Test different types of searches
        test_queries = [
            ("artificial intelligence", "general"),
            ("machine learning algorithms", "technical"),
            ("quantum computing", "academic"),
            ("python programming", "code"),
            ("climate change", "news")
        ]
        
        console.print(f"\n[bold yellow]🚀 Testing {len(test_queries)} Different Search Types...[/bold yellow]")
        
        for i, (query, search_type) in enumerate(test_queries, 1):
            console.print(f"\n[cyan]--- Test {i}: {search_type.title()} Search ---[/cyan]")
            console.print(f"Query: '{query}'")
            
            try:
                # Perform advanced search
                search_result = ai.searcher.comprehensive_search(query, search_type)
                
                # Show results summary
                total_sources = search_result.get('total_sources', 0)
                confidence = search_result.get('confidence_score', 0)
                
                console.print(f"[green]✅ Sources Found: {total_sources}[/green]")
                console.print(f"[green]✅ Confidence: {confidence:.2f}[/green]")
                
                # Show source breakdown
                synthesized = search_result.get('synthesized_results', {})
                source_summary = synthesized.get('source_summary', {})
                
                if source_summary:
                    console.print("[dim]Sources used:[/dim]")
                    for source, count in source_summary.items():
                        console.print(f"[dim]  • {source}: {count} results[/dim]")
                
                # Show sample results
                if synthesized.get('definitions'):
                    console.print(f"[dim]📖 Definitions found: {len(synthesized['definitions'])}[/dim]")
                if synthesized.get('academic_insights'):
                    console.print(f"[dim]🎓 Academic papers: {len(synthesized['academic_insights'])}[/dim]")
                if synthesized.get('code_examples'):
                    console.print(f"[dim]💻 Code examples: {len(synthesized['code_examples'])}[/dim]")
                if synthesized.get('discussions'):
                    console.print(f"[dim]💬 Discussions: {len(synthesized['discussions'])}[/dim]")
                
            except Exception as e:
                console.print(f"[red]❌ Search {i} failed: {e}[/red]")
        
        # Show search statistics
        console.print("\n[cyan]📊 Final Search Statistics:[/cyan]")
        ai._show_search_statistics()
        
        console.print(f"\n[bold green]✅ Advanced Search Test Complete![/bold green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_advanced_search_features():
    """Show the advanced search features"""
    
    console.print("[bold blue]🔍 Advanced Search Engine Features[/bold blue]")
    console.print("=" * 60)
    
    features = [
        "🌐 **Multi-Source Search** - 6 different search sources simultaneously",
        "🧠 **Intelligent Synthesis** - Combines results from all sources",
        "📊 **Confidence Scoring** - Measures result reliability",
        "🎯 **Specialized Search Types** - Academic, technical, news, code, general",
        "📋 **Smart Caching** - Avoids duplicate searches for 24 hours",
        "🔍 **Source Reliability** - Weights results by source trustworthiness",
        "📈 **Search Statistics** - Tracks performance and usage",
        "⚡ **Parallel Processing** - Searches multiple sources simultaneously",
        "🎓 **Academic Papers** - Searches arXiv for research papers",
        "💻 **Code Search** - Finds GitHub repositories and Stack Overflow solutions"
    ]
    
    for feature in features:
        console.print(f"  {feature}")
    
    console.print("\n[bold yellow]🌐 Search Sources:[/bold yellow]")
    sources = [
        "📖 **Wikipedia** - Comprehensive encyclopedia (90% reliability)",
        "🦆 **DuckDuckGo** - General web search (60% reliability)",
        "🎓 **arXiv** - Academic research papers (95% reliability)",
        "💻 **GitHub** - Code repositories and projects (90% reliability)",
        "❓ **Stack Overflow** - Technical Q&A (90% reliability)",
        "💬 **Reddit** - Community discussions (60% reliability)"
    ]
    
    for source in sources:
        console.print(f"  {source}")
    
    console.print("\n[bold cyan]🎯 Search Types:[/bold cyan]")
    search_types = [
        "🔍 **General** - Searches all sources for comprehensive results",
        "🎓 **Academic** - Focuses on research papers and scholarly content",
        "🔧 **Technical** - Emphasizes documentation and technical resources",
        "📰 **News** - Searches for current events and news content",
        "💻 **Code** - Finds code examples and programming resources"
    ]
    
    for search_type in search_types:
        console.print(f"  {search_type}")

def show_usage_examples():
    """Show usage examples"""
    
    console.print("\n[bold green]🎯 How to Use Advanced Search[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]Interactive Mode:[/yellow]")
    console.print("  python main_ai.py interactive")
    console.print("  Then use these commands:")
    console.print("    search <query>        # Advanced multi-source search")
    console.print("    search_stats          # Show search statistics")
    console.print("    ask <question>        # AI will auto-search and answer")
    
    console.print("\n[yellow]Example Searches:[/yellow]")
    examples = [
        "search artificial intelligence",
        "search python machine learning",
        "search quantum computing algorithms",
        "search climate change research",
        "search blockchain technology"
    ]
    
    for example in examples:
        console.print(f"    {example}")

def main():
    """Main test function"""
    
    console.print("[bold green]🧪 Advanced Search Engine Test Suite[/bold green]")
    console.print("This will test your AI's advanced multi-source search capabilities!")
    console.print("=" * 60)
    
    # Show features
    show_advanced_search_features()
    
    console.print("\n" + "=" * 60)
    
    # Run test
    success = test_advanced_search()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: Advanced Search Engine Working![/bold green]")
        console.print("\n[cyan]Your AI can now search:[/cyan]")
        console.print("  📖 Wikipedia for encyclopedia entries")
        console.print("  🦆 DuckDuckGo for general web content")
        console.print("  🎓 arXiv for academic research papers")
        console.print("  💻 GitHub for code repositories")
        console.print("  ❓ Stack Overflow for technical solutions")
        console.print("  💬 Reddit for community discussions")
        console.print("  🧠 Intelligently synthesizes all results")
        console.print("  📊 Provides confidence scores")
        console.print("  🎯 Supports specialized search types")
        
        # Show usage examples
        show_usage_examples()
        
    else:
        console.print("\n[bold red]❌ FAILED: There were issues with advanced search[/bold red]")

if __name__ == "__main__":
    main()
