from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

# Retrieves words from csv files, either from the words_to_learn file or the original data file if it does not exist
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')
word_dict = data.to_dict(orient='records')


def next_card():
    """
    Resets timer for flipping card, displays the next vocabulary word and changes UI elements
    """
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(word_dict)

    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(lang_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_word['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """
    Switches card to definition and changes UI elements
    """
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(lang_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_word['English'], fill='white')


def word_known():
    """
    Removes word from word list if the user knows the word and overwrites the words_to_learn.csv before moving to
    the next card
    """
    word_dict.remove(current_word)
    new_df = pandas.DataFrame(word_dict)
    new_df.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front)
lang_text = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=word_known)
right_button.grid(row=1, column=1)


next_card()

window.mainloop()
