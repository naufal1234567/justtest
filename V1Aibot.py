import random
import pickle
import datetime
import tkinter as tk

greetings = ["Hello!", "What's up?!", "Howdy!", "Greetings!"]
goodbyes = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]

keywords = ["music", "pet", "book", "game"]
responses = ["Music is so relaxing!", "Dogs are man's best friend!", "I know about a lot of books.", "I like to play video games."]

try:
    # Load existing data
    with open('keywords.pkl', 'rb') as f:
        keywords = pickle.load(f)
    with open('responses.pkl', 'rb') as f:
        responses = pickle.load(f)
except FileNotFoundError:
    # If data doesn't exist, create new data
    pass

# Function to respond to user input
def respond_to_user():
    global keywords
    global responses
    
    user_input = input_entry.get().lower()
    input_entry.delete(0, tk.END)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    
    keywords_found = False
    for index in range(len(keywords)):
        if(keywords[index] in user_input):
            nakama_response = "Nakama: " + responses[index] + "\n"
            chat_log.insert(tk.END, nakama_response)
            keywords_found = True
    if(keywords_found == False):
        if "time" in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            chat_log.insert(tk.END, "Nakama: The current time is " + current_time + ".\n")
        elif "date" in user_input:
            current_date = datetime.datetime.now().strftime("%m/%d/%Y")
            chat_log.insert(tk.END, "Nakama: Today's date is " + current_date + ".\n")
        else:
            chat_log.insert(tk.END, "Nakama: I don't know what to say to that. But I'll remember that for next time.\n")
    
def add_new_response():
    global keywords
    global responses
    
    new_keyword = new_keyword_entry.get().lower()
    new_response = new_response_entry.get().lower()
    new_response_entry.delete(0, tk.END)
    new_keyword_entry.delete(0, tk.END)
        
    keywords.append(new_keyword)
    responses.append(new_response)
        
    # Save new data
    with open('keywords.pkl', 'wb') as f:
        pickle.dump(keywords, f)
    with open('responses.pkl', 'wb') as f:
        pickle.dump(responses, f)
            
    chat_log.insert(tk.END, "Nakama: Thanks for teaching me something new!\n")

# Create GUI window
root = tk.Tk()
root.title("Nakama Chat")

# Create chat log and input field
chat_log = tk.Text(root)
chat_log.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

input_frame = tk.Frame(root)
input_frame.pack(side=tk.BOTTOM, fill=tk.X)

input_entry = tk.Entry(input_frame)
input_entry.pack(side=tk.LEFT, fill=tk.X, expand=1)
input_entry.bind("<Return>", (lambda event: respond_to_user()))

send_button = tk.Button(input_frame, text="Send", command=respond_to_user)
send_button.pack(side=tk.RIGHT)

# Create frame for adding new keyword and response
new_response_frame = tk.Frame
new_response_label = tk.Label(root, text="Teach me something new!")
new_response_label.pack()

new_response_entry_frame = tk.Frame(root)
new_response_entry_frame.pack()

new_keyword_label = tk.Label(new_response_entry_frame, text="Keyword:")
new_keyword_label.pack(side=tk.LEFT)

new_keyword_entry = tk.Entry(new_response_entry_frame)
new_keyword_entry.pack(side=tk.LEFT)

new_response_label = tk.Label(new_response_entry_frame, text="Response:")
new_response_label.pack(side=tk.LEFT)

new_response_entry = tk.Entry(new_response_entry_frame)
new_response_entry.pack(side=tk.LEFT)

add_response_button = tk.Button(root, text="Add Response", command=add_new_response)
add_response_button.pack()


chat_log.insert(tk.END, "Nakama: " + random.choice(greetings) + "\n")
root.mainloop()
