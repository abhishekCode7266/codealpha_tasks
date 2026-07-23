# Hangman Game

A simple console-based Hangman game written in Python.

## Overview

This is a small implementation of the classic Hangman game. The program selects a random word from a predefined list and asks the player to guess it one letter at a time. The player has 6 incorrect guesses (lives) before the game ends.

## Requirements

- Python 3.6+ (Python 3 recommended)

## Files

- `hangman Game.py` — The main Python script that runs the game.

> Note: The file name contains a space. To run it from a terminal, you may need to quote the filename (see examples below) or rename it to `hangman_game.py`.

## How to run

1. Open a terminal or command prompt.
2. Change directory to the Hangman game folder:

   cd "CodeAlpha_Tasks_python project/CodeAlpha_Hangman Game"

3. Run the script:

   python "hangman Game.py"

   or, if your system uses `python3` for Python 3:

   python3 "hangman Game.py"

If you rename the script to `hangman_game.py`, you can run it without quotes:

   python hangman_game.py

## How to play

- The program will display a series of underscores representing the letters of the secret word.
- Type a single letter and press Enter to make a guess.
- Correct letters are revealed in their positions. Incorrect guesses reduce your remaining lives.
- You have 6 incorrect guesses. The game ends when you either guess all letters correctly or run out of lives.

## Customization

- To add or change words, edit the `words` list in `hangman Game.py`.
- To change the number of allowed incorrect guesses, modify the `lives` variable (and ensure the `hangman_stages` list has a matching number of stages).

## Example

When you run the game you'll see the hangman ASCII art, the current word with underscores, guessed letters, and remaining lives. Keep guessing letters until you win or lose.

## License & Attribution

Created by abhishekCode7266 as part of the CodeAlpha tasks collection.

No explicit license is included in the repository; add one if you want to make reuse terms clear.
