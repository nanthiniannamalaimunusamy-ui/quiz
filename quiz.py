import tkinter as tk

questions = [
    {
        "question": "Which language is used to create this GUI?",
        "options": ["Java", "Python", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "Which library is used to create GUI in Python?",
        "options": ["NumPy", "Tkinter", "Pandas", "Matplotlib"],
        "answer": "Tkinter"
    },
    {
        "question": "Which data structure follows LIFO?",
        "options": ["Queue", "Array", "Stack", "Linked List"],
        "answer": "Stack"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "def"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    }
]

current_question = 0
time_left = 15
timer_id = None

# Store answers selected by the user
selected_answers = [None] * len(questions)

root = tk.Tk()
root.title("Quiz Application")
root.geometry("700x500")
root.resizable(False, False)

root.configure(bg="#EAF4F4")

title_label = tk.Label(
    root,
    text="Python Quiz",
    font=("Arial", 24, "bold"),
    bg="#EAF4F4"
)

title_label.pack(pady=20)

question_number = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#EAF4F4"
)

question_number.pack()

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    wraplength=600,
    bg="#EAF4F4"
)

question_label.pack(pady=20)

timer_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#EAF4F4"
)

timer_label.pack(pady=5)

selected_option = tk.StringVar()

radio_buttons = []

for i in range(4):

    rb = tk.Radiobutton(
        root,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 13),
        bg="#EAF4F4",
        anchor="w",
        width=40
    )

    rb.pack(pady=5)

    radio_buttons.append(rb)

button_frame = tk.Frame(
    root,
    bg="#EAF4F4"
)

button_frame.pack(side="bottom", pady=20)

def load_question():
    global time_left, timer_id

    # Stop old timer
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    question = questions[current_question]

    # Question number
    question_number.config(
        text=f"Question {current_question + 1} of {len(questions)}"
    )

    # Question text
    question_label.config(
        text=question["question"]
    )

    # Options
    for i in range(4):
        radio_buttons[i].config(
            text=question["options"][i],
            value=question["options"][i]
        )

    # Load previously selected answer
    if selected_answers[current_question] is not None:
        selected_option.set(selected_answers[current_question])
    else:
        selected_option.set("")

    # Change button according to question number
    if current_question == len(questions) - 1:
        next_button.pack_forget()
        finish_button.pack(side="right", padx=20)
    else:
        finish_button.pack_forget()
        next_button.pack(side="right", padx=20)

    # Previous button
    if current_question == 0:
        previous_button.config(state="disabled")
    else:
        previous_button.config(state="normal")

    # Start timer
    time_left = 15
    timer_label.config(text=f"Time: {time_left}")

    countdown()


def countdown():
    global time_left, timer_id

    timer_label.config(text=f"Time: {time_left}")

    if time_left > 0:

        time_left -= 1

        timer_id = root.after(
            1000,
            countdown
        )

    else:
        # Time is over
        save_answer()

        if current_question < len(questions) - 1:
            next_question()
        else:
            finish_quiz()


def save_answer():
    selected_answers[current_question] = selected_option.get()


def next_question():
    global current_question

    save_answer()

    if current_question < len(questions) - 1:

        current_question += 1

        load_question()


def previous_question():
    global current_question

    save_answer()

    if current_question > 0:

        current_question -= 1

        load_question()


def finish_quiz():
    global timer_id

    save_answer()

    # Stop timer
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    # Calculate score
    score = 0

    for i in range(len(questions)):

        if selected_answers[i] == questions[i]["answer"]:
            score += 1

    show_result(score)


def show_result(score):

    # Hide quiz widgets
    question_number.pack_forget()
    question_label.pack_forget()
    timer_label.pack_forget()

    for rb in radio_buttons:
        rb.pack_forget()

    previous_button.pack_forget()
    next_button.pack_forget()
    finish_button.pack_forget()

    # Show result
    result_label.config(
        text=f"Quiz Completed!\n\n"
             f"Your Score: {score}/{len(questions)}\n\n"
             f"Percentage: {(score / len(questions)) * 100:.0f}%"
    )

    result_label.pack(pady=60)

    restart_button.pack(pady=10)


def restart_quiz():

    global current_question

    current_question = 0

    # Clear all answers
    for i in range(len(selected_answers)):
        selected_answers[i] = None

    # Hide result
    result_label.pack_forget()
    restart_button.pack_forget()

    # Show quiz widgets
    question_number.pack()
    question_label.pack(pady=20)
    timer_label.pack(pady=5)

    for rb in radio_buttons:
        rb.pack(pady=5)

    previous_button.pack(side="left", padx=20)
    next_button.pack(side="right", padx=20)

    load_question()


previous_button = tk.Button(
    button_frame,
    text="Previous",
    font=("Arial", 12, "bold"),
    command=previous_question,
    width=12
)

previous_button.pack(side="left", padx=20)


next_button = tk.Button(
    button_frame,
    text="Next",
    font=("Arial", 12, "bold"),
    command=next_question,
    width=12
)


finish_button = tk.Button(
    button_frame,
    text="Finish",
    font=("Arial", 12, "bold"),
    command=finish_quiz,
    width=12
)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 22, "bold"),
    bg="#EAF4F4"
)


restart_button = tk.Button(
    root,
    text="Restart Quiz",
    font=("Arial", 12, "bold"),
    command=restart_quiz,
    width=15
)

load_question()

root.mainloop()