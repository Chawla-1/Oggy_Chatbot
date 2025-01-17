import tkinter as tk
from tkinter import scrolledtext
import http.client
import json

# RASA server details
RASA_SERVER_HOST = "localhost"
RASA_SERVER_PORT = 5005
RASA_SERVER_ENDPOINT = "/webhooks/rest/webhook"

# Function to send user input to RASA and get a response
def get_response_from_rasa(user_input):
    try:
        # Establish a connection to the RASA server
        conn = http.client.HTTPConnection(RASA_SERVER_HOST, RASA_SERVER_PORT)
        
        # Prepare the payload
        payload = json.dumps({
            "sender": "user",
            "message": user_input
        })
        
        # Send the POST request
        headers = {"Content-Type": "application/json"}
        conn.request("POST", RASA_SERVER_ENDPOINT, body=payload, headers=headers)
        
        # Get the response
        response = conn.getresponse()
        if response.status == 200:
            data = response.read().decode("utf-8")
            messages = json.loads(data)
            if messages:
                return " ".join([msg.get("text", "") for msg in messages])
            else:
                return "I'm sorry, I didn't understand that."
        else:
            return f"Error: Server responded with status code {response.status}."
    except Exception as e:
        return f"Error: Unable to connect to the RASA server. {e}"
    finally:
        conn.close()

# Function to handle user input and chatbot response
def respond_to_user():
    user_input = user_entry.get().strip()
    if not user_input:
        return

    # Display user's message
    chatbox.configure(state="normal")
    chatbox.insert(tk.END, f"You: {user_input}\n")

    # Get chatbot's response from RASA
    response = get_response_from_rasa(user_input)
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
    root.title("RASA Chatbot")

    # Chatbox for conversation display
    chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state="disabled")
    chatbox.pack(padx=10, pady=10)
    chatbox.configure(state="normal")
    chatbox.insert(tk.END, "Chatbot: Hi! I'm your RASA chatbot. How can I help you today?\n")
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
