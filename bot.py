import json

# Load FAQs
try:
    with open('data/faqs.json', 'r', encoding='utf-8') as f:
        FAQS = json.load(f)
except:
    FAQS = []

def get_answer(user_msg):
    user_msg = user_msg.lower()
    for item in FAQS:
        for keyword in item["keywords"]:
            if keyword in user_msg:
                return item["answer"]
    return "Thanks for asking! Our support team will contact you soon."

def chat():
    print("🛒 E-commerce Chatbot (type 'exit' to quit)")
    while True:
        msg = input("You: ")
        if msg.lower() in ["exit", "quit", "bye"]:
            print("Bot: Thank you for visiting! 👋")
            break
        print(f"Bot: {get_answer(msg)}")

if __name__ == "__main__":
    chat()
