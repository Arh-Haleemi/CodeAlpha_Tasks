# Hangman Game in Python
# Author : Abdulrahman Haleemi
# Assigment : Hangman Game from CodeAlpha


import random

def hangman_game():
    words = ["python", "hangman", "programing", "computer", "Challenge", "Gaming"]
    # Choose a random word from the list
    word = random.choice(words).lower()
    word_length = len(word)

    # Initialize variables
    guessed_letters = []
    max_incorrect = 6
    incorrect_guesses = 0

    # Get player name
    name = input("Enter your name:")
    print("Hello", name)

    # Create word display for the all words
    word_display = []
    for word in words:
        word_display.append(["_"] * len(word))

    completed_words = []

    print("There are 5 words in the list!")
    print("Words to guess:")
    for i, word in enumerate(words):
        print(f"{i+1}. {' '.join(['_'] * len(word))} ({len(word)} letters)")
    print()
    
    print("Welcome to Hangman Game!")
    print("You have 6 incorrect guesses before the game is over.")
    print("Tpye 'exit' anytime to quit the game.")
    print()
    

    # Game loop
    while incorrect_guesses < max_incorrect and len(completed_words) < len(words):
        # Display current state of all words
        print("Current progress:")
        for i, (word, display) in enumerate(zip(words, word_display)):
            if i in completed_words:
                print(f"{i+1}. {word.upper()} ✅ COMPLETED!")
            else:
                print(f"{i+1}. {' '.join(display)} ({len(word)} letters)")

        print(f"\nGuessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Completed words: {len(completed_words)}/{len(words)}")
        print()

        # Check if all words are complete
        if len(completed_words) == len(words):
            print()
            print("🎉" * 30)
            print(f"AMAZING {name.upper()}! YOU COMPLETED ALL WORDS!")
            print("🎉" * 30)
            print()
            break

        # Get player input
        try:
            guess = input("Enter a letter (or 'exit' to quit): ").lower().strip()
        except EOFError:
            print("Input is not supported in this environment. Please run this script in a terminal that supports input().")
            return
            
        # Check for exit command
        if guess == 'exit':
            print(f"Thanks for playing, {name}! Goodbye!")
            return

        # Validate input
        if guess in guessed_letters:
            print("You already guessed that letter.")
            print()
            continue

        # Add guess to list
        guessed_letters.append(guess)
        
        # Check if guess is correct in any word
        found_in_words = []
        newly_completed = []

        for i, word in enumerate(words):
            if i not in completed_words and guess in word:
                found_in_words.append(word)

                # Update word display for this word
                for j, letter in enumerate(word):
                    if letter == guess:
                        word_display[i][j] = guess
                        
                # Check if this word is now complete
                if "_" not in word_display[i]:
                    completed_words.append(i)
                    newly_completed.append(word)

        # Provide feedback
        if found_in_words:
            # Show which word numbers contain the letter
            word_numbers = []
            for word in found_in_words:
                word_numbers.append(str(words.index(word) + 1))
            print(f"Great! '{guess}' is found in word(s): {', '.join(word_numbers)}")

            # Congratulate for newly completed words
            for word in newly_completed:
                print()
                print("🎉" * 15)
                print(f"CONGRATULATIONS! You completed: {word.upper()}")
                print("🎉" * 15)
        else:
            print(f"Sorry, '{guess}' is not in any remaining words.")
            incorrect_guesses += 1

        print()

    # Check if game was lost
    if incorrect_guesses >= max_incorrect:
        print("Game Over! You ran out of guesses.")
        print("The words were:")
        for word in words:
            print(f"  - {word.upper()}")

    print(f"\nThanks for playing, {name}!")
    print("Goodbye!")
    
if __name__ == "__main__":
    hangman_game()
    # End of the game
