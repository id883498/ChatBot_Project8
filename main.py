from chatbot import ChatBot

bot = ChatBot()
print("ChatBot: Hello! Type 'bye' to end the conversation.")

while True:
    user_input = input("You: ")
    user_time = bot.timestamp()
    print(f"[{user_time}] You: {user_input}")
    
    response = bot.respond(user_input)
    bot_time = bot.timestamp()
    print(f"[{bot_time}] Bot: {response}")
    
    if user_input.lower().strip() == "bye":
        break
