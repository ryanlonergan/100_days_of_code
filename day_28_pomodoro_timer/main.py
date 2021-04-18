from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """
    Resets UI, global reps counter and any timers
    """
    window.after_cancel(timer)
    top_text.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    checkmarks_text.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """
    Increases global reps counter by 1 and starts timer for long break, short break or work period based on the reps counter
    """
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        top_text.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        top_text.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        top_text.config(text='Work', fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """
    Takes the amount of time for the work or break period and prints the count down on the screen. Also adds checkmarks
    for successful work periods.
    :param count: The amount of time for the work or break period
    """
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks = '✔' * int(reps / 2)
            checkmarks_text.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)


top_text = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36, 'bold'))
top_text.config(padx=50)
top_text.grid(column=1, row=0)


start_button = Button(text='Start', font=(FONT_NAME, 12, 'normal'), highlightthickness=0,
                      borderwidth=0, bg='white', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'normal'), highlightthickness=0,
                      borderwidth=0, bg='white', command=reset_timer)
reset_button.grid(column=3, row=2)


checkmarks_text = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, 'normal'))
checkmarks_text.grid(column=1, row=3)


window.mainloop()
