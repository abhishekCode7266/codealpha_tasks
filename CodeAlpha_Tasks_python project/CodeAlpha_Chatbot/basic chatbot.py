def chatbot():
    print("=" * 40)
    print("      Welcome to Friendly Chatbot")
    print("Type 'bye' to end the chat.")
    print("=" * 40)

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is Friendly ChatBot.")

        elif user == "good morning":
            print("Bot: Good morning! Have a great day!")

        elif user == "good evening":
            print("Bot: Good evening!")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()