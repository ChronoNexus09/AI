import random

BOT_NAME = "Nova"

def get_chatbot_response(user_message):
    message_lower = user_message.lower()

    responses = {
        "greetings": ["Hello! How can I help you today?", "Hi! What’s on your mind?", "Hey! Need assistance?"],
        "how_are_you": ["I'm doing great! How about you?", "I'm fantastic! What can I do for you today?", "All systems go! How's your day?"],
        "help": ["I'm here to assist! Ask me anything.", "I can help with questions, discussions, or brainstorming!", "Need assistance? Let me know."],
        "programming": ["Python is amazing! What are you working on?", "Coding is fun! What's your project?", "Software development is exciting! Tell me more."],
        "thanks": ["You're welcome!", "Glad I could help!", "Anytime!"],
        "goodbye": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
    }

    for category, options in responses.items():
        if any(word in message_lower for word in category.split("_")):
            return f"{BOT_NAME}: {random.choice(options)}"

    return f"{BOT_NAME}: That's interesting! Tell me more."
