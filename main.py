from tkinter import *
import pandas as french
import random

BACKGROUND_COLOR = "#B1DDC6"

french_words = french.read_csv("french_words.csv")
french_dict = french_words.to_dict("records")
choice_fr = {}


def random_word():
    global choice_fr
    choice_fr = random.choice(french_dict)
    title_label.config(text="Francois", bg="white")
    word_label.config(text=f"{choice_fr['French']}", bg="white")
    canvas.itemconfig(fr_image, image=front_card)



def change_card():
    title_label.config(text="English", bg=BACKGROUND_COLOR)
    word_label.config(text=f"{choice_fr['English']}", bg=BACKGROUND_COLOR)
    canvas.itemconfig(fr_image, image=back_card)


screen = Tk()
screen.minsize(1100, 900)
screen.config(bg=BACKGROUND_COLOR)
screen.title("Flash Cards")


front_card = PhotoImage(file="card_front.png")
back_card = PhotoImage(file="card_back.png")
canvas = Canvas(width=800, height=600,  bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.place(x=150, y=130)
fr_image = canvas.create_image(400, 300, image=front_card)

title_label = Label(text="French", font=("Arial", 20, "italic"))
title_label.config(bg="white")
title_label.place(x=490, y=300)

word_label = Label(text="frère", font=("Arial", 40, "bold"))
word_label.config(bg="white")
word_label.place(x=470, y=400)

pass_image = PhotoImage(file="right.png")
pass_button = Button(image=pass_image, highlightthickness=0)
pass_button.config(height=75, width=75, command=random_word)
pass_button.place(x=200, y=700)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.config(height=75, width=75, command=change_card)
wrong_button.place(x=800, y=700)




screen.mainloop()
