from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


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
    # But just change the range if you would like a different number
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # A  change from the previous day - puts the data in a dict to add to a json file
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    # Check to see if the user has filled out all the needed fields
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:  # Makes json file if none is present
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #


def find_password():
    """
    Attempts to open a json data file, searches for password records and returns the details if it they exist
    """
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data Stored", message="No data file found")
    else:
        website = website_entry.get()
        if website in data.keys():
            messagebox.showinfo(title=f"{website} Details", message=f"Email: {data[website]['email']}\n"
                                                                    f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="No Details", message=f"No details for {website} exist")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky='EW')
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
email_entry.insert(0, "test@email.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='EW')

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky='EW')

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
