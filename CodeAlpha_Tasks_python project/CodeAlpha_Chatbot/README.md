# Friendly Chatbot

A simple command-line chatbot written in Python. This is a minimal example showing how to interact with a user via the console using basic keyword-based responses.

## File

`basic chatbot.py`

## Description

This chatbot responds to a few predefined user inputs (like "hello", "how are you", "what is your name", "good morning", "good evening", "thank you", and "bye"). Any other input will return a default message indicating the bot doesn't understand.

It's intended as a beginner-friendly example to demonstrate basic input/output and control flow in Python.

## Features

- Console-based interaction
- Simple keyword matching
- Graceful exit with `bye`

## Requirements

- Python 3.6 or newer

## How to run

1. Open a terminal and navigate to the folder containing `basic chatbot.py`.
2. Run the script:

```bash
python "basic chatbot.py"
```

Note: The filename contains a space. Either wrap the filename in quotes as shown above or rename the file to remove spaces (recommended: `basic_chatbot.py`).

## Example session

```
========================================
      Welcome to Friendly Chatbot
Type 'bye' to end the chat.
========================================
You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: what is your name
Bot: My name is Friendly ChatBot.
You: bye
Bot: Goodbye!
```

## Suggested improvements

- Use a dictionary to map inputs to responses to simplify the code.
- Add fuzzy matching or synonyms (e.g., using `in` checks or `difflib.get_close_matches`) to accept variations like "hi", "hey", or "good morning!" with punctuation.
- Refactor into functions or a class for easier extension and testing.
- Remove spaces from the filename and add argument parsing so the script can be run more flexibly.

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project has no license specified. Add a LICENSE file if you want to make the usage terms explicit.
