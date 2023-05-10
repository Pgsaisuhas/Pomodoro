import tkinter as tk
import customtkinter as ctk
import notification

# ----------------------------------------------- Constants -------------------------------------------------- #

FONT_NAME = "Arial"
GREEN = "#6ab04c"
RED = "#e7305b"
PINK = "#f7a8b8"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0

# ----------------------------------------------- Variables -------------------------------------------------- #

timer = None
marks = ""


# ----------------------------------------------- Functions -------------------------------------------------- #

def start_timer():  # start timer from 25:00, new session
    global REPS, marks
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_sec)
        TIMER_LABEL.configure(text="BREAK", text_color=PINK)
        notification.notify_long()
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        TIMER_LABEL.configure(text="BREAK", text_color=RED)
        notification.notify_short()
    else:
        count_down(work_sec)
        TIMER_LABEL.configure(text="WORK", text_color=GREEN)
        notification.notify_work()
    marks = "✔" * (REPS // 2)
    check_mark.configure(text=marks)


def reset_timer():  # reset timer to 00:00
    global REPS, timer, marks
    REPS = 0
    marks = ""
    check_mark.configure(text=marks)
    TIMER_LABEL.configure(text="TIMER", text_color=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    if timer:
        window.after_cancel(timer)
        timer = None


def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text="{:02d}:{:02d}".format(count_min, count_sec))
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()


# ----------------------------------------------- UI Setup --------------------------------------------------- #
window = ctk.CTk()
window.title("POMODORO")
window.config(padx=10, pady=10)
window.geometry("425x425")
window.maxsize(width=425, height=425)

canvas = tk.Canvas(width=200, height=250, bg="#242423", highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_image)
timer_text = canvas.create_text(105, 112, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1, padx=15, pady=15)

TIMER_LABEL = ctk.CTkLabel(master=window, text="TIMER", text_color=GREEN, font=(FONT_NAME, 40, "bold"))
TIMER_LABEL.grid(row=0, column=1, padx=15, pady=15)

start_button = ctk.CTkButton(master=window, text="Start", width=100, border_width=2, border_color="White",
                             corner_radius=10, command=start_timer)
start_button.grid(row=2, column=0, padx=5)

reset_button = ctk.CTkButton(master=window, text="Reset", width=100, border_width=2, border_color="White",
                             corner_radius=10, command=reset_timer)
reset_button.grid(row=2, column=3, padx=5)

check_mark = ctk.CTkLabel(master=window, text=marks, font=(FONT_NAME, 18, "bold"), bg_color="#242423", pady=35)
check_mark.grid(row=3, column=1)

window.mainloop()
