import tkinter as tk
from tkinter import scrolledtext
import time


FAQ_DATABASE = {
    "weather": "The weather today is sunny with a chance of clouds.",
    "name": "I'm a simple rule-based chatbot. What's your name?",
    "time": f"The current time is {time.strftime('%H:%M:%S')}.",
    "help": "I'm here to answer basic questions. Try asking about weather, my name, or time!",
    "how are you": "I'm just a bunch of code, so I'm always feeling functional!",
    "favorite movie": "I don’t watch movies, but I've heard 'The Matrix' is great!",
    "think about humans": "Humans are fascinating beings. You created me, after all!",
    "friends": "Of course! I’d love to be friends with you.",
    "tired": "I never get tired. I'm powered by your curiosity!",
    "joke": "Why don't programmers like nature? Too many bugs!",
    "meaning of life": "42. At least, that's what I've been told.",
    "birthday": "I don't have a birthday, but you can celebrate me every day!",
    "sing": "La la la! I'm better at chatting than singing.",
    "favorite color": "I like the color of code: green and black!",
    "recommend book": "How about 'Python Crash Course' by Eric Matthes?",
    "secret to happiness": "Happiness is finding joy in small moments and asking me fun questions!",
    "aliens": "I haven’t met any aliens yet, but I’d love to chat with one someday.",
    "fun fact": "Did you know honey never spoils? Archaeologists found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
    "travel": "If I could travel, I’d visit all the computer servers in the world!",
    "asdfghjkl": "That looks like you hit random keys. Is everything okay?",
    "what if": "I might not understand everything, but I’m always here to try!",
    "exit exit exit": "I get it, you want to exit! Type 'exit' to close the chat.",
    "hello": "Hello! How can I assist you today?",
    "1234567890": "That’s a number, but I’m not sure what it means!"
}


LOG_FILE = "chatbot_log.txt"


def log_conversation(user_input, bot_response):
    with open(LOG_FILE, "a") as file:
        file.write(f"User: {user_input}\nChatbot: {bot_response}\n\n")

def get_response(user_input):
    user_input = user_input.strip().lower()
    if "exit" in user_input:
        return "Goodbye! Have a great day!"
    for key in FAQ_DATABASE.keys():
        if key in user_input:
            return FAQ_DATABASE[key]
    return "Sorry, I don't understand that. Can you try asking something else?"

def handle_input():
    user_input = input_field.get().strip()
    if not user_input:
        return
    chat_window.insert(tk.END, f"You: {user_input}\n", "user")
    input_field.delete(0, tk.END)

    
    response = get_response(user_input)
    chat_window.insert(tk.END, f"Chatbot: {response}\n\n", "bot")
    chat_window.see(tk.END)  

    
    log_conversation(user_input, response)

    if "exit" in user_input:
        root.quit()

root = tk.Tk()
root.title("Rule-Based Chatbot")
root.geometry("600x700")
root.configure(bg="#f7f7f7") 


chat_window = scrolledtext.ScrolledText(
    root, 
    wrap=tk.WORD, 
    state="normal", 
    font=("Helvetica", 12), 
    bg="#f4f4f4", 
    fg="#333333", 
    padx=10, 
    pady=10
)
chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

chat_window.tag_config("user", foreground="#0055FF", font=("Helvetica", 12, "bold"))
chat_window.tag_config("bot", foreground="#FF5733", font=("Helvetica", 12))


input_frame = tk.Frame(root, bg="#f7f7f7")
input_frame.pack(fill=tk.X, padx=10, pady=5)

input_field = tk.Entry(
    input_frame, 
    font=("Helvetica", 14), 
    bg="#ffffff", 
    fg="#333333", 
    relief=tk.GROOVE
)
input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
input_field.bind("<Return>", lambda event: handle_input())

send_button = tk.Button(
    input_frame, 
    text="Send", 
    command=handle_input, 
    font=("Helvetica", 12), 
    bg="#4CAF50", 
    fg="#ffffff", 
    activebackground="#45a049", 
    relief=tk.RAISED, 
    padx=10, 
    pady=5
)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

header = tk.Label(
    root, 
    text="Welcome to Rule-Based Chatbot", 
    font=("Helvetica", 16, "bold"), 
    bg="#333333", 
    fg="#ffffff", 
    pady=10
)
header.pack(fill=tk.X)


chat_window.insert(tk.END, "Chatbot: Welcome to the Chatbot! Type 'exit' to end the chat.\n\n", "bot")

root.mainloop()
