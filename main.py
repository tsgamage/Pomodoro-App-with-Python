import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF748B"
DARK_PINK = "#F72C5B"
RED = "#e7305b"
GREEN = "#A6CF98"
NUM_FONT_NAME = "Courier"
FONT_NAME = "montserrat"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

WORKING_TIME = 25 * 60
SMALL_BREAK = 5 * 60
LONG_BREAK = 20 * 60

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.geometry("300x410")
window.resizable(False, False)
window.config(padx=25, pady=25, bg=GREEN)

logo = PhotoImage(file="./assets/tomato.png")
window.iconphoto(False, logo)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

header_text = Label(text="Pomodoro App")
header_text.config(font=(FONT_NAME, 20), bg=GREEN, )
header_text.grid(row=0, column=0, columnspan=2)

canvas = Canvas()
canvas.config(bg=GREEN, width=250, height=224, highlightthickness=0)
tomato_image = PhotoImage(file="./assets/tomato.png")
canvas.create_image(125, 112, image=tomato_image)
canvas.create_text(125, 130, text="00:00", font=(FONT_NAME, 36), fill="white")
canvas.grid(row=1, column=0, columnspan=2)

checkmark_label = Label(text="✔✔✔")
checkmark_label.config(font=(FONT_NAME, 18), bg=GREEN, fg=RED)
checkmark_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

start_btn = Button(text="Start")
start_btn.config(width=10, height=1, font=(FONT_NAME, 18), bg=PINK, fg='white', activebackground=DARK_PINK,
                 activeforeground='white')
start_btn.grid(row=3, column=0, padx=5, pady=10)

reset_btn = Button(text="Reset")
reset_btn.config(width=10, height=1, font=(FONT_NAME, 18), bg=PINK, fg='white', activebackground=DARK_PINK,
                 activeforeground='white')
reset_btn.grid(row=3, column=1, padx=5, pady=10)

window.mainloop()
