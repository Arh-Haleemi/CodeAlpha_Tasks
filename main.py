#!/usr/bin/env python3
"""
Python Learning Projects Collection
Four console applications demonstrating core programming concepts.
"""

from src.hangman import hangman_game
from src.portfolio_tracker import portfolio_tracker
from src.task_automation import task_automation_menu
from src.chatbot import chatbot

def display_menu():
    """Display the main menu."""
    print("=" * 50)
    print("    PYTHON CODEALPHA LEARNING PROJECTS COLLECTION")
    print("=" * 50)
    print("1. 🎮 Hangman Game")
    print("   - Guess words with limited tries")
    print("   - 5 predefined words, 6 incorrect guesses max")
    print()
    print("2. 📈 Stock Portfolio Tracker") 
    print("   - Track your stock investments")
    print("   - Hardcoded prices, CSV export option")
    print()
    print("3. 🤖 Task Automation Scripts")
    print("   - JPG file organizer")
    print("   - Email extractor from text files")
    print("   - Webpage title scraper")
    print()
    print("4. 💬 Basic Chatbot")
    print("   - Simple rule-based conversations")
    print("   - Responds to greetings and basic questions")
    print()
    print("5. 🚪 Exit")
    print("=" * 50)

def main():
    """Main application loop."""
    
    while True:
        try:
            display_menu()
            choice = input("Choose an application (1-5): ").strip()
            
            if choice == '1':
                print("\n🎮 Starting Hangman Game...\n")
                hangman_game()
                input("\nPress Enter to return to main menu...")
                
            elif choice == '2':
                print("\n📈 Starting Stock Portfolio Tracker...\n")
                portfolio_tracker()
                input("\nPress Enter to return to main menu...")
                
            elif choice == '3':
                print("\n🤖 Starting Task Automation Scripts...\n")
                task_automation_menu()
                input("\nPress Enter to return to main menu...")
                
            elif choice == '4':
                print("\n💬 Starting Basic Chatbot...\n")
                chatbot()
                input("\nPress Enter to return to main menu...")
                
            elif choice == '5':
                print("\n👋 Thanks for using Python Learning Projects!")
                print("Hope you enjoyed exploring these applications!")
                break
                
            else:
                print("\n❌ Invalid choice. Please enter a number between 1-5.")
                input("Press Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Exiting... Thanks for using Python Learning Projects!")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()