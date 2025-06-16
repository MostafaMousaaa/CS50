from cs50 import get_string

class PromptEngineeringDemo:
    def __init__(self):
        self.examples = {
            "basic_vs_specific": {
                "poor": "Write code",
                "better": "Write a Python function that calculates the factorial of a number using recursion, with error handling for negative inputs",
                "explanation": "Specific prompts with clear requirements yield better results"
            },
            
            "context_matters": {
                "poor": "Fix this bug",
                "better": "I'm working on a CS50 problem set in C. My program should calculate change owed but it's giving wrong results. Here's my code: [code]. The expected output is X but I'm getting Y. What's wrong?",
                "explanation": "Providing context, expected vs actual results helps AI understand the problem"
            },
            
            "step_by_step": {
                "poor": "Explain sorting algorithms",
                "better": "Explain bubble sort step by step: 1) How it works conceptually, 2) Show an example with numbers [64, 34, 25, 12], 3) Analyze time complexity, 4) Compare with other O(n²) algorithms",
                "explanation": "Breaking down complex requests into steps gets more comprehensive answers"
            },
            
            "examples_help": {
                "poor": "Generate test cases",
                "better": "Generate test cases for a function that validates email addresses. Include examples like: valid@email.com (valid), invalid.email (invalid), test@domain (invalid). Create 5 more test cases covering edge cases.",
                "explanation": "Providing examples shows the AI exactly what format and style you want"
            },
            
            "role_playing": {
                "poor": "Help me debug",
                "better": "Act as an experienced CS50 teaching assistant. A student is struggling with pointers in C. Their code has a segmentation fault. Walk them through debugging step by step, asking questions to help them discover the issue themselves.",
                "explanation": "Assigning a role helps the AI respond in the appropriate style and depth"
            }
        }
        
        self.techniques = {
            "be_specific": [
                "Instead of: 'Help me with my code'",
                "Try: 'Help me fix this C function that should reverse a string but crashes on line 15'",
                "Specificity reduces ambiguity and gets targeted help"
            ],
            
            "provide_context": [
                "Include relevant background information",
                "Mention what you've already tried",
                "Specify your experience level (beginner, intermediate, etc.)"
            ],
            
            "use_examples": [
                "Show input and expected output",
                "Include both working and non-working examples",
                "Demonstrate the format you want for responses"
            ],
            
            "break_down_complex": [
                "Split complex requests into smaller parts",
                "Number your sub-questions",
                "Ask for step-by-step explanations"
            ],
            
            "iterate_and_refine": [
                "Start with a basic prompt",
                "Refine based on the response you get",
                "Ask follow-up questions for clarification"
            ]
        }
    
    def show_before_after(self, category):
        """Show before/after example for a category"""
        example = self.examples[category]
        print(f"\n=== {category.replace('_', ' ').title()} ===")
        print(f"❌ Poor prompt: {example['poor']}")
        print(f"✅ Better prompt: {example['better']}")
        print(f"💡 Why it's better: {example['explanation']}")
    
    def demonstrate_all_examples(self):
        """Show all before/after examples"""
        print("=== Prompt Engineering Examples ===")
        for category in self.examples:
            self.show_before_after(category)
            print()
    
    def show_techniques(self):
        """Display prompt engineering techniques"""
        print("=== Prompt Engineering Techniques ===")
        for technique, tips in self.techniques.items():
            print(f"\n{technique.replace('_', ' ').title()}:")
            for tip in tips:
                print(f"  • {tip}")
    
    def prompt_analyzer(self, prompt):
        """Analyze a prompt and suggest improvements"""
        suggestions = []
        
        # Check length
        if len(prompt) < 20:
            suggestions.append("Consider being more specific - very short prompts often lack detail")
        
        # Check for context
        context_words = ['because', 'since', 'for', 'working on', 'trying to', 'need to']
        if not any(word in prompt.lower() for word in context_words):
            suggestions.append("Add context - explain what you're working on or why you need this")
        
        # Check for examples
        example_words = ['example', 'like', 'such as', 'e.g.', 'for instance']
        if not any(word in prompt.lower() for word in example_words):
            suggestions.append("Consider adding examples to clarify what you want")
        
        # Check for questions
        if '?' not in prompt:
            suggestions.append("Consider ending with a specific question")
        
        # Check for vague words
        vague_words = ['help', 'fix', 'make', 'do', 'thing', 'stuff']
        vague_found = [word for word in vague_words if word in prompt.lower()]
        if vague_found:
            suggestions.append(f"Replace vague words ({', '.join(vague_found)}) with specific terms")
        
        return suggestions
    
    def interactive_prompt_builder(self):
        """Help user build a better prompt interactively"""
        print("=== Interactive Prompt Builder ===")
        print("Let's build a better prompt together!")
        
        # Get basic request
        basic_request = get_string("What do you want help with? (basic description): ")
        
        # Get context
        context = get_string("What's the context? (what are you working on, your experience level, etc.): ")
        
        # Get specifics
        specifics = get_string("What specific part do you need help with?: ")
        
        # Get examples
        examples = get_string("Can you provide an example of what you want? (optional): ")
        
        # Build improved prompt
        improved_prompt = f"{basic_request}"
        
        if context:
            improved_prompt += f" I'm {context}."
        
        if specifics:
            improved_prompt += f" Specifically, I need help with {specifics}."
        
        if examples:
            improved_prompt += f" For example: {examples}."
        
        print(f"\n=== Your Improved Prompt ===")
        print(improved_prompt)
        
        # Analyze the improved prompt
        suggestions = self.prompt_analyzer(improved_prompt)
        if suggestions:
            print(f"\n=== Additional Suggestions ===")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"{i}. {suggestion}")
        else:
            print("\n✅ Great! Your prompt looks well-structured.")

def cs50_ai_demo():
    """Demonstrate CS50.ai concepts"""
    print("=== CS50.ai Concepts ===")
    print("\nCS50.ai is an AI-powered teaching assistant that:")
    print("• Helps students with coding questions")
    print("• Provides hints rather than direct answers")
    print("• Adapts to individual learning styles")
    print("• Available 24/7 for immediate help")
    
    print("\nEffective ways to use CS50.ai:")
    print("1. Ask specific questions about concepts you don't understand")
    print("2. Share your code when asking about bugs or errors")
    print("3. Ask for debugging strategies, not just solutions")
    print("4. Request explanations of error messages")
    print("5. Get help with testing your code")
    
    print("\nExample good questions for CS50.ai:")
    good_questions = [
        "I'm getting a segmentation fault on line 12 of my C program. How do I debug this?",
        "Can you explain the difference between malloc and calloc?",
        "My Caesar cipher is shifting letters incorrectly. What should I check?",
        "How do I test edge cases for my readability program?",
        "What's the best way to validate user input in C?"
    ]
    
    for i, question in enumerate(good_questions, 1):
        print(f"{i}. {question}")

def main():
    """Main program for prompt engineering demonstration"""
    demo = PromptEngineeringDemo()
    
    print("=== Prompt Engineering for AI ===")
    print("Learn how to craft effective prompts for AI systems!")
    
    while True:
        print("\nOptions:")
        print("1. See before/after examples")
        print("2. Learn prompt engineering techniques")
        print("3. Analyze a prompt")
        print("4. Build a better prompt interactively")
        print("5. CS50.ai tips")
        print("6. Exit")
        
        choice = get_string("Choose an option: ")
        
        if choice == "1":
            demo.demonstrate_all_examples()
        
        elif choice == "2":
            demo.show_techniques()
        
        elif choice == "3":
            user_prompt = get_string("Enter a prompt to analyze: ")
            suggestions = demo.prompt_analyzer(user_prompt)
            
            print(f"\n=== Analysis of: '{user_prompt}' ===")
            if suggestions:
                print("Suggestions for improvement:")
                for i, suggestion in enumerate(suggestions, 1):
                    print(f"{i}. {suggestion}")
            else:
                print("✅ This prompt looks well-structured!")
        
        elif choice == "4":
            demo.interactive_prompt_builder()
        
        elif choice == "5":
            cs50_ai_demo()
        
        elif choice == "6":
            print("Happy prompting! Remember: specific, contextual prompts get better results.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
