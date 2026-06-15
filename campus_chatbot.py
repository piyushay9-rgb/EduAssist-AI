import tkinter as tk
from tkinter import scrolledtext

def get_response(user_input):
    user_input = user_input.lower()

    if "admission" in user_input:
        return "Admissions open on 1st July and close on 31st August."

    elif "fee" in user_input:
        return "Fees can be paid online through the student portal or at the Accounts Office."

    elif "library" in user_input:
        return "The library is open Monday to Saturday from 8:00 AM to 8:00 PM."

    elif "timetable" in user_input or "schedule" in user_input:
        return "Your timetable is available in the Student Portal under Academics > Timetable."

    elif "event" in user_input:
        return "Upcoming events include the Tech Fest on Friday and the Cultural Program on Saturday."

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "thank" in user_input:
        return "You're welcome! Happy to help."

    else:
        return "Sorry, I didn't understand that. Please ask about admissions, fees, library, timetable, or events."

def send_message():
    user_message = entry.get()

    if user_message.strip() == "":
        return

    chat_area.insert(tk.END, f"You: {user_message}\n")
    bot_response = get_response(user_message)
    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")

    entry.delete(0, tk.END)
    chat_area.see(tk.END)

root = tk.Tk()
root.title("Campus FAQ Assistant")
root.geometry("600x500")

title = tk.Label(root, text="Campus FAQ Assistant", font=("Arial", 16, "bold"))
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
chat_area.pack(padx=10, pady=10)

chat_area.insert(
    tk.END,
    "Bot: Welcome to Campus FAQ Assistant!\n"
    "Ask me about admissions, fees, library, timetable, or events.\n\n"
)

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

root.mainloop()