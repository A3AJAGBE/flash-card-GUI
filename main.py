from tkinter import *
import pandas as pd
import random

# Get the data
data = pd.read_csv("Spanish_words.csv")
language_data = data.to_dict(orient="records")


def next_card():
    """This function displays random words to the user"""
    current = random.choice(language_data)
    canvas.itemconfig(language, text="Spanish")
    canvas.itemconfig(word, text=current["Spanish"])


BACKGROUND_COLOR = "#007bff"

# Setup the User interface
interface = Tk()
interface.title("Study the Spanish Language")
interface.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Add front card image using canvas widget
canvas = Canvas(width=340, height=210)
bg_image = PhotoImage(file="flash_cards/front.png")
canvas.create_image(170, 105, image=bg_image)
settings = canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(170, 55, text="Title", font=("Arial", 30, "italic"))
word = canvas.create_text(170, 140, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

cross = PhotoImage(file="verify/unknown.png")
unknown_button = Button(image=cross, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check = PhotoImage(file="verify/known.png")
known_button = Button(image=check, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

# Keeps the interface open until exited
interface.mainloop()
