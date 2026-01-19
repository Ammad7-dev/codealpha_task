def simple_chatbot():
    # Predefined rules/responses
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! Hope you're having a great day.",
        "how are you": "I'm just a Python script, but I'm functioning perfectly! How about you?",
        "what is your name": "I am the CodeAlpha Basic Chatbot.",
        "bye": "Goodbye! Have a wonderful day ahead!",
        "thanks": "You're very welcome!",
    }

    print("--- Chatbot Initialized (Type 'bye' to exit) ---")

    while True:
        # Get user input and normalize it (lowercase)
        user_input = input("You: ").lower().strip()

        # Exit condition
        if user_input == "bye":
            print(f"Bot: {responses['bye']}")
            break

        # Check for matches in our dictionary
        found_response = False
        for key in responses:
            if key in user_input:
                print(f"Bot: {responses[key]}")
                found_response = True
                break
        
        # Default response if no keyword is found
        if not found_response:
            print("Bot: I'm sorry, I don't understand that yet. Could you try asking something else?")

if __name__ == "__main__":
    simple_chatbot()