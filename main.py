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
    elif re.search(r"(UGC|recognition).*(status|approved)", user_input, re.IGNORECASE): 
        return "Bennett University programs are recognized by UGC. The university ensures that all programs are approved by relevant authorities."

    elif re.search(r"when.*Bennett University.*established", user_input, re.IGNORECASE): 
        return "Bennett University was established in 2016."

    elif re.search(r"(degrees|programs).*(recognized|nationally|internationally)", user_input, re.IGNORECASE): 
        return "Bennett University degrees are recognized both nationally and internationally."

    elif re.search(r"(application form|fee)", user_input, re.IGNORECASE): 
        return "The application form fee for Bennett University can be found on the official website. Please check there for more details."

    elif re.search(r"(real-time|interactive).*(sessions|programs)", user_input, re.IGNORECASE): 
        return "Yes, the university conducts real-time interactive sessions about the programs."

    elif re.search(r"can.*withdraw.*admission", user_input, re.IGNORECASE): 
        return "Once your admission is confirmed, you can withdraw, but please refer to the official guidelines for specific withdrawal procedures."

    elif re.search(r"whom.*contact.*admission", user_input, re.IGNORECASE): 
        return "You can contact the admissions office for any queries related to admission."

    elif re.search(r"regional.*offices.*admission", user_input, re.IGNORECASE): 
        return "Yes, Bennett University has regional offices for admission-related information, which help aspirants from other states."

    elif re.search(r"schools.*at Bennett University", user_input, re.IGNORECASE): 
        return "Bennett University has several schools, including the School of Engineering, School of Management, and School of Law."

    elif re.search(r"multidisciplinary.*university", user_input, re.IGNORECASE): 
        return "Yes, Bennett University is a multidisciplinary university offering diverse programs across various fields."

    elif re.search(r"undergraduate programs.*Bennett University", user_input, re.IGNORECASE): 
        return "Bennett University offers various undergraduate programs, including B.Tech, BBA, and more."

    elif re.search(r"postgraduate.*Ph.D.*programs", user_input, re.IGNORECASE): 
        return "The university offers a range of postgraduate and Ph.D. programs. For details, please refer to the official website."

    elif re.search(r"support.*Ph.D.*students", user_input, re.IGNORECASE): 
        return "Bennett University offers comprehensive support for Ph.D. students, including research guidance and infrastructure."

    elif re.search(r"unique.*curricula.*University", user_input, re.IGNORECASE): 
        return "The university follows a unique, industry-oriented curriculum designed to meet global standards."

    elif re.search(r"distinguishes.*teaching faculty", user_input, re.IGNORECASE): 
        return "Bennett University faculty members are highly experienced and qualified, many of them have industry expertise."

    elif re.search(r"industry.*support.*programs", user_input, re.IGNORECASE): 
        return "Bennett University ensures industry support for its programs through collaborations, internships, and guest lectures."

    elif re.search(r"study facilities.*support.*infra", user_input, re.IGNORECASE): 
        return "The university offers excellent study facilities, including modern classrooms, libraries, and dedicated research spaces."

    elif re.search(r"placement.*internship.*opportunities", user_input, re.IGNORECASE): 
        return "Yes, Bennett University offers placement and internship opportunities to students in collaboration with industry partners."

    elif re.search(r"entrepreneurs.*innovators.*opportunities", user_input, re.IGNORECASE): 
        return "Bennett University offers a variety of opportunities for aspiring entrepreneurs and student innovators, including incubation support."

    elif re.search(r"fee structure.*Bennett University", user_input, re.IGNORECASE): 
        return "The fee structure for students enrolled in programs at Bennett University can be found on the official website."

    elif re.search(r"online fee payment portal", user_input, re.IGNORECASE): 
        return "Yes, Bennett University has an online fee payment portal available for students."

    elif re.search(r"bank loan.*Bennett University", user_input, re.IGNORECASE): 
        return "Yes, students aspiring to study at Bennett University can avail a bank loan through the university’s tie-ups with financial institutions."

    elif re.search(r"scholarships.*deserving students", user_input, re.IGNORECASE): 
        return "Yes, deserving students are eligible for scholarships. Details can be found on the university website."

    elif re.search(r"commute.*day scholars.*Bennett University", user_input, re.IGNORECASE): 
        return "Day scholars typically commute via public transport, carpooling, or personal vehicles. The university provides some assistance in this regard."

    elif re.search(r"anti-ragging.*sexual harassment.*measures", user_input, re.IGNORECASE): 
        return "Yes, Bennett University has strict anti-ragging and sexual harassment measures in place on campus."

    elif re.search(r"popular student events.*campus", user_input, re.IGNORECASE): 
        return "The university organizes a variety of student events including cultural festivals, fests, and academic conferences."

    elif re.search(r"hostel rooms.*living facilities", user_input, re.IGNORECASE): 
        return "Bennett University offers comfortable hostel rooms with various living facilities, including Wi-Fi and mess services."

    elif re.search(r"free Wi-Fi", user_input, re.IGNORECASE): 
        return "Yes, free Wi-Fi is available across the campus, including hostels and study areas."

    elif re.search(r"canteen.*food", user_input, re.IGNORECASE): 
        return "The university cafeteria serves a variety of food, including Indian and continental dishes."

    elif re.search(r"sports.*facility.*campus", user_input, re.IGNORECASE): 
        return "Bennett University has excellent sports facilities, including indoor and outdoor courts, a gym, and more."

    elif re.search(r"hospital.*on campus", user_input, re.IGNORECASE): 
        return "Yes, there is a health center on campus to provide medical assistance to students."

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
