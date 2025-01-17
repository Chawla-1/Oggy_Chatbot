import tkinter as tk
from tkinter import scrolledtext
import random
import re

# Chatbot logic
def get_response(user_input):
    user_input = user_input.lower()

    # Exit condition
    if user_input in ["exit", "quit", "bye"]:
        return "Goodbye! Have a great day!"

    # Check for various queries using regular expressions and keyword matching
    elif re.search(r"(timing|timings).*(parents|meet)", user_input, re.IGNORECASE):
        return "The timings for parents to meet are available on the official website. Please check there for specific hours."
    
    elif re.search(r"(committees|committees present).*(college)", user_input, re.IGNORECASE):
        return "The college has various committees, including the student council, promotion committee, cultural committee, and more. Do you want to know about a specific one?"
    
    elif "gym" in user_input:
        return "Yes, the college has a gym. It is open during regular hours and requires a student ID for access."
    
    elif re.search(r"(payment|methods).*(available)", user_input, re.IGNORECASE):
        return "The college accepts payments via credit/debit cards, UPI, and bank transfers for fees."
    
    elif re.search(r"(website|college website)", user_input, re.IGNORECASE):
        return "The official website of the college is www.college-website.com. Please visit it for more information."
    
    elif re.search(r"(dish|canteen).*(available)", user_input, re.IGNORECASE):
        return "The canteen offers a variety of dishes, including sandwiches, noodles, biryani, and more. Would you like to know the menu?"
    
    elif "average price of canteen dish" in user_input:
        return "The average price of a canteen dish is around ₹100 to ₹150."
    
    elif re.search(r"vadapao.*canteen", user_input, re.IGNORECASE):
        return "Yes, Vadapao is available in the canteen during lunch hours."
    
    elif re.search(r"(activities|events).*(college)", user_input, re.IGNORECASE):
        return "The college organizes various activities, such as cultural fests, workshops, sports events, and more."
    
    elif re.search(r"student head.*promotion committee", user_input, re.IGNORECASE):
        return "The current student head of the promotion committee is [Student Name]. You can contact them for any promotional queries."
    
    elif "fine for not wearing an ID card" in user_input:
        return "The fine for not wearing an ID card is ₹50 per day."
    
    elif re.search(r"food stalls.*outside college", user_input, re.IGNORECASE):
        return "There are several food stalls outside the college offering snacks, drinks, and fast food."

    # Generic responses
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing well! How about you?"
    
    elif "your name" in user_input:
        return "I'm a simple chatbot. What's your name?"
    
    elif "weather" in user_input:
        return "I can't check the weather right now, but it's always a good idea to be prepared!"
    
    elif "help" in user_input:
        return "Sure, I can try to assist you. Please tell me more."
    
    # Default response for unrecognized queries
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

if __name__ == "__main__":
    main()
