from chatbot import ChatBot

if __name__ == "__main__":
    bot = ChatBot()
    print("ChatBot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = bot.respond(user_input)
        print("Bot:", response)
