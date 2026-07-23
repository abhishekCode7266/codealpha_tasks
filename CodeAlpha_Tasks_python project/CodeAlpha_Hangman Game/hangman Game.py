import random

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# List of predefined words
words = ["apple", "tiger", "house", "python", "garden"]

# Select a random word
secret_word = random.choice(words)

# Display word with underscores
display_word = ["_"] * len(secret_word)

# Store guessed letters
guessed_letters = []

# Number of lives
lives = 6

print("=" * 40)
print("        HANGMAN GAME")
print("=" * 40)
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while lives > 0 and "_" in display_word:

    print(hangman_stages[6 - lives])
    print("Word: ", " ".join(display_word))
    print("Guessed Letters:", " ".join(guessed_letters))
    print("Lives Left:", lives)

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check duplicate guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        print("Correct Guess!\n")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    # Wrong guess
    else:
        lives -= 1
        print("Wrong Guess!\n")

# Final result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print(hangman_stages[6])
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")