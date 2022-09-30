# ----------------------- MODULES ---------------------- #

import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

# ----------------------- CONSTANTS ---------------------- #

BACKGROUND_COLOR = '#FFF5E1'
FRONT_COLOR = '#781C68'
TITLE_COLOUR = '#319DA0'
WORD_COLOUR = '#FFD39A'
TITLE_FONT = ('Arial Nova Light', 40, 'italic')
WORD_FONT = ('Arial Nova Light', 60, 'bold')

# ----------------------- FUNCTIONS ---------------------- #


def canvas_update(t: str, w: str, c: str, f: str):
    """
    Configuration of the title, word and background colour of the canvas card
    :param t: String for the canvas title
    :param w: String for the canvas word
    :param c: String for the canvas background colour
    :param f: String for the canvas text fill colour
    :return: NONE
    """
    canvas.itemconfig(title, text=t)
    canvas.itemconfig(word, text=w)
    canvas.itemconfig(word, fill=f)
    canvas.config(background=c)


def flash_cards():
    """
    The function enables the 'flip' of the canvas card after 3 seconds
    :return:NONE
    """
    global display_word
    display_word = random.choice(words_dict)
    data = list(display_word.items())
    canvas_update(data[0][0], data[0][1], BACKGROUND_COLOR, f=FRONT_COLOR)

    def english_translation():
        canvas_update(data[1][0], data[1][1], FRONT_COLOR, f=BACKGROUND_COLOR)
        window.after_cancel(solve)

    solve = window.after(3000, english_translation)


def unknown_words():
    """
    Function removes the known words from the words dictionary.
    :return: None
    """
    for i, dic in enumerate(words_dict):
        if dic["Spanish"] == display_word['Spanish']:
            del words_dict[i]


def on_starting():
    """
    Function determines if the user wants to continue or restart.
    If continue then select the complete words csv
    Else select the csv with the unknown words
    :return: None
    """
    global words
    ask = messagebox.askquestion(title='Game Restart'
                                 , message='Do you want to continue from last time?')
    print(ask)
    if ask == 'yes':
        words = pd.read_csv("data/words_to_learn.csv")
    elif ask == 'no':
        words = pd.read_csv("data/spanish_words.csv")


def on_closing():
    """
    Function prompts the user to confirm they want to exit the app.
    Saves the current words_dict with excluded known words to a csv file.
    :return: None
    """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        words_to_learn = pd.DataFrame.from_dict(words_dict)
        words_to_learn.to_csv('data/words_to_learn.csv', index=False)
        window.destroy()


# ----------------------- WINDOW SETUP ---------------------- #

window = tk.Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR
              , padx=50
              , pady=50)

canvas = tk.Canvas(window
                   , height=400
                   , width=800
                   , highlightthickness=10
                   , background=BACKGROUND_COLOR
                   , highlightbackground=FRONT_COLOR)
canvas.grid(column=0, row=0, rowspan=1, columnspan=2)

title = canvas.create_text(400, 150
                           , text='Spanish'
                           , font=TITLE_FONT
                           , fill=TITLE_COLOUR)

word = canvas.create_text(400, 250
                          , text="Sample Word"
                          , font=WORD_FONT
                          , fill=FRONT_COLOR)

right = tk.PhotoImage(file="images/right.png")
wrong = tk.PhotoImage(file="images/wrong.png")

right_button = tk.Button(image=right
                         , borderwidth=0
                         , highlightthickness=5
                         , highlightbackground="green"
                         , command=lambda: [unknown_words(), flash_cards()])
right_button.grid(column=0, row=1, pady=50, padx=50)

wrong_button = tk.Button(image=wrong
                         , borderwidth=0
                         , highlightthickness=5
                         , highlightbackground="red"
                         , command=flash_cards)
wrong_button.grid(column=1, row=1, pady=50, padx=50)

# ----------------------- MAIN ---------------------- #

on_starting()

words_dict = words.to_dict(orient="records")
display_word = random.choice(words_dict)

flash_cards()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
