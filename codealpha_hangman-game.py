import random

def hangman():
    # 1. Predefined list of words
    words = ["python", "coding", "intern", "logic", "script"]
    secret_word = random.choice(words).lower()
    
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("--- Welcome to Hangman! ---")

    # 2. Game Loop
    while incorrect_guesses < max_attempts:
        # Display the current status of the word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")

        # Check if the player has won
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            break

        # 3. Handle User Input
        guess = input("Guess a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        # 4. Check Guess
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not there.")

    # 5. End of Game
    if incorrect_guesses == max_attempts:
        print("\nGame Over!")
        print(f"The word was: {secret_word}")

if __name__ == "__main__":
    hangman()