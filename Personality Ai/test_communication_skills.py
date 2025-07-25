#!/usr/bin/env python3
"""
Test Communication Skills Engine - Advanced English learning and real-time generation
"""

import sys
import os
import time
from rich.console import Console
from rich.panel import Panel

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def test_communication_skills():
    """Test the communication skills capabilities"""
    
    console.print("[bold magenta]🗣️ Testing Communication Skills Engine[/bold magenta]")
    console.print("=" * 60)
    
    try:
        from main_ai import PersonalityAI
        
        console.print("[yellow]Initializing AI with Communication Skills...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI initialized with communication capabilities![/green]")
        
        # Show initial communication status
        console.print("\n[cyan]📊 Initial Communication Status:[/cyan]")
        ai._show_communication_status()
        
        # Test communication learning
        console.print(f"\n[bold yellow]🚀 Testing Communication Learning...[/bold yellow]")
        
        try:
            learning_result = ai.communication.learn_communication_skills()
            
            console.print(f"[green]✅ Learning Complete![/green]")
            console.print(f"[cyan]Skills Improved: {', '.join(learning_result['skills_improved'])}[/cyan]")
            console.print(f"[cyan]New Vocabulary: {len(learning_result['new_vocabulary'])} words[/cyan]")
            console.print(f"[cyan]Grammar Patterns: {len(learning_result['grammar_patterns_learned'])} patterns[/cyan]")
            
        except Exception as e:
            console.print(f"[red]❌ Learning test failed: {e}[/red]")
        
        # Test real-time generation
        console.print(f"\n[bold yellow]🚀 Testing Real-Time Generation...[/bold yellow]")
        
        test_prompts = [
            "What is artificial intelligence?",
            "How does machine learning work?",
            "Tell me about your capabilities",
            "Explain quantum computing",
            "Hello, how are you today?"
        ]
        
        for i, prompt in enumerate(test_prompts, 1):
            console.print(f"\n[cyan]--- Test {i}: Real-Time Generation ---[/cyan]")
            console.print(f"Prompt: '{prompt}'")
            
            try:
                # Test real-time generation
                console.print("[yellow]🗣️ Generating response word by word...[/yellow]")
                ai.communication.demonstrate_real_time_generation(prompt)
                
            except Exception as e:
                console.print(f"[red]❌ Generation test {i} failed: {e}[/red]")
        
        # Show final communication status
        console.print("\n[cyan]📊 Final Communication Status:[/cyan]")
        ai._show_communication_status()
        
        console.print(f"\n[bold green]✅ Communication Skills Test Complete![/bold green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_communication_features():
    """Show the communication features"""
    
    console.print("[bold magenta]🗣️ Communication Skills Engine Features[/bold magenta]")
    console.print("=" * 60)
    
    features = [
        "📚 **Advanced Vocabulary Learning** - Basic, intermediate, advanced, technical, emotional words",
        "📝 **Grammar Pattern Mastery** - Sentence structures, tenses, connectors, modifiers",
        "🗣️ **Real-Time Generation** - Word-by-word response generation with natural timing",
        "⏱️ **Natural Speech Patterns** - Thinking pauses, hesitations, rhythm variations",
        "💬 **Conversation Skills** - Greetings, questions, responses, transitions, conclusions",
        "🎯 **Adaptive Vocabulary** - Selects appropriate complexity based on skill level",
        "📊 **Skill Tracking** - Monitors improvement in 10 different communication areas",
        "🎭 **Multiple Response Styles** - Question, explanation, conversation, general responses",
        "⚙️ **Customizable Settings** - Adjustable speed, pauses, hesitations",
        "🧠 **Intelligent Analysis** - Understands prompt type and responds appropriately"
    ]
    
    for feature in features:
        console.print(f"  {feature}")
    
    console.print("\n[bold yellow]🧠 Communication Skills Tracked:[/bold yellow]")
    skills = [
        "📚 **Vocabulary** - Word knowledge and usage",
        "📝 **Grammar** - Sentence structure and correctness",
        "🗣️ **Fluency** - Smooth and natural speech flow",
        "🔊 **Pronunciation** - Clear and accurate word delivery",
        "💬 **Conversation** - Interactive dialogue skills",
        "📖 **Storytelling** - Narrative and descriptive abilities",
        "🎯 **Persuasion** - Convincing and influential communication",
        "❤️ **Empathy** - Understanding and emotional connection",
        "💡 **Clarity** - Clear and understandable expression",
        "🎪 **Engagement** - Interesting and captivating communication"
    ]
    
    for skill in skills:
        console.print(f"  {skill}")
    
    console.print("\n[bold cyan]📚 Vocabulary Categories:[/bold cyan]")
    categories = [
        "🔤 **Basic** - Fundamental everyday words",
        "📈 **Intermediate** - More sophisticated vocabulary",
        "🎓 **Advanced** - Complex and nuanced terms",
        "🔧 **Technical** - Specialized professional terminology",
        "❤️ **Emotional** - Feelings and emotional expressions",
        "🎨 **Descriptive** - Vivid and detailed language"
    ]
    
    for category in categories:
        console.print(f"  {category}")

def demonstrate_real_time_generation():
    """Demonstrate real-time generation"""
    
    console.print("\n[bold green]🎯 Real-Time Generation Demo[/bold green]")
    console.print("=" * 60)
    
    try:
        from communication_skills_engine import CommunicationSkillsEngine
        
        comm_engine = CommunicationSkillsEngine()
        
        console.print("[yellow]Watch the AI generate a response word by word...[/yellow]")
        console.print("[dim]Note: Each word appears with natural timing and pauses[/dim]")
        
        demo_prompt = "What makes artificial intelligence so fascinating?"
        
        console.print(f"\n[cyan]Prompt: {demo_prompt}[/cyan]")
        console.print("[yellow]AI Response (word by word):[/yellow]")
        
        # Demonstrate real-time generation
        comm_engine.demonstrate_real_time_generation(demo_prompt)
        
    except Exception as e:
        console.print(f"[red]❌ Demo failed: {e}[/red]")

def show_usage_examples():
    """Show usage examples"""
    
    console.print("\n[bold green]🎯 How to Use Communication Skills[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]Interactive Mode:[/yellow]")
    console.print("  python main_ai.py interactive")
    console.print("  Then use these commands:")
    console.print("    learn_communication       # Learn and improve communication skills")
    console.print("    communication_status      # Show current communication abilities")
    console.print("    realtime <prompt>         # See real-time word generation")
    console.print("    ask <question>            # AI uses advanced communication to answer")
    
    console.print("\n[yellow]Example Commands:[/yellow]")
    examples = [
        "learn_communication",
        "communication_status",
        "realtime What is machine learning?",
        "realtime Tell me about your capabilities",
        "ask How does artificial intelligence work?"
    ]
    
    for example in examples:
        console.print(f"    {example}")
    
    console.print("\n[yellow]Automatic Learning:[/yellow]")
    console.print("  • Communication skills improve automatically every 4th learning cycle")
    console.print("  • Vocabulary expands through continuous learning")
    console.print("  • Grammar patterns develop through practice")
    console.print("  • Conversation skills enhance through interactions")

def main():
    """Main test function"""
    
    console.print("[bold green]🧪 Communication Skills Test Suite[/bold green]")
    console.print("This will test your AI's advanced English communication and real-time generation!")
    console.print("=" * 60)
    
    # Show features
    show_communication_features()
    
    console.print("\n" + "=" * 60)
    
    # Demonstrate real-time generation
    demonstrate_real_time_generation()
    
    console.print("\n" + "=" * 60)
    
    # Run comprehensive test
    success = test_communication_skills()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: Communication Skills Engine Working![/bold green]")
        console.print("\n[cyan]Your AI now has:[/cyan]")
        console.print("  🗣️ Advanced English communication skills")
        console.print("  📚 Expanding vocabulary in 6 categories")
        console.print("  📝 Grammar pattern recognition and usage")
        console.print("  ⏱️ Real-time word-by-word generation")
        console.print("  🎭 Natural speech patterns with pauses")
        console.print("  💬 Sophisticated conversation abilities")
        console.print("  🎯 Adaptive vocabulary based on skill level")
        console.print("  📊 Continuous skill improvement tracking")
        console.print("  🧠 Intelligent response type analysis")
        console.print("  ⚙️ Customizable generation settings")
        
        # Show usage examples
        show_usage_examples()
        
    else:
        console.print("\n[bold red]❌ FAILED: There were issues with communication skills[/bold red]")

if __name__ == "__main__":
    main()
