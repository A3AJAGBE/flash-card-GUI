from tkinter import *

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
language = canvas.create_text(170, 55, text="Spanish", font=("Arial", 30, "italic"))
word = canvas.create_text(170, 140, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

cross = PhotoImage(file="verify/unknown.png")
unknown_button = Button(image=cross, highlightthickness=0)
unknown_button.grid(column=0, row=1)

check = PhotoImage(file="verify/known.png")
known_button = Button(image=check, highlightthickness=0)
known_button.grid(column=1, row=1)

# Keeps the interface open until exited
interface.mainloop()
