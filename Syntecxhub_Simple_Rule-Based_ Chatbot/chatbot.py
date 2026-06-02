import datetime

# Conversation history file
history_file = "chat_history.txt"

print("=" * 50)
print("Simple Rule-Based Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

# Knowledge Base
knowledge_base = {
    "what is ai": "AI stands for Artificial Intelligence, enabling machines to mimic human intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI where systems learn from data.",
    "what is python": "Python is a high-level programming language used in AI, Web Development, and more.",
    "what is data science": "Data Science is the process of extracting insights from data."
}

# Function to log conversations
def log_conversation(user, bot):
    with open(history_file, "a") as file:
        timestamp = datetime.datetime.now()
        file.write(f"[{timestamp}]\n")
        file.write(f"You: {user}\n")
        file.write(f"Bot: {bot}\n\n")

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye!")
        log_conversation(user_input, "Goodbye!")
        break

    # Greeting Intent
    elif user_input in ["hi", "hello", "hey"]:
        response = "Hello! How can I help you today?"

    # Help Intent
    elif user_input == "help":
        response = """I can:
1. Greet you
2. Answer AI-related questions
3. Chat with you
4. Log conversation history"""

    # Small Talk
    elif "how are you" in user_input:
        response = "I'm doing great! Thanks for asking."

    elif "your name" in user_input:
        response = "I am a Rule-Based Chatbot."

    elif "thank you" in user_input:
        response = "You're welcome!"

    # Knowledge Base
    elif user_input in knowledge_base:
        response = knowledge_base[user_input]

    else:
        response = "Sorry, I don't understand that question."

    print("Bot:", response)

    log_conversation(user_input, response)