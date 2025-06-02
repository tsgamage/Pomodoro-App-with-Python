import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF748B"
DARK_PINK = "#F72C5B"

BLUE = "#77CDFF"
GREEN = "#7aff77"
PURPLE = "#D895DA"
YELLOW = "#ffe777"
ORANGE = "#ff9600"

NUM_FONT_NAME = "Courier"
FONT_NAME = "montserrat"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

WORKING_TIME_SEC = 2
SMALL_BREAK_SEC = 2
LONG_BREAK_SEC = 5

_is_running = True
loop_time = 0
check_marks = ""


def change_color(color):
    window.config(bg=color)
    canvas.config(bg=color)
    header_text.config(bg=color)
    checkmark_label.config(bg=color)


def timer(count):
    if _is_running:
        timer_min = math.floor(count / 60)
        timer_sec = count % 60

        if timer_min < 10:
            timer_min = f"0{timer_min}"
        if timer_sec < 10:
            timer_sec = f"0{timer_sec}"
        if timer_sec == 0:
            timer_sec = "00"

        canvas.itemconfig(timer_text, text=f"{timer_min}:{timer_sec}")
        if count > 0:
            window.after(1000, timer, count - 1)
        else:
            call_timer()


def reset():
    global _is_running, loop_time, check_marks, timer_text

    header_text.config(text="Ready to Focus?")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    change_color(BLUE)
    _is_running = False
    loop_time = 0
    check_marks = ""


def call_timer():
    global loop_time, check_marks, _is_running

    _is_running = True
    loop_time += 1

    print(f"loop_time: {loop_time}")

    if loop_time == 8:
        print(f"called", 3)
        timer(LONG_BREAK_SEC)
        change_color(YELLOW)
        check_marks = ''
        header_text.config(text="Take a Long Break!")

    elif loop_time % 2 == 0:
        print(f"called", 2)
        timer(SMALL_BREAK_SEC)
        change_color(PURPLE)
        header_text.config(text="Take a Little Break!")

    elif loop_time % 2 == 1:
        print(f"called", 1)
        timer(WORKING_TIME_SEC)
        change_color(GREEN)
        check_marks += '🔥'  # ✔
        checkmark_label.config(text=check_marks)
        header_text.config(text="Stay Focused!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.geometry("300x410")
window.resizable(False, False)
window.config(padx=25, pady=25, bg=BLUE)

logo = PhotoImage(file="./assets/tomato.png")
window.iconphoto(False, logo)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

header_text = Label(text="Ready to Focus?")
header_text.config(font=(FONT_NAME, 20), bg=BLUE, )
header_text.grid(row=0, column=0, columnspan=2)

canvas = Canvas()
canvas.config(bg=BLUE, width=250, height=224, highlightthickness=0)
tomato_image = PhotoImage(file="./assets/tomato.png")
canvas.create_image(125, 112, image=tomato_image)
timer_text = canvas.create_text(125, 130, text="00:00", font=(FONT_NAME, 36), fill="white")
canvas.grid(row=1, column=0, columnspan=2)

checkmark_label = Label(text="")
checkmark_label.config(font=(FONT_NAME, 18), bg=BLUE, fg='#1B3C73')
checkmark_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

start_btn = Button(text="Start")
start_btn.config(width=10, height=1, font=(FONT_NAME, 18), bg=PINK, fg='white', activebackground=DARK_PINK,
                 activeforeground='white', command=call_timer)
start_btn.grid(row=3, column=0, padx=5, pady=10)

reset_btn = Button(text="Reset")
reset_btn.config(width=10, height=1, font=(FONT_NAME, 18), bg=PINK, fg='white', activebackground=DARK_PINK,
                 activeforeground='white', command=reset)
reset_btn.grid(row=3, column=1, padx=5, pady=10)

window.mainloop()
