# chatbot.py
# Team Project: Python AI Chatbot Prototype
# A small experiment in humor and human-like conversation

import random

def chatbot_response(user_input):
    responses = [
        "Why did the AI go to school? To improve its 'byte'-sized knowledge!",
        "I'm not entirely sure, but let's figure it out together!",
        "Do you have anything else to ask me? What else would you like to know?",
        "Humor and AI are a strange combo, but here we are!",
        "Sometimes I think in code, sometimes I just try to make you smile."
    ]
    return responses[hash(user_input) % len(responses)]

def main():
    print("Welcome to our team AI Chatbot! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Keep exploring AI with humor.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    main()
