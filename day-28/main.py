from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    count_down(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



timer = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 25,"bold"), bg=YELLOW)
timer.grid(column=1, row=0)

start = Button(text="Start", bg=GREEN, fg="white", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=GREEN, fg="white")
reset.grid(column=2, row=2)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)

canvas = Canvas(width=200, height= 224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)







window.mainloop()