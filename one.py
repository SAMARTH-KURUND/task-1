import random

# List of words to choose from
word_list = ['python', 'hangman', 'developer', 'programming', 'computer', 'algorithm', 'variable', 'function', 'loop', 'condition']

# Function to select a random word
def get_random_word():
    return random.choice(word_list)

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# Function to play the Hangman game
def play_hangman():
    word = get_random_word()  # Select a random word from the list
    guessed_letters = []  # List to keep track of guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect_guesses = 6  # Maximum incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: ", display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        # Check if the player has guessed all letters correctly
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break

    # If the loop ends because the player has used up all their guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nSorry, you've run out of guesses. The word was '{word}'. Better luck next time!")

# Start the game
if __name__ == "__main__":
    play_hangman()
