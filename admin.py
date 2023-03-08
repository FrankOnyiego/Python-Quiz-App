import tkinter as tk
import sqlite3
from tkinter import messagebox


# Create a SQLite connection and cursor
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Show a message to indicate that the question was saved
messagebox.showinfo("Login", "Successfully loggen in!")

# Create the questions table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY,
                  question TEXT,
                  choice1 TEXT,
                  choice2 TEXT,
                  choice3 TEXT,
                  choice4 TEXT,
                  difficulty TEXT)''')

# Create the GUI window
window = tk.Tk()
window.title("Question Setter")

# Set the window size to 720x440 pixels
window.geometry("720x440")

# Create the question entry box
question_label = tk.Label(window, text="Question:")
question_label.pack()
question_entry = tk.Entry(window, width=50)
question_entry.pack()

# Create the answer choice entry boxes
choice1_label = tk.Label(window, text="Choice 1:")
choice1_label.pack()
choice1_entry = tk.Entry(window, width=50)
choice1_entry.pack()

choice2_label = tk.Label(window, text="Choice 2:")
choice2_label.pack()
choice2_entry = tk.Entry(window, width=50)
choice2_entry.pack()

choice3_label = tk.Label(window, text="Choice 3:")
choice3_label.pack()
choice3_entry = tk.Entry(window, width=50)
choice3_entry.pack()

choice4_label = tk.Label(window, text="Choice 4:")
choice4_label.pack()
choice4_entry = tk.Entry(window, width=50)
choice4_entry.pack()

answer_label = tk.Label(window, text="answer:")
answer_label.pack()
answer_entry = tk.Entry(window, width=50)
answer_entry.pack()

# Create the difficulty level dropdown menu
difficulty_label = tk.Label(window, text="Difficulty Level:")
difficulty_label.pack()
difficulty_options = ["Easy", "Medium", "Hard"]
difficulty_var = tk.StringVar(window)
difficulty_var.set(difficulty_options[0])
difficulty_menu = tk.OptionMenu(window, difficulty_var, *difficulty_options)
difficulty_menu.pack()

# Define a function to save the question to the database
def save_question():
    # Get the question, answer choices, and difficulty level from the entry boxes and dropdown menu
    question = question_entry.get()
    choice1 = choice1_entry.get()
    choice2 = choice2_entry.get()
    choice3 = choice3_entry.get()
    choice4 = choice4_entry.get()
    answer = answer_entry.get()
    difficulty = difficulty_var.get()

    # Insert the question into the database
    cursor.execute("INSERT INTO questions (question, choice1, choice2, choice3, choice4, difficulty,answer) VALUES (?, ?, ?, ?, ?, ?,?)",
                   (question, choice1, choice2, choice3, choice4, difficulty,answer))
    conn.commit()

    # Clear the entry boxes
    question_entry.delete(0, tk.END)
    choice1_entry.delete(0, tk.END)
    choice2_entry.delete(0, tk.END)
    choice3_entry.delete(0, tk.END)
    choice4_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)

    # Show a message to indicate that the question was saved
    messagebox.showinfo("Question Setter", "Question saved successfully!")

# Create the "Save Question" button
save_button = tk.Button(window, text="Save Question", command=save_question, bg="green",padx=2,pady=2)

save_button.pack()

# Start the GUI event loop
window.mainloop()

# Close the SQLite connection
conn.close()
