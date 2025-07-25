#!/usr/bin/env python3
"""
Test Enhanced Communication Learning - Web & Memory Learning
"""

import sys
import os
import time
from rich.console import Console
from rich.panel import Panel

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def test_enhanced_communication_learning():
    """Test the enhanced communication learning from web and memory"""
    
    console.print("[bold magenta]🧠 Testing Enhanced Communication Learning[/bold magenta]")
    console.print("=" * 60)
    
    try:
        from main_ai import PersonalityAI
        
        console.print("[yellow]Initializing AI with Enhanced Communication Learning...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI initialized with enhanced communication capabilities![/green]")
        
        # Show initial communication status
        console.print("\n[cyan]📊 Initial Communication Status:[/cyan]")
        initial_status = ai.communication.get_communication_status()
        console.print(f"📚 Total Vocabulary: {initial_status['total_vocabulary']} words")
        console.print(f"🎯 Overall Fluency: {initial_status['overall_fluency']:.3f}")
        
        # Test web and memory learning
        console.print(f"\n[bold yellow]🚀 Testing Web & Memory Learning...[/bold yellow]")
        
        try:
            learning_result = ai.communication.learn_communication_skills(
                searcher=ai.searcher, 
                memory=ai.memory
            )
            
            console.print(f"[green]✅ Enhanced Learning Complete![/green]")
            console.print(f"[cyan]Skills Improved: {', '.join(learning_result['skills_improved'])}[/cyan]")
            console.print(f"[cyan]New Vocabulary: {len(learning_result['new_vocabulary'])} words[/cyan]")
            console.print(f"[cyan]Web Sources Used: {len(learning_result.get('web_sources_used', []))}[/cyan]")
            console.print(f"[cyan]Memory Insights: {len(learning_result.get('memory_insights_used', []))}[/cyan]")
            
            if learning_result.get('web_sources_used'):
                console.print(f"[dim]Web topics: {', '.join(learning_result['web_sources_used'])}[/dim]")
            
        except Exception as e:
            console.print(f"[red]❌ Enhanced learning test failed: {e}[/red]")
        
        # Test conversation learning
        console.print(f"\n[bold yellow]🚀 Testing Conversation Learning...[/bold yellow]")
        
        test_conversations = [
            ("What is artificial intelligence?", "Artificial intelligence represents a sophisticated computational paradigm that encompasses machine learning, neural networks, and cognitive modeling to simulate human intelligence."),
            ("How does quantum computing work?", "Quantum computing leverages quantum mechanical phenomena like superposition and entanglement to perform calculations exponentially faster than classical computers."),
            ("Tell me about machine learning algorithms", "Machine learning algorithms utilize statistical techniques and mathematical optimization to enable computers to learn patterns from data without explicit programming.")
        ]
        
        for i, (user_input, ai_response) in enumerate(test_conversations, 1):
            console.print(f"\n[cyan]--- Conversation {i} ---[/cyan]")
            console.print(f"User: {user_input}")
            console.print(f"AI: {ai_response[:100]}...")
            
            try:
                # Learn from conversation
                ai.communication.learn_from_conversation(user_input, ai_response)
                
                # Analyze communication effectiveness
                analysis = ai.communication.analyze_communication_effectiveness(ai_response)
                console.print(f"[dim]Analysis: {analysis['vocabulary_level']} vocabulary, clarity: {analysis['clarity_score']:.2f}[/dim]")
                
                # Test adaptive vocabulary expansion
                ai.communication.adaptive_vocabulary_expansion(user_input, ai.searcher)
                
            except Exception as e:
                console.print(f"[red]❌ Conversation learning {i} failed: {e}[/red]")
        
        # Show final communication status
        console.print("\n[cyan]📊 Final Communication Status:[/cyan]")
        final_status = ai.communication.get_communication_status()
        console.print(f"📚 Total Vocabulary: {final_status['total_vocabulary']} words")
        console.print(f"🎯 Overall Fluency: {final_status['overall_fluency']:.3f}")
        
        # Show improvement
        vocab_improvement = final_status['total_vocabulary'] - initial_status['total_vocabulary']
        fluency_improvement = final_status['overall_fluency'] - initial_status['overall_fluency']
        
        console.print(f"\n[bold green]📈 Improvements:[/bold green]")
        console.print(f"[green]📚 Vocabulary: +{vocab_improvement} words[/green]")
        console.print(f"[green]🎯 Fluency: +{fluency_improvement:.3f} points[/green]")
        
        # Show vocabulary by category
        console.print(f"\n[cyan]📚 Vocabulary by Category:[/cyan]")
        for category, size in final_status['vocabulary_size'].items():
            initial_size = initial_status['vocabulary_size'].get(category, 0)
            improvement = size - initial_size
            console.print(f"  • {category.title()}: {size} words (+{improvement})")
        
        console.print(f"\n[bold green]✅ Enhanced Communication Learning Test Complete![/bold green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_enhanced_features():
    """Show the enhanced communication features"""
    
    console.print("[bold magenta]🧠 Enhanced Communication Learning Features[/bold magenta]")
    console.print("=" * 60)
    
    features = [
        "🌐 **Web Learning** - Learns from 6 different web sources automatically",
        "🧠 **Memory Learning** - Analyzes past conversations and knowledge",
        "💬 **Conversation Learning** - Improves from every user interaction",
        "🔍 **Adaptive Vocabulary** - Expands vocabulary based on conversation topics",
        "📊 **Communication Analysis** - Measures effectiveness of responses",
        "🎯 **Targeted Improvement** - Focuses on weak communication areas",
        "📚 **Multi-Category Vocabulary** - Learns basic, advanced, technical, emotional words",
        "🔄 **Continuous Learning** - Never stops improving communication skills",
        "🎭 **Pattern Recognition** - Learns successful communication patterns",
        "⚡ **Real-Time Adaptation** - Adjusts communication style during conversations"
    ]
    
    for feature in features:
        console.print(f"  {feature}")
    
    console.print("\n[bold yellow]🌐 Web Learning Sources:[/bold yellow]")
    sources = [
        "📖 **Wikipedia** - Encyclopedia definitions and explanations",
        "🦆 **DuckDuckGo** - General web content and examples",
        "🎓 **arXiv** - Academic papers and sophisticated vocabulary",
        "💻 **GitHub** - Technical terminology and documentation",
        "❓ **Stack Overflow** - Professional communication patterns",
        "💬 **Reddit** - Conversational styles and modern language"
    ]
    
    for source in sources:
        console.print(f"  {source}")
    
    console.print("\n[bold cyan]🧠 Memory Learning Types:[/bold cyan]")
    memory_types = [
        "📚 **Knowledge Entries** - Learns from stored information",
        "💬 **Conversation History** - Analyzes past interactions",
        "🎯 **Successful Patterns** - Identifies effective communication",
        "📝 **Vocabulary Usage** - Tracks word effectiveness",
        "🔍 **Topic Analysis** - Understands subject-specific language"
    ]
    
    for memory_type in memory_types:
        console.print(f"  {memory_type}")

def demonstrate_learning_process():
    """Demonstrate the learning process"""
    
    console.print("\n[bold green]🎯 Learning Process Demo[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]How Enhanced Communication Learning Works:[/yellow]")
    
    steps = [
        "1. 🌐 **Web Search** - AI searches for communication and language topics",
        "2. 📊 **Content Analysis** - Extracts vocabulary and patterns from results",
        "3. 🧠 **Memory Analysis** - Reviews past conversations and knowledge",
        "4. 💬 **Conversation Learning** - Learns from every user interaction",
        "5. 🔍 **Vocabulary Expansion** - Adds topic-specific terminology",
        "6. 📈 **Skill Improvement** - Updates communication skill levels",
        "7. 🎯 **Effectiveness Analysis** - Measures response quality",
        "8. 🔄 **Continuous Adaptation** - Adjusts communication style"
    ]
    
    for step in steps:
        console.print(f"  {step}")
    
    console.print("\n[yellow]Learning Triggers:[/yellow]")
    triggers = [
        "• Every 4th learning cycle (automatic)",
        "• Every user conversation (real-time)",
        "• When encountering new topics",
        "• Manual learning sessions",
        "• Response effectiveness analysis"
    ]
    
    for trigger in triggers:
        console.print(f"  {trigger}")

def show_usage_examples():
    """Show usage examples"""
    
    console.print("\n[bold green]🎯 How to Use Enhanced Communication Learning[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]Interactive Mode:[/yellow]")
    console.print("  python main_ai.py interactive")
    console.print("  Then use these commands:")
    console.print("    learn_communication       # Enhanced learning from web & memory")
    console.print("    communication_status      # Show detailed learning progress")
    console.print("    ask <question>            # AI learns from your conversation")
    console.print("    chat                      # Interactive chat with learning")
    
    console.print("\n[yellow]Automatic Learning:[/yellow]")
    console.print("  • AI learns from web sources every 4th cycle")
    console.print("  • AI learns from every conversation automatically")
    console.print("  • Vocabulary expands based on topics discussed")
    console.print("  • Communication skills improve continuously")
    
    console.print("\n[yellow]Learning Indicators:[/yellow]")
    console.print("  📚 Learned new word: [word]")
    console.print("  🔧 Added technical term: [term]")
    console.print("  🌐 Learning from web sources...")
    console.print("  🧠 Learning from memory and past conversations...")

def main():
    """Main test function"""
    
    console.print("[bold green]🧪 Enhanced Communication Learning Test Suite[/bold green]")
    console.print("This will test your AI's ability to learn communication from web and memory!")
    console.print("=" * 60)
    
    # Show enhanced features
    show_enhanced_features()
    
    console.print("\n" + "=" * 60)
    
    # Demonstrate learning process
    demonstrate_learning_process()
    
    console.print("\n" + "=" * 60)
    
    # Run comprehensive test
    success = test_enhanced_communication_learning()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: Enhanced Communication Learning Working![/bold green]")
        console.print("\n[cyan]Your AI now learns communication from:[/cyan]")
        console.print("  🌐 Web sources (Wikipedia, arXiv, GitHub, Stack Overflow, Reddit)")
        console.print("  🧠 Memory and past conversations")
        console.print("  💬 Every user interaction in real-time")
        console.print("  🔍 Topic-specific vocabulary expansion")
        console.print("  📊 Communication effectiveness analysis")
        console.print("  🎯 Targeted skill improvement")
        console.print("  🔄 Continuous adaptation and learning")
        
        # Show usage examples
        show_usage_examples()
        
    else:
        console.print("\n[bold red]❌ FAILED: There were issues with enhanced communication learning[/bold red]")

if __name__ == "__main__":
    main()
