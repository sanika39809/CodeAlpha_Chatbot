print("===== Simple Chatbot =====")
print("Hello! I am your chatbot.")
print("You can talk to me. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hi!")
    
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")
    
    elif user_input == "what is your name":
        print("Bot: My name is CodeAlpha Bot.")
    
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break
    
    else:
        print("Bot: Sorry, I don't understand that.")