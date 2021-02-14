from tkinter import *
import pandas as pd
import random

# Get the data
data = pd.read_csv("Spanish_words.csv")
language_data = data.to_dict(orient="records")
current_word = {}


def next_card():
    """This function displays random words to the user"""
    global current_word, flip_timer
    interface.after_cancel(flip_timer)
    current_word = random.choice(language_data)
    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(word, text=current_word["Spanish"], fill="black")
    canvas.itemconfig(card_image, image=front_image)
    flip_timer = interface.after(5000, func=flip_card)


def flip_card():
    """This function displays the english meaning of the word"""
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_image, image=back_image)


BACKGROUND_COLOR = "#3396ff"

# Setup the User interface
interface = Tk()
interface.title("Study the Spanish Language")
interface.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = interface.after(5000, func=flip_card)

# Add front card image using canvas widget
canvas = Canvas(width=340, height=210)
front_image = PhotoImage(file="flash_cards/front.png")
back_image = PhotoImage(file="flash_cards/back.png")
card_image = canvas.create_image(170, 105, image=front_image)
settings = canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(170, 55, text="", font=("Arial", 30, "italic"))
word = canvas.create_text(170, 140, text="", font=("Arial", 50, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

cross = PhotoImage(file="verify/unknown.png")
unknown_button = Button(image=cross, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check = PhotoImage(file="verify/known.png")
known_button = Button(image=check, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()

# Keeps the interface open until exited
interface.mainloop()
