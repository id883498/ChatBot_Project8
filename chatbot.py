class ChatBot:
    def __init__(self):
        self.responses = {
            "hi": "Hello!",
            "how are you": "I'm just a bunch of code, but I'm great!",
            "bye": "Goodbye!"
        }

    def respond(self, message):
        message = message.lower().strip()
        return self.responses.get(message, "Sorry, I didn't get that.")
