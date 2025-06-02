import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

# Colors for Buttons
PINK = "#FF748B"
DARK_PINK = "#F72C5B"

# Colors for UI
BLUE = "#77CDFF"
GREEN = "#7aff77"
YELLOW = "#ffe777"
PURPLE = "#D895DA"

# Colors for Elements
CHECKMARK_COLOR = "#1B3C73"

# Fonts
NUM_FONT_NAME = "Courier"
TEXT_FONT_NAME = "montserrat"

# Application's main timings
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timing in seconds
WORKING_TIME_SEC = WORK_MIN * 60
SMALL_BREAK_SEC = SHORT_BREAK_MIN * 60
LONG_BREAK_SEC = LONG_BREAK_MIN * 60

# Global Variables
_started = True
loop_time = 0
check_marks = ""
timer = None


# ---------------------------- Mechanism ------------------------------- #

# The main function that updates the timer every 1 second
def timer_counter(count):
    # changing the given seconds to minutes and seconds
    timer_min = math.floor(count / 60)
    timer_sec = count % 60

    # Adding a '0' to the front of minutes when it is smaller than 10
    if timer_min < 10:
        timer_min = f"0{timer_min}"

    # Adding a '0' to the front of seconds when it is smaller than 10
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"

    # Adding additional 0 to the seconds when it is zero
    if timer_sec == 0:
        timer_sec = "00"

    # Updates the timer text showed on canvas
    canvas.itemconfig(timer_text, text=f"{timer_min}:{timer_sec}")

    # Update the timer only when count (the given seconds) bigger than zero
    # If count not bigger than zero it means the timer has finished running
    if count > 0:
        global timer
        # Runs the whole function continuously after every second
        timer = window.after(1000, timer_counter, count - 1)
    else:
        # When the timer hits 'zero,' it means it's time to change the app state (Working, Short Break, Long Break)
        # Before calling the call_timer function the app needs to go to the top of the screen
        # So, user know when it's time to a break, or it's time to work
        window.attributes("-topmost", True)

        # After the application comes to the top of the screen, the call_timer function will be executed
        call_timer()


# The function that's control the app's state
def call_timer():
    """
    The interval periods of this app

    1: 25 minutes of work,
    2: 5-minute break,
    3: 25 minutes of work,
    4: 5-minute break,
    5: 25 minutes of work,
    6: 5-minute break,
    7: 25 minutes of work,
    8: 20 minutes of long break

    """

    global loop_time, check_marks

    #  Keep track of how many times this function called
    loop_time += 1
    # Removed always on top status from app, So user can use another app without distracted from with this app's window
    window.attributes("-topmost", False)

    # Check whether this function called for the first time, If that's the case, the Start button will be disabled and the reset button will be enabled
    if _started:
        toggle_reset_btn()
        toggle_start_btn()

    # If this function runs 8 times, It means it's time for a long break
    if loop_time == 8:
        timer_counter(LONG_BREAK_SEC)
        change_color(YELLOW)
        # Reset the checkmark variable to default
        check_marks = ''
        header_text.config(text="Take a Long Break!")

    #  All the loop time numbers for a short break are odd value, So this will check whether its odd and set app's state to short Break
    elif loop_time % 2 == 0:
        timer_counter(SMALL_BREAK_SEC)
        change_color(PURPLE)
        header_text.config(text="Take a Little Break!")

    #  All the loop time numbers for a Working time are even value, So this will check whether its even and set app's state to working
    elif loop_time % 2 == 1:
        timer_counter(WORKING_TIME_SEC)
        change_color(GREEN)
        header_text.config(text="Stay Focused!")
        # this will update the checkmark variable every working state and display its value
        check_marks += '🔥'  # ✔
        checkmark_label.config(text=check_marks)


#  Reset app to its original
def reset():
    global loop_time, check_marks, timer_text, timer

    # Disable the timer
    window.after_cancel(timer)

    # Enable the start button and disable the reset button, So user can't spam it :)
    toggle_reset_btn()
    toggle_start_btn()

    # Reset all elements to their initial state
    header_text.config(text="Ready to Focus?")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    change_color(BLUE)

    # Change the variable that's control the app state, So user can start the app normally again
    loop_time = 0
    check_marks = ""


# Disable the button if its enabled, If not disabling it
def toggle_start_btn():
    global _started
    if _started:
        start_btn.config(state="disabled", bg='white', text="Started")
        _started = False
    else:
        start_btn.config(state="normal", bg=PINK, fg='white', text="Start")
        _started = True


def toggle_reset_btn():
    global _started
    if _started:
        reset_btn.config(state="normal", bg=PINK, fg='white')
    else:
        reset_btn.config(state="disabled", bg='white')


# Change every element's color to the given color when it called
def change_color(color):
    window.config(bg=color)
    canvas.config(bg=color)
    header_text.config(bg=color)
    checkmark_label.config(bg=color)


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
header_text.config(font=(TEXT_FONT_NAME, 20), bg=BLUE, )
header_text.grid(row=0, column=0, columnspan=2)

canvas = Canvas()
canvas.config(bg=BLUE, width=250, height=224, highlightthickness=0)
TOMATO_IMAGE = PhotoImage(file="./assets/tomato.png")
canvas.create_image(125, 112, image=TOMATO_IMAGE)
timer_text = canvas.create_text(125, 130, text="00:00", font=(TEXT_FONT_NAME, 36), fill="white")
canvas.grid(row=1, column=0, columnspan=2)

checkmark_label = Label(text="")
checkmark_label.config(font=(TEXT_FONT_NAME, 18), bg=BLUE, fg=CHECKMARK_COLOR)
checkmark_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

start_btn = Button(text="Start")
start_btn.config(width=10, height=1, font=(TEXT_FONT_NAME, 18), bg=PINK, fg='white', activebackground=DARK_PINK,
                 activeforeground='white', command=call_timer)
start_btn.grid(row=3, column=0, padx=5, pady=10)

reset_btn = Button(text="Reset")
reset_btn.config(width=10, height=1, font=(TEXT_FONT_NAME, 18), fg='white', activebackground=DARK_PINK,
                 activeforeground='white', command=reset, state="disabled", bg='white')
reset_btn.grid(row=3, column=1, padx=5, pady=10)

window.mainloop()
