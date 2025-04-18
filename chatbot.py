from datetime import datetime

class ChatBot:
    def __init__(self):
        self.responses = {
            "hi": "Hello!",
            "how are you": "I'm great, thanks for asking!",
            "bye": "Goodbye!"
        }

    def respond(self, message):
        message = message.lower().strip()
        return self.responses.get(message, "I don't understand that.")
    
    def timestamp(self):
        return datetime.now().strftime("%H:%M:%S")
