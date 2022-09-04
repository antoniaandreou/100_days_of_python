# ----------------------- MODULES ---------------------- #

import tkinter as tk

# ----------------------- CONSTANTS ---------------------- #

BACKGROUND_COLOR = '#FFF5E1'
FRONTGROUND_COLOR = '#FFD39A'
TITLE_COLOUR = '#781C68'
WORD_COLOUR = '#319DA0'
TITLE_FONT = ('Arial Nova Light', 40, 'italic')
WORD_FONT = ('Arial Nova Light', 60, 'bold')

# ----------------------- FUNCTIONS ---------------------- #


# ----------------------- MAIN ---------------------- #

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
                   , highlightbackground=FRONTGROUND_COLOR)
canvas.grid(column=0, row=0, rowspan=1, columnspan=2)

canvas.create_text(400, 150
                   , text='Spanish'
                   , font=TITLE_FONT
                   , fill=TITLE_COLOUR)

canvas.create_text(400, 250
                   , text='Sample Word'
                   , font=WORD_FONT
                   , fill=WORD_COLOUR)

right = tk.PhotoImage(file="images/right.png")
wrong = tk.PhotoImage(file="images/wrong.png")

right_button = tk.Button(image=right
                         , borderwidth=0
                         , highlightthickness=5
                         , highlightbackground="green")
right_button.grid(column=0, row=1, pady=50, padx=50)

wrong_button = tk.Button(image=wrong
                         , borderwidth=0
                         , highlightthickness=5
                         , highlightbackground="red")
wrong_button.grid(column=1, row=1, pady=50, padx=50)


window.mainloop()
