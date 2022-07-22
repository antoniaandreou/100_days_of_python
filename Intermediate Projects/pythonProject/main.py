from tkinter import *


def converter():
    mls = input.get()
    km = float(mls) * 1.60934
    kms_result = Label(text=km, font=("Arial", 24, "bold"))
    kms_result.grid(column=1, row=1)
    kms_result.config(padx=10, pady=10)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels
equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# Entry
input = Entry(width=10, font=("Microsoft San Serif", 26, "italic"))
print(input.get())
input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=converter, font=("Microsoft San Serif", 22, "italic"))
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

window.mainloop()
