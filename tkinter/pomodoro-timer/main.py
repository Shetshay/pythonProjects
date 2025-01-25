from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    check_marks.config(text="", bg = YELLOW)
    canvas.itemconfig(timer_text, text=f"{"00"}:{"00"}")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        title_label.config(text="Work", fg=GREEN)
        #print(reps)
        work_session = math.floor(reps/2) # every two reps (work / break) = 1 work session
        emoji = ""
        for _ in range(work_session): # for every work session we add an emoji to show completion
            emoji += "✔" # override what emoji is and replace it with correct amount of emojis per session completion
        check_marks.config(text=f"{emoji}") # edit the screen to update the effect


    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60) # 60 seconds in one minute
    count_sec = count % 60 # grab remainder of 60
    if count_sec == 0: # if the second is exactly equal to 0
        count_sec = "00" # make it visually equal to 00 instead of just 0 on the screen
    elif count_sec > 9: # if the seconds is less than 9 skip the else statement below
        pass
    else:
        count_sec = f"0{count_sec}" # if count is greater than 9 add 0 in front of the seconds to give it analog effect
    if count_min < 10:
        count_min = f"0{count_min}" # if count minute is less than 10, so single digits will also have the analog effect

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # show minutes and seconds on screen
    if count > 0: # if its over 0 seconds
        global timer
        timer = window.after(1000, count_down, count - 1) # every 1000 milliseconds (1 second) count - 1
        # call count_down() function
    else:
        start_timer() # if count is less than 0 (so the current timer is complete) start again

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=2 , row=1 )
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

#Labels
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))

title_label.grid(column=2 , row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0 , row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3 , row=3)

check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(column=2, row=3)

window.mainloop()