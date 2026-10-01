import random

def play_hangman():
    # 1. Predefined list of 5 words (Lists)
    word_list = ["PYTHON", "ALGORITHM", "VARIABLE", "FUNCTION", "SYNTAX"]
    
    # Select a random word (random)
    secret_word = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6
    
    print("Welcome to Hangman!")
    print("Try to guess the secret word one letter at a time.")
    
    # Main game loop (while loop)
    while incorrect_guesses < max_guesses:
        # Display the current state of the word (Strings and for loops)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print(f"\nWord to guess: {display_word}")
        print(f"Incorrect guesses remaining: {max_guesses - incorrect_guesses}")
        
        # Check if the player has won
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly!")
            break
            
        # Get player input
        guess = input("Guess a letter: ").upper()
        
        # Basic input validation (if-else)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
            
        # Add valid guess to our list
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect!")
            incorrect_guesses += 1
            
    # Check for loss condition
    if incorrect_guesses == max_guesses:
        print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()