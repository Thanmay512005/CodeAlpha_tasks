def get_reply(message):
    """Return a reply based on the message entered by the user."""
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand. Try saying hello, how are you, or bye."


def main():
    print("Simple Chatbot")
    print("You can say: hello, how are you, or bye.")

    while True:
        user_message = input("You: ")
        reply = get_reply(user_message)
        print("Bot:", reply)

        if user_message.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()
