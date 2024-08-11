import re
from datetime import datetime


def chatbot_response(user_input):
    user_input = user_input.lower()
    if re.search(r'\b(hello|hi|hey)\b', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'who\s+are\s+you', user_input):
        return "I am an advanced rule-based chatbot created to assist you with various queries."
    elif re.search(r'\b(what\s+is\s+your\s+name|your\s+name|who\s+are\s+you)\b', user_input):
        return "I don't have a specific name, but you can call me ChatBot."
    elif re.search(r'\b(what\s+can\s+you\s+do|your\s+abilities|what\s+do\s+you\s+do)\b', user_input):
        return "I can assist you with general queries, provide information, and help you with simple tasks. Just ask!"
    elif re.search(r'\b(help|assist)\b', user_input):
        return "Sure! I can help you with general queries. Please ask me anything."
    elif re.search(r'\b(time)\b', user_input):
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    elif re.search(r'\b(weather|forecast)\b', user_input):
        return "I can't check the weather, but it looks like a good day to learn coding!"
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r'\b(tell\s+me\s+a\s+joke|joke)\b', user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif re.search(r'\b(date)\b', user_input):
        today = datetime.today().strftime('%Y-%m-%d')
        return f"Today's date is {today}."
    else:
        return "I'm sorry, I don't fully understand that. Can you please clarify?"

def chat():
    print("Chatbot: Hello! I am an advanced rule-based chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print(f"Chatbot: {chatbot_response(user_input)}")


if __name__ == "__main__":
        chat()
