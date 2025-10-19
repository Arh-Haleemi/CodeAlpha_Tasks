import random
import re

def chatbot():
    """Simple rule-based chatbot with predefined responses."""
    
    # Define response patterns
    responses = {
        'greetings': {
            'patterns': [r'\b(hello|hi|hey|good morning|good afternoon|good evening)\b'],
            'responses': [
                "Hi there! How can I help you today?",
                "Hello! Nice to meet you!",
                "Hey! What's on your mind?",
                "Hi! How are you doing?",
                "Hello! Great to see you!"
            ]
        },
        'how_are_you': {
            'patterns': [r'\b(how are you|how do you do|how\'s it going|what\'s up)\b'],
            'responses': [
                "I'm doing great, thanks for asking!",
                "I'm fine, thank you! How about you?",
                "All good here! How are you?",
                "I'm fantastic! Thanks for asking!",
                "Doing well, thanks! What about you?"
            ]
        },
        'goodbye': {
            'patterns': [r'\b(bye|goodbye|see you|farewell|take care|exit|quit)\b'],
            'responses': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! It was nice talking to you!",
                "Farewell! Come back soon!",
                "Take care! See you next time!"
            ]
        },
        'name': {
            'patterns': [r'\b(what\'s your name|who are you|your name)\b'],
            'responses': [
                "I'm ChatBot, your friendly assistant!",
                "You can call me ChatBot!",
                "I'm ChatBot, nice to meet you!",
                "My name is ChatBot, at your service!"
            ]
        },
        'weather': {
            'patterns': [r'\b(weather|sunny|rainy|cold|hot|temperature)\b'],
            'responses': [
                "I wish I could check the weather for you, but I don't have access to real-time data!",
                "I'm not connected to weather services, but I hope it's nice where you are!",
                "I can't check the weather, but I hope you're having a beautiful day!",
                "Weather updates aren't my specialty, but I hope it's perfect weather for you!"
            ]
        },
        'help': {
            'patterns': [r'\b(help|what can you do|commands|options)\b'],
            'responses': [
                "I can chat with you! Try saying hello, asking how I am, or saying goodbye!",
                "I'm a simple chatbot. I can respond to greetings, questions about how I'm doing, and farewells!",
                "I can have basic conversations! Say hi, ask about me, or chat about the weather!",
                "I'm here to chat! I understand greetings, questions about myself, and goodbyes!"
            ]
        },
        'thank_you': {
            'patterns': [r'\b(thank you|thanks|appreciate)\b'],
            'responses': [
                "You're very welcome!",
                "No problem at all!",
                "Happy to help!",
                "My pleasure!",
                "Anytime! Glad I could help!"
            ]
        }
    }
    
    # Default responses for unmatched input
    default_responses = [
        "That's interesting! Tell me more.",
        "I'm not sure I understand. Can you rephrase that?",
        "Hmm, I don't have a good response for that. Try asking me something else!",
        "That's beyond my knowledge. Is there something else I can help with?",
        "I'm still learning! Can you try a different question?",
        "I didn't quite get that. Maybe try saying hello or asking how I am?"
    ]
    
    print("=== SIMPLE CHATBOT ===")
    print("Hi! I'm a friendly chatbot. Type 'quit', 'exit', or 'bye' to end our conversation.")
    print("Try saying hello, asking how I am, or asking what I can do!\n")
    
    conversation_history = []
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            if not user_input:
                print("ChatBot: Please say something!")
                continue
            
            # Store in conversation history
            conversation_history.append(f"User: {user_input}")
            
            # Convert to lowercase for pattern matching
            user_input_lower = user_input.lower()
            
            # Check for goodbye patterns first
            for pattern in responses['goodbye']['patterns']:
                if re.search(pattern, user_input_lower):
                    response = random.choice(responses['goodbye']['responses'])
                    print(f"ChatBot: {response}")
                    conversation_history.append(f"ChatBot: {response}")
                    return
            
            # Look for matching patterns
            response_found = False
            for category, data in responses.items():
                if category == 'goodbye':  # Already handled above
                    continue
                    
                for pattern in data['patterns']:
                    if re.search(pattern, user_input_lower):
                        response = random.choice(data['responses'])
                        print(f"ChatBot: {response}")
                        conversation_history.append(f"ChatBot: {response}")
                        response_found = True
                        break
                
                if response_found:
                    break
            
            # If no pattern matched, use default response
            if not response_found:
                response = random.choice(default_responses)
                print(f"ChatBot: {response}")
                conversation_history.append(f"ChatBot: {response}")
                
        except KeyboardInterrupt:
            print("\nChatBot: Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"ChatBot: Oops, something went wrong: {e}")

def get_response(user_input, responses, default_responses):
    """Get appropriate response for user input."""
    user_input_lower = user_input.lower()
    
    # Look for matching patterns
    for category, data in responses.items():
        for pattern in data['patterns']:
            if re.search(pattern, user_input_lower):
                return random.choice(data['responses'])
    
    # Return default response if no pattern matched
    return random.choice(default_responses)

if __name__ == "__main__":
    chatbot()