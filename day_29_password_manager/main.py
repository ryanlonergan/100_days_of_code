from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """
    Creates a random password that includes letters, numbers and symbols, shuffles it and then suggests it to the user
    in the GUI. Also copies the password to your clipboard.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # The program generates a random length for the password between 12 and 18 characters
    # But just change the range if you would like
    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)  # Nice way to change the order, useful to check out if you've never used it before

    password = "".join(password_list)  # Joins together all the symbols in the password_list to a string

    password_input.delete(0, END)  # Clears the password_input field in the GUI
    password_input.insert(0, password)
    pyperclip.copy(password)  # Copies the password to your clipboard if you want to use it right away


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """
    Checks if the fields were filled out correctly, checks that the user wants to save the password and will then
    creates or appends the details to a text file.
    """
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    # Check to see if the user has filled out all the needed fields
    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title='Oops', message='Please do not leave any field empty.')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n'
                                                              f'Username: {username}\n'
                                                              f'Password: {password}\n'
                                                              f'Is it ok to save?')

        if is_ok:
            with open('data.txt', 'a') as data:  # Will either create a new text file or append to an existing one
                data.write(f'{website}  |  {username}  |  {password}\n')
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('MyPass Password Manager')
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text='Website:')
website_text.grid(row=1, column=0)

username_text = Label(text='Email/Username:')
username_text.grid(row=2, column=0)

password_text = Label(text='Password:')
password_text.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky='EW')
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky='EW')
username_input.insert(0, 'default@email.com')

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky='EW')

# Buttons
generate_button = Button(text='Generate Password', highlightthickness=0, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', highlightthickness=1, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
