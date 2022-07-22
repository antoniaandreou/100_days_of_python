from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"


# ---------------------------- GLOBAL VARIABLES -------------------------- #
reps = 0
timer_clock = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Function to reset the program to its original settings when 'Reset' button is pressed.
    :return: None
    """
    global timer_clock
    global reps
    window.after_cancel(timer_clock)
    title.config(text="Timer", fg=GREEN)
    tracker.config(text="")
    canvas.itemconfig(timer, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_timer():
    """
    Main function starting the sessions and timer. Type of session determined by the global variable reps.
    :return: None
    """
    global reps
    reps += 1
    seconds = 60
    if reps % 8 == 0:
        counter(LONG_BREAK_MIN * seconds)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        counter(SHORT_BREAK_MIN * seconds)
        title.config(text="Break", fg=PINK)
    else:
        counter(WORK_MIN * seconds)
        title.config(text="Work", fg=GREEN)
        tracker.config(text=CHECK_MARK * int(reps / 2))


# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def counter(count: int):
    """
    Displays the correct counter according to the session the user is in
    :param count: minutes for the session
    :return: None
    """
    global timer_clock
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        timer_clock = window.after(1000, counter, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ---------------------------------- #
# -- WINDOW SET UP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# -- TITLE SET UP
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

# -- IMAGE SET UP
tomato_image = PhotoImage(file="tomato.png")

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(104, 112, image=tomato_image)
timer = canvas.create_text(104, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# -- START BUTTON SET UP
start_button = Button(text="Start",
                      fg=PINK,
                      bg=YELLOW,
                      border=0,
                      highlightthickness=0,
                      font=(FONT_NAME, 16, "italic"),
                      command=start_timer)
start_button.grid(column=0, row=2)

# -- RESET BUTTON SET UP
reset_button = Button(text="Reset",
                      fg=PINK,
                      bg=YELLOW,
                      border=0,
                      highlightthickness=0,
                      font=(FONT_NAME, 16, "italic"),
                      command=reset_timer)
reset_button.grid(column=2, row=2)

# -- TICK MARK SET UP
tracker = Label(fg=RED, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tracker.grid(column=1, row=3)

window.mainloop()
