def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing well, thank you for asking. How about you?"

    elif "your name" in user_input:
        return "I'm a simple Python chatbot created for an automation project."

    elif "help" in user_input:
        return "I can respond to greetings, answer basic questions, and have a simple conversation."

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Happy to help."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I don't understand that yet. Please try a different question."


def chatbot():
    print("=" * 50)
    print("        Welcome to Basic Python Chatbot")
    print("Type 'bye' to end the conversation")
    print("=" * 50)

    while True:
        user_message = input("\nYou: ")

        response = get_response(user_message)
        print("Bot:", response)

        if user_message.lower().strip() in ["bye", "goodbye"]:
            break


# Start chatbot
chatbot()