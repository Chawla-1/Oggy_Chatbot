import tkinter as tk
from tkinter import scrolledtext
import random

# Chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    
    if user_input in ["exit", "quit", "bye"]:
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing well! How about you?"
    elif "your name" in user_input:
        return "I’m a simple chatbot. What’s your name?"
    elif "weather" in user_input:
        return "I can't check the weather right now, but it's always a good idea to be prepared!"
    elif "help" in user_input:
        return "Sure, I can try to assist you. Please tell me more."
    else:
        responses = [
            "That's interesting!",
            "Could you tell me more?",
            "I'm not sure I understand, but I'm here to help!",
            "Let's talk more about that!"
        ]
        return random.choice(responses)

# Function to handle user input and chatbot response
def respond_to_user():
    user_input = user_entry.get().strip()
    if not user_input:
        return

    # Display user's message
    chatbox.configure(state="normal")
    chatbox.insert(tk.END, f"You: {user_input}\n")

    # Get chatbot's response
    response = get_response(user_input)
    chatbox.insert(tk.END, f"Chatbot: {response}\n")

    # Clear the entry box
    user_entry.delete(0, tk.END)

    # Close the application if the user says goodbye
    if user_input.lower() in ["exit", "quit", "bye"]:
        chatbox.insert(tk.END, "Chatbot: Closing the application...\n")
        chatbox.configure(state="disabled")
        root.after(2000, root.destroy)  # Close the app after 2 seconds
    else:
        chatbox.configure(state="disabled")
        chatbox.yview(tk.END)  # Scroll to the latest message

# GUI setup
def main():
    global root, chatbox, user_entry
    root = tk.Tk()
    root.title("Chatbot")

    # Chatbox for conversation display
    chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state="disabled")
    chatbox.pack(padx=10, pady=10)
    chatbox.configure(state="normal")
    chatbox.insert(tk.END, "Chatbot: Hi! I'm your chatbot. How can I help you today?\n")
    chatbox.configure(state="disabled")

    # Entry field for user input
    user_entry = tk.Entry(root, width=50)
    user_entry.pack(padx=10, pady=5)

    # Send button
    send_button = tk.Button(root, text="Send", command=respond_to_user)
    send_button.pack(pady=5)

    # Handle "Enter" key
    user_entry.bind("<Return>", lambda event: respond_to_user())

    # Run the GUI application
    root.mainloop()

if _name_ == "_main_":
    main()