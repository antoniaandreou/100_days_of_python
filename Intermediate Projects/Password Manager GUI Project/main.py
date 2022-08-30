from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------ #
BLUE = "#8CC0DE"
BEIGE = "#FAF0D7"
PINK = "#F4BFBF"
ORANGE = "#FFD9C0"
FONT = ("Courier", 16, "bold")
INPUT_COLOUR = "#2A2550"
PW_FONT = ("Courier", 12)


# ---------------------------- PASSWORD GENERATOR ---------------------- #


def password_generator():
    """
    Generates a random password with letters, symbols and numbers of a random length between 12 and 18 characters.
    Copies password to clipboard and autofill the password entry field in the UI.
    :return: None
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]  # Letters
    [password_list.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]  # Symbols
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]  # Numbers
    random.shuffle(password_list)

    password_gen = ''.join(password_list)  # Creates the password string
    pyperclip.copy(password_gen)  # Copies the password on clipboard
    pw_entry.insert(0, password_gen)  # Inserts the password in the UI entry space


# ---------------------------- SAVE PASSWORD --------------------------- #


def save():
    """
    The function writes the information passed in the UI in a json-=p[[ file.
    Clears the UI and re-inserts the email ready for next entry.
    :return: None
    """
    # -- Extract variables needed
    site = web_entry.get().lower()
    user = email_entry.get().lower()
    pswrd = pw_entry.get().lower()
    new_entry = {
        site: {
            "email": user,
            "password": pswrd
        }
    }
    if len(site) == 0 or len(pswrd) == 0 or len(user) == 0:
        messagebox.showerror(title="Incomplete Fields Error",
                             message="Ensure there are no empty fields! ")
    else:
        is_ok = messagebox.askokcancel(title=f"{site}",
                                       message=f"Credentials...\nUsername: {user}\n Password: {pswrd}\n"
                                               f"Save credentials?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_entry, file, indent=4)
            else:
                data.update(new_entry)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entries = [web_entry, email_entry, pw_entry]
                for _ in entries:
                    _.delete(0, END)

                email_entry.insert(0, "antoniaandreou@gmail.com")
                messagebox.showinfo(title="Confirmation", message="Credentials successfully saved")


# ---------------------------- SEARCH PASSWORD ------------------------- #
def find_password():
    """
    The function looks through the json file that stores the passwords and extracts based on the website.
    :return: None
    """
    site = web_entry.get().lower()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Not Data Found",
                            message=f"No data file found")
    else:
        for key in data:
            if key == site:
                email = data[key]["email"]
                password = data[key]["password"]
                messagebox.showinfo(title=f"{key.title()}",
                                    message=f"\nEmail: {email}"
                                            f"\nPassword: {password}")
                break
        else:
            messagebox.showinfo(title=f"No Entry Found",
                                message=f"No details for this website exist")


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

web_entry = Entry(width=22, bg=ORANGE, fg=INPUT_COLOUR, highlightthickness=0, textvariable=web_ref)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=37, bg=ORANGE, fg=INPUT_COLOUR, highlightthickness=0, textvariable=username)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "antoniaandreou@gmail.com")

pw_entry = Entry(width=22, bg=ORANGE, fg=INPUT_COLOUR, highlightthickness=0, textvariable=password)
pw_entry.grid(column=1, row=3)

# -- BUTTON SETUP
search_button = Button(width=14,
                       text="Search",
                       font=PW_FONT,
                       bg=ORANGE,
                       border=0,
                       highlightbackground=BEIGE,
                       command=find_password)
search_button.grid(column=2, row=1, sticky="N")

pw_button = Button(width=14,
                   text="Generate Password",
                   font=PW_FONT,
                   bg=PINK,
                   border=0,
                   highlightbackground=BEIGE,
                   command=password_generator)
pw_button.grid(column=2, row=3, sticky="N")

add_button = Button(width=43,
                    text="ADD",
                    font=PW_FONT,
                    bg=ORANGE,
                    border=0,
                    highlightbackground=BEIGE,
                    command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
