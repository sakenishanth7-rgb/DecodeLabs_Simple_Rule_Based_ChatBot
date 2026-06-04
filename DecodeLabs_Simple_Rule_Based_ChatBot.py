"""
Project No.1

Simple Rule Based ChatBot

1.   Using Dictionary
2.   Infinite Loop Untill Exit..
3.   PreDefined Messages

"""

message_bank = {
    "hi": "Hello!",
    "hello": "Hello! How can I help you today?",
    "good morning": "Good Morning!",
    "good afternoon": "Good Afternoon!",
    "good evening": "Good Evening!",
    "who are you": "I am a Rule-Based AI Chatbot.",
    "what is your name": "I am a Chatbot.",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a nice day.",
    "exit": "Goodbye! Have a nice day.",
    "thanks": "You're welcome!",
    "how are you": "I'm doing great!",
    "help": "Try saying Hi, Hello, Who are you, Bye, etc."
}

print("AI ChatBot Started..")
while True:
    msg = input("User: ").strip().lower()

    if msg in ["bye", "exit"]:
        print("AI:", message_bank[msg])
        break

    elif msg in message_bank:
        print("AI:", message_bank[msg])

    else:
        print("AI: Sorry, I don't understand that.")

print("AI ChatBot Ended..!")

