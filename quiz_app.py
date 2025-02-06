import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Correct answer is the first option (index 0)
    },
    {
        "topic": "Lists",
        "question": "What is the correct syntax to create a list in Python?",
        "options": ["[]", "{}", "()", "<>"],
        "answer": 0  # Correct answer is the first option (index 0)
    },
    {
        "topic": "Strings",
        "question": "What will be the output of this code snippet?",
        "code": "s = 'Hello World'\nprint(s[6:])",
        "options": ["World", "Hello", "Hello World", "Error"],
        "answer": 0  # Correct answer is the first option (index 0)
    },
    {
        "topic": "Dictionaries",
        "question": "How do you add a new key-value pair to a dictionary in Python?",
        "options": ["dict.add('key', 'value')", "dict['key'] = 'value'", "dict.append('key', 'value')", "dict.insert('key', 'value')"],
        "answer": 1  # Correct answer is the second option
    },
    {
        "topic": "Dictionaries",
        "question": "What will be the output of this code?",
        "code": "d = {'a': 1, 'b': 2}\nprint(d['b'])",
        "options": ["1", "2", "KeyError", "None"],
        "answer": 1  # Correct answer is the second option ("2")
    },
]

# Function to display a new question based on the topic
def generate_question():
    topic = topic_entry.get()
    # Find a question that matches the entered topic
    for question in questions:
        if question['topic'].lower() == topic.lower():
            display_question(question)
            return
    messagebox.showerror("Error", f"No questions found for topic: {topic}")

# Function to display question, options, and code
def display_question(question):
    # Clear previous question and options
    question_label.config(text=question['question'])
    code_label.config(text=question.get('code', ''), fg="blue", font=("Courier", 12))
    var.set(-1)  # Deselect any previous options

    # Display the options
    for i, option in enumerate(question['options']):
        option_buttons[i].config(text=option, font=("Helvetica", 12), bg="#f0f0f0")

    # Store the correct answer for checking later
    correct_answer.set(question['answer'])

# Function to check the answer
def check_answer():
    selected_answer = var.get()
    if selected_answer == correct_answer.get():
        feedback_label.config(text="Correct! Well done!", fg="green", font=("Helvetica", 14))
    else:
        feedback_label.config(text="Incorrect. Try again.", fg="red", font=("Helvetica", 14))

# Initialize the main window
root = tk.Tk()
root.title("Python Quiz App")

# Set window size and background color
root.geometry("500x500")
root.config(bg="#f9f9f9")

# Create a frame to hold the content
frame = tk.Frame(root, bg="#f9f9f9", padx=20, pady=20)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Input field to enter the topic
topic_label = tk.Label(frame, text="Enter Python topic:", bg="#f9f9f9", font=("Helvetica", 12))
topic_label.grid(row=0, column=0, padx=10, pady=10)

topic_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
topic_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate a new question
generate_button = tk.Button(frame, text="Generate Python Question", command=generate_question, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief="flat")
generate_button.grid(row=1, columnspan=2, pady=20)

# Display the question and code
question_label = tk.Label(frame, text="", wraplength=400, bg="#f9f9f9", font=("Helvetica", 12))
question_label.grid(row=2, columnspan=2, pady=10)

code_label = tk.Label(frame, text="", fg="blue", font=("Courier", 12), bg="#f9f9f9")
code_label.grid(row=3, columnspan=2, pady=10)

# Variable for storing selected option
var = tk.IntVar(value=-1)

# Option buttons for multiple choices
option_buttons = []
for i in range(4):
    button = tk.Radiobutton(frame, text="", variable=var, value=i, font=("Helvetica", 12), bg="#f9f9f9")
    button.grid(row=4 + i, columnspan=2, pady=5, sticky="w")
    option_buttons.append(button)

# Store the correct answer to compare later
correct_answer = tk.IntVar()

# Submit button to check the answer
submit_button = tk.Button(frame, text="Submit", command=check_answer, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white", relief="flat")
submit_button.grid(row=8, columnspan=2, pady=20)

# Feedback area for answer result
feedback_label = tk.Label(frame, text="", bg="#f9f9f9")
feedback_label.grid(row=9, columnspan=2)

# Run the app
root.mainloop()