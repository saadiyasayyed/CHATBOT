import tkinter as tk
from tkinter import scrolledtext
import random

# Define a simple Q&A dictionary for the chatbot
qa_pairs = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi! How can I help you?",
    "how are you?": "I am fine, how are you?",  # Custom response for "how are you?"
    "what is your name?": "I am a chatbot created in Python!",
    "what is your purpose?": "I am here to answer your questions.",
    "what is your favorite color?": "I don't have a favorite color, but I think blue is nice!",
    "how old are you?": "I don't age, but I'm always here to assist you!",
    "what can you do?": "I can answer questions, provide information, and assist with simple tasks.",
    "who created you?": "I was created by a team of developers using Python and Tkinter.",
    "can you help me with coding?": "Yes, I can assist with coding questions! Just let me know what you're working on.",
    "what is 2+2?": "2 + 2 equals 4.",
    "what is Python?": "Python is a high-level programming language known for its simplicity and readability. It's great for beginners and experts alike.",
    "how do I install Python?": "You can download Python from the official website at https://www.python.org/downloads/.",
    "how do I make a GUI in Python?": "You can use the Tkinter library to create GUI applications in Python. Let me know if you need help with that!",
    "what is the capital of France?": "The capital of France is Paris.",
    "what is the largest planet in our solar system?": "The largest planet is Jupiter.",
    "can you speak?": "I can't speak, but I can type responses. You can use text-to-speech tools to hear me speak!",
    "what is the weather today?": "Sorry, I can't check the current weather. You can use a weather app or website like Weather.com for the latest updates.",
    "bye": "Goodbye! It was nice talking to you. Have a nice day!",
    "thank you": "You're welcome!"
}

# Define a list of questions for the chatbot to ask
#follow_up_questions = [
    #"What are your hobbies?",
    #"Do you like coding?",
    #"Have you traveled anywhere recently?",
    #"What kind of music do you enjoy?",
    #"Do you prefer reading books or watching movies?"
#]

# Function to get the response from the chatbot
def get_response():
    user_input = user_input_box.get().lower()  # Get user input and convert to lowercase
    response = qa_pairs.get(user_input, "Sorry, I didn't understand that.")
    
    # Insert the user input and bot response into the chat area
    chat_area.config(state=tk.NORMAL)  # Enable text area to modify it
    chat_area.insert(tk.END, "You: " + user_input + '\n')  # User's message
    chat_area.insert(tk.END, "Bot: " + response + '\n')  # Bot's response
    chat_area.yview(tk.END)  # Scroll to the bottom
    chat_area.config(state=tk.DISABLED)  # Disable editing the chat area
    
    user_input_box.delete(0, tk.END)  # Clear the user input box after submission

    # After responding, the bot will ask a follow-up question
    if user_input == "how are you?":
        follow_up = "How are you?"
    else:
        follow_up = random.choice(follow_up_questions)  # Randomly pick a follow-up question

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "Bot: " + follow_up + '\n')  # Bot asks a question
    chat_area.yview(tk.END)
    chat_area.config(state=tk.DISABLED)  # Disable editing the chat area

# Set up the Tkinter window
root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("400x500")

# Create a scrolled text area for displaying the chat conversation
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=20, width=45)
chat_area.pack(padx=10, pady=10)

# Create a text entry box for user input
user_input_box = tk.Entry(root, width=40)
user_input_box.pack(padx=10, pady=10)

# Create a button to trigger the chatbot response
send_button = tk.Button(root, text="Send", command=get_response)
send_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
