from tkinter import *

# ---------------------------- CONSTANTS ------------------------------ #
BLUE = "#8CC0DE"
BEIGE = "#FAF0D7"
PINK = "#F4BFBF"
ORANGE = "#FFD9C0"
FONT = ("Courier", 16, "bold")
INPUT_COLOUR = "#2A2550"
PW_FONT = ("Courier", 12)

# --------------------------- GLOBAL VARIABLES ------------------------- #


# ---------------------------- PASSWORD GENERATOR ---------------------- #

# ---------------------------- SAVE PASSWORD --------------------------- #
def save():
    print(password.get())


# ---------------------------- UI SETUP -------------------------------- #
# -- WINDOW SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=BEIGE)

# -- CANVAS SETUP
logo_image = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200, bg=BEIGE, highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# -- LABELS SETUP
web_label = Label(text="Website:", fg=BLUE, bg=BEIGE, font=FONT)
web_label.grid(column=0, row=1, sticky="E")

email_label = Label(text="Email/Username:", fg=BLUE, bg=BEIGE, font=FONT)
email_label.grid(column=0, row=2)

pw_label = Label(text="Password:", fg=BLUE, bg=BEIGE, font=FONT)
pw_label.grid(column=0, row=3, sticky="E")

# -- ENTRY SETUP
web_ref = StringVar()
username = StringVar()
password = StringVar()

web_entry = Entry(width=37, bg=ORANGE, fg=INPUT_COLOUR, highlightthickness=0, textvariable=web_ref)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=37, bg=ORANGE, fg=INPUT_COLOUR, highlightthickness=0, textvariable=username)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "antoniaandreou21@gmail.com")

pw_entry = Entry(width=22, bg=ORANGE, fg=INPUT_COLOUR, highlightthickness=0, textvariable=password)
pw_entry.grid(column=1, row=3)

# -- BUTTON SETUP
pw_button = Button(width=14, text="Generate Password", font=PW_FONT, bg=PINK, border=0, highlightbackground=BEIGE)
pw_button.grid(column=2, row=3, sticky="N")

add_button = Button(width=43, text="ADD", font=PW_FONT, bg=ORANGE, border=0, highlightbackground=BEIGE)
add_button.grid(column=1, row=4, columnspan=2)

save()


window.mainloop()
