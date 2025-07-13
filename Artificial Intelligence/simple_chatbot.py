import random
import re
from cs50 import get_string

class SimpleChatbot:
    def __init__(self):
        self.name = "CS50 Bot"
        self.patterns = {
            # Greetings
            r'hello|hi|hey': [
                "Hello! How can I help you today?",
                "Hi there! What would you like to talk about?",
                "Hey! I'm here to chat with you."
            ],
            
            # Questions about the bot
            r'what.*your.*name|who.*are.*you': [
                f"I'm {self.name}, a simple chatbot created for CS50!",
                "I'm an AI chatbot designed to demonstrate conversation patterns.",
                f"My name is {self.name}. I'm here to help and chat!"
            ],
            
            # How are you
            r'how.*are.*you|how.*you.*doing': [
                "I'm doing well, thank you for asking!",
                "I'm great! Always ready to chat.",
                "I'm functioning perfectly, thanks!"
            ],
            
            # CS50 related
            r'cs50|computer.*science|programming|coding': [
                "CS50 is an amazing introduction to computer science!",
                "Programming is a powerful skill. Are you enjoying learning to code?",
                "Computer science opens up so many possibilities. What interests you most?"
            ],
            
            # AI related
            r'artificial.*intelligence|machine.*learning|ai': [
                "AI is fascinating! It's amazing how computers can learn and make decisions.",
                "Machine learning is transforming many industries. What aspects interest you?",
                "AI has incredible potential, but we must consider ethics and limitations too."
            ],
            
            # Help requests
            r'help|stuck|problem|error': [
                "I'd be happy to help! Can you tell me more about what you're working on?",
                "Don't worry, everyone gets stuck sometimes. What specific issue are you facing?",
                "I'm here to help! Describe the problem and I'll do my best to assist."
            ],
            
            # Feelings
            r'frustrated|angry|mad': [
                "I understand programming can be frustrating. Take a break if you need to!",
                "It's normal to feel that way when learning something new. You've got this!",
                "Debugging can be annoying, but each error teaches you something new."
            ],
            
            r'happy|excited|great': [
                "That's wonderful! I'm glad you're feeling positive.",
                "Great to hear! What's making you happy?",
                "Excellent! Positive energy makes learning more enjoyable."
            ],
            
            # Goodbye
            r'bye|goodbye|see.*you|exit|quit': [
                "Goodbye! Thanks for chatting with me.",
                "See you later! Keep up the great work in CS50!",
                "Bye! Feel free to come back anytime you want to chat."
            ],
            
            # Questions
            r'\?': [
                "That's an interesting question! Let me think about that.",
                "Good question! What do you think about it?",
                "I'm not sure about that, but I'd love to explore it with you."
            ]
        }
        
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I see. Can you elaborate on that?",
            "Hmm, I'm not sure I understand completely. Can you rephrase?",
            "That sounds important to you. Why is that?",
            "I'd like to learn more about your perspective on that."
        ]
        
        self.conversation_history = []
    
    def find_pattern_match(self, user_input):
        """Find matching pattern in user input"""
        user_input = user_input.lower()
        
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        return None
    
    def generate_response(self, user_input):
        """Generate response to user input"""
        # Store conversation
        self.conversation_history.append(("User", user_input))
        
        # Check for pattern match
        response = self.find_pattern_match(user_input)
        
        # Use default response if no pattern matches
        if not response:
            response = random.choice(self.default_responses)
        
        # Store bot response
        self.conversation_history.append(("Bot", response))
        
        return response
    
    def show_conversation_history(self):
        """Display conversation history"""
        print("\n=== Conversation History ===")
        for speaker, message in self.conversation_history:
            print(f"{speaker}: {message}")
    
    def get_conversation_stats(self):
        """Get statistics about the conversation"""
        user_messages = [msg for speaker, msg in self.conversation_history if speaker == "User"]
        bot_messages = [msg for speaker, msg in self.conversation_history if speaker == "Bot"]
        
        stats = {
            "total_exchanges": len(user_messages),
            "avg_user_message_length": sum(len(msg) for msg in user_messages) / len(user_messages) if user_messages else 0,
            "avg_bot_message_length": sum(len(msg) for msg in bot_messages) / len(bot_messages) if bot_messages else 0
        }
        
        return stats

def demonstrate_ai_concepts():
    """Demonstrate AI and chatbot concepts"""
    print("=== AI Chatbot Concepts ===")
    print("\n1. Pattern Matching:")
    print("   - Chatbot uses regular expressions to find patterns")
    print("   - Maps patterns to appropriate responses")
    print("   - Simple but effective for basic conversation")
    
    print("\n2. Natural Language Processing:")
    print("   - Understanding human language is complex")
    print("   - Modern chatbots use machine learning")
    print("   - Context and intent recognition are crucial")
    
    print("\n3. Conversation Flow:")
    print("   - Maintaining context across exchanges")
    print("   - Handling unexpected input gracefully")
    print("   - Providing helpful and relevant responses")
    
    print("\n4. Limitations:")
    print("   - Rule-based systems are brittle")
    print("   - Limited understanding of context")
    print("   - Cannot truly 'understand' like humans")
    
    print("\n5. Modern Improvements:")
    print("   - Large language models (GPT, etc.)")
    print("   - Deep learning for better understanding")
    print("   - Training on massive text datasets")

def chat_with_bot():
    """Main chat interface"""
    bot = SimpleChatbot()
    print(f"Hello! I'm {bot.name}. Type your message or 'quit' to exit.")
    print("You can also type 'history' to see our conversation or 'stats' for statistics.")
    
    while True:
        user_input = get_string("\nYou: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"{bot.name}: Goodbye! Thanks for chatting!")
            break
        elif user_input.lower() == 'history':
            bot.show_conversation_history()
            continue
        elif user_input.lower() == 'stats':
            stats = bot.get_conversation_stats()
            print(f"\n=== Chat Statistics ===")
            print(f"Total exchanges: {stats['total_exchanges']}")
            print(f"Average user message length: {stats['avg_user_message_length']:.1f} characters")
            print(f"Average bot message length: {stats['avg_bot_message_length']:.1f} characters")
            continue
        
        response = bot.generate_response(user_input)
        print(f"{bot.name}: {response}")

def test_chatbot():
    """Test chatbot with predefined inputs"""
    bot = SimpleChatbot()
    test_inputs = [
        "Hello there!",
        "What's your name?",
        "I'm learning about AI in CS50",
        "I'm stuck on a programming problem",
        "This is really frustrating!",
        "Thanks for the help, goodbye!"
    ]
    
    print("=== Chatbot Testing ===")
    for test_input in test_inputs:
        response = bot.generate_response(test_input)
        print(f"User: {test_input}")
        print(f"Bot: {response}\n")

def main():
    """Main program"""
    print("=== Simple AI Chatbot ===")
    
    while True:
        print("\nOptions:")
        print("1. Chat with the bot")
        print("2. Test the bot")
        print("3. Learn about AI concepts")
        print("4. Exit")
        
        choice = get_string("Choose an option: ")
        
        if choice == "1":
            chat_with_bot()
        elif choice == "2":
            test_chatbot()
        elif choice == "3":
            demonstrate_ai_concepts()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
