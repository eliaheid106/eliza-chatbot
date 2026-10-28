
# eliza-chatbot
import random

PHRASEN = [
    "Can you explain the problem to me in more detail?",
    "Tell me more about it.",
    "Why is this important to you?",
    "Okay, I'll help you.",
    "Tell me more about it so I can get a better sense of your problem.",
    "It's definitely not as bad as it looks.",
    "You can do it!",
    "Is it really as bad as you imagine?"
]

print("Eliza: Hi, I'm Eliza! Let's talk about something.")

user_input = "x"

while user_input != "":
    user_input = input("You: ").lower()

    if "hate" in user_input:
        print("Eliza: Hate can destroy what is valuable.")

    elif "love" in user_input:
        print("Eliza: Love is wonderful.")

    elif "sleep" in user_input:
        print("Eliza: Sleep is important—whether you're studying, playing sports, or doing other activities. Be sure to set aside at least 6 hours for it.")

    elif "hello" in user_input:
        print("Eliza: Hi, how are you?")

    elif "hi" in user_input:
        print("Eliza: Hello, whats up?")

    elif "how" in user_input:
        print("Eliza: I'm Eliza, your AI assistant!")

    elif user_input != "":
        text = random.choice(PHRASEN)
        print("Eliza:", text)

print("Eliza: It was nice chatting with you—see you next time!")
