from tkinter import *

# Setup the User interface
interface = Tk()
interface.title("Study the Spanish Language")
interface.config(padx=50, pady=50, bg="#007bff")

# Add front card image using canvas widget
canvas = Canvas(width=340, height=210, bg="#007bff", highlightthickness=0)
bg_image = PhotoImage(file="front.png")
canvas.create_image(170, 105, image=bg_image)
language = canvas.create_text(170, 55, text="Spanish", font=("Arial", 30, "italic"))
word = canvas.create_text(170, 140, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, columnspan=2, row=0)


# Keeps the interface open until exited
interface.mainloop()
