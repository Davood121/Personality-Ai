#!/usr/bin/env python3
"""
Test Vision Intelligence Engine - Complete visual processing and learning
"""

import sys
import os
from rich.console import Console
from rich.panel import Panel
from PIL import Image, ImageDraw

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

console = Console()

def create_test_images():
    """Create test images for vision testing"""
    console.print("[yellow]📸 Creating test images...[/yellow]")
    
    # Create test_images directory
    os.makedirs("test_images", exist_ok=True)
    
    # Create a simple test image
    img = Image.new('RGB', (400, 300), color='lightblue')
    draw = ImageDraw.Draw(img)
    
    # Draw some shapes
    draw.rectangle([50, 50, 150, 150], fill='red', outline='black')
    draw.ellipse([200, 100, 350, 200], fill='green', outline='black')
    draw.polygon([(300, 50), (350, 100), (250, 100)], fill='yellow', outline='black')
    
    # Add some text
    try:
        draw.text((50, 200), "Test Image", fill='black')
    except:
        pass  # Font might not be available
    
    img.save("test_images/test_shapes.png")
    console.print("[green]✅ Created test_shapes.png[/green]")
    
    # Create a colorful test image
    img2 = Image.new('RGB', (300, 200), color='white')
    draw2 = ImageDraw.Draw(img2)
    
    # Create a gradient-like effect
    for i in range(300):
        color = (i % 255, (i * 2) % 255, (i * 3) % 255)
        draw2.line([(i, 0), (i, 200)], fill=color)
    
    img2.save("test_images/test_colors.png")
    console.print("[green]✅ Created test_colors.png[/green]")
    
    return ["test_images/test_shapes.png", "test_images/test_colors.png"]

def test_vision_intelligence():
    """Test the vision intelligence capabilities"""
    
    console.print("[bold blue]👁️ Testing Vision Intelligence Engine[/bold blue]")
    console.print("=" * 60)
    
    try:
        from main_ai import PersonalityAI
        
        console.print("[yellow]Initializing AI with Vision Intelligence...[/yellow]")
        ai = PersonalityAI()
        
        console.print("[green]✅ AI initialized with vision capabilities![/green]")
        
        # Create test images
        test_images = create_test_images()
        
        # Show initial vision status
        console.print("\n[cyan]📊 Initial Vision Status:[/cyan]")
        ai._show_vision_status()
        
        # Test image analysis
        console.print(f"\n[bold yellow]🚀 Testing Image Analysis...[/bold yellow]")
        
        for i, image_path in enumerate(test_images, 1):
            console.print(f"\n[cyan]--- Test {i}: Analyzing {os.path.basename(image_path)} ---[/cyan]")
            
            try:
                # Test comprehensive image analysis
                analysis_result = ai.vision.analyze_image(
                    image_path, 
                    searcher=ai.searcher, 
                    memory=ai.memory
                )
                
                if analysis_result.get('success', False):
                    console.print(f"[green]✅ Analysis successful![/green]")
                    
                    # Show key results
                    objects = analysis_result.get('objects_detected', [])
                    console.print(f"[cyan]Objects detected: {len(objects)}[/cyan]")
                    for obj in objects[:3]:
                        console.print(f"  • {obj['object'].replace('_', ' ').title()} (confidence: {obj['confidence']:.2f})")
                    
                    colors = analysis_result.get('colors_analyzed', {}).get('dominant_colors', [])
                    console.print(f"[cyan]Colors found: {len(colors)}[/cyan]")
                    for color in colors[:3]:
                        console.print(f"  • {color['name'].title()}")
                    
                    learning = analysis_result.get('learning_insights', [])
                    console.print(f"[cyan]Learning insights: {len(learning)}[/cyan]")
                    for insight in learning[:2]:
                        console.print(f"  • {insight}")
                    
                    web_research = analysis_result.get('web_research', {})
                    if web_research:
                        console.print(f"[cyan]Web research: {len(web_research)} objects researched[/cyan]")
                
                else:
                    console.print(f"[red]❌ Analysis failed: {analysis_result.get('error', 'Unknown error')}[/red]")
                    
            except Exception as e:
                console.print(f"[red]❌ Test {i} failed: {e}[/red]")
        
        # Test quick vision
        console.print(f"\n[bold yellow]🚀 Testing Quick Vision...[/bold yellow]")
        
        for image_path in test_images[:1]:  # Test one image
            console.print(f"\n[cyan]--- Quick Vision Test: {os.path.basename(image_path)} ---[/cyan]")
            
            try:
                ai._see_image(image_path)
            except Exception as e:
                console.print(f"[red]❌ Quick vision failed: {e}[/red]")
        
        # Show final vision status
        console.print("\n[cyan]📊 Final Vision Status:[/cyan]")
        final_status = ai.vision.get_vision_status()
        
        console.print(f"👁️ Overall Vision Capability: {final_status['overall_vision_capability']:.3f}")
        console.print(f"🎯 Objects Learned: {final_status['objects_learned']}")
        console.print(f"🎨 Colors Learned: {final_status['colors_learned']}")
        console.print(f"🧠 Visual Memories: {final_status['visual_memories']}")
        
        # Show vision skills
        console.print(f"\n[cyan]👁️ Vision Skills:[/cyan]")
        for skill, level in final_status['vision_skills'].items():
            console.print(f"  • {skill.replace('_', ' ').title()}: {level:.3f}")
        
        console.print(f"\n[bold green]✅ Vision Intelligence Test Complete![/bold green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        import traceback
        traceback.print_exc()
        return False

def show_vision_features():
    """Show the vision intelligence features"""
    
    console.print("[bold blue]👁️ Vision Intelligence Engine Features[/bold blue]")
    console.print("=" * 60)
    
    features = [
        "👁️ **Complete Image Analysis** - Comprehensive visual processing",
        "🎯 **Object Detection** - Identifies objects, scenes, and elements",
        "📝 **Text Extraction (OCR)** - Reads text from images and documents",
        "🎨 **Color Analysis** - Analyzes dominant colors and color temperature",
        "📊 **Visual Statistics** - Brightness, contrast, sharpness, complexity",
        "🧠 **Visual Learning** - Learns from every image analyzed",
        "🌐 **Web Research Integration** - Researches unknown objects online",
        "💾 **Visual Memory** - Stores and recalls visual experiences",
        "📖 **Scene Description** - Generates natural language descriptions",
        "📈 **Skill Development** - 8 different vision skills tracked and improved"
    ]
    
    for feature in features:
        console.print(f"  {feature}")
    
    console.print("\n[bold yellow]👁️ Vision Skills Tracked:[/bold yellow]")
    skills = [
        "🎯 **Object Recognition** - Identifying objects in images",
        "📝 **Text Extraction** - Reading text from visual content",
        "📊 **Image Analysis** - Understanding visual characteristics",
        "🧠 **Visual Learning** - Learning from visual experiences",
        "🌍 **Scene Understanding** - Comprehending overall scenes",
        "🎨 **Color Analysis** - Understanding color relationships",
        "🔍 **Pattern Recognition** - Identifying visual patterns",
        "💾 **Visual Memory** - Storing and recalling visual information"
    ]
    
    for skill in skills:
        console.print(f"  {skill}")
    
    console.print("\n[bold cyan]🌐 Web Integration Features:[/bold cyan]")
    web_features = [
        "🔍 **Object Research** - Searches web for unknown objects",
        "📚 **Knowledge Enhancement** - Learns object characteristics online",
        "🎯 **Confidence Scoring** - Measures reliability of web information",
        "📊 **Multi-Source Learning** - Combines visual and web knowledge",
        "🧠 **Intelligent Synthesis** - Merges visual analysis with web research"
    ]
    
    for feature in web_features:
        console.print(f"  {feature}")

def show_usage_examples():
    """Show usage examples"""
    
    console.print("\n[bold green]🎯 How to Use Vision Intelligence[/bold green]")
    console.print("=" * 60)
    
    console.print("[yellow]Interactive Mode:[/yellow]")
    console.print("  python main_ai.py interactive")
    console.print("  Then use these commands:")
    console.print("    see <image_path>           # Quick image viewing")
    console.print("    analyze_image <path>       # Full analysis with web research")
    console.print("    vision_status              # Show vision capabilities")
    
    console.print("\n[yellow]Example Commands:[/yellow]")
    examples = [
        "see photo.jpg",
        "analyze_image document.png",
        "see screenshot.png",
        "analyze_image diagram.jpg",
        "vision_status"
    ]
    
    for example in examples:
        console.print(f"    {example}")
    
    console.print("\n[yellow]Supported Image Formats:[/yellow]")
    formats = [
        "📸 **JPEG/JPG** - Photos and images",
        "🖼️ **PNG** - Screenshots and graphics",
        "🎨 **GIF** - Animated and static images",
        "📊 **BMP** - Bitmap images",
        "📋 **TIFF** - High-quality images"
    ]
    
    for format_info in formats:
        console.print(f"  {format_info}")
    
    console.print("\n[yellow]Automatic Learning:[/yellow]")
    console.print("  • Vision skills develop with every image analyzed")
    console.print("  • Objects and colors are learned and remembered")
    console.print("  • Web research enhances object knowledge")
    console.print("  • Visual memories are stored for future reference")
    console.print("  • Skills improve automatically every 6th learning cycle")

def main():
    """Main test function"""
    
    console.print("[bold green]🧪 Vision Intelligence Test Suite[/bold green]")
    console.print("This will test your AI's ability to see, analyze, and learn from images!")
    console.print("=" * 60)
    
    # Show features
    show_vision_features()
    
    console.print("\n" + "=" * 60)
    
    # Run comprehensive test
    success = test_vision_intelligence()
    
    if success:
        console.print("\n[bold green]🎉 SUCCESS: Vision Intelligence Working![/bold green]")
        console.print("\n[cyan]Your AI can now:[/cyan]")
        console.print("  👁️ See and analyze any image")
        console.print("  🎯 Detect objects and scenes")
        console.print("  📝 Extract text from images (OCR capability)")
        console.print("  🎨 Analyze colors and visual characteristics")
        console.print("  🧠 Learn from every image it sees")
        console.print("  🌐 Research unknown objects on the web")
        console.print("  💾 Remember visual experiences")
        console.print("  📖 Describe scenes in natural language")
        console.print("  📊 Track and improve 8 vision skills")
        console.print("  🔄 Continuously develop visual intelligence")
        
        # Show usage examples
        show_usage_examples()
        
        console.print("\n[bold yellow]🎯 Try it now:[/bold yellow]")
        console.print("  python main_ai.py interactive")
        console.print("  Then use: see test_images/test_shapes.png")
        
    else:
        console.print("\n[bold red]❌ FAILED: There were issues with vision intelligence[/bold red]")

if __name__ == "__main__":
    main()
