from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)


# Input field
input_field = Entry(width=5)
input_field.insert(END, '0')
input_field.grid(column=1, row=0)

# Miles label
miles_label = Label(text='miles')
miles_label.grid(column=2, row=0)

# Equals label
equals_label = Label(text='is equal to')
equals_label.grid(column=0, row=1)

# calculation label
calc_label = Label(text='0')
calc_label.grid(column=1, row=1)

# Km label
km_label = Label(text='Km')
km_label.grid(column=2, row=1)


# Calculate button
def calculate():
    num_miles = input_field.get()
    num_km = round(int(num_miles) * 5/3, 2)
    calc_label.config(text=num_km)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
