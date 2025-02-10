def chatbot():
    print("Chatbot: Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I assist you?")
        elif "your name" in user_input:
            print("Chatbot: I am a simple chatbot.")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected!")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()