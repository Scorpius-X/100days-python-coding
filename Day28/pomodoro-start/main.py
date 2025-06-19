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
reps = 1
test= "✓"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    windows.after_cancel(timer)
    timer_label.config(text= "Timer", fg= GREEN, font= (FONT_NAME,35, "bold"), bg= YELLOW)
    check_mark.config(text= "")
    canvas.itemconfig(timer_text, text = "00:00")
    reps = -1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if reps < 9:
        if reps % 2 != 0:
            timer_label.config(text= "WORK", fg= GREEN)
            print("work")
            count_down(work_sec)
        elif reps == 8:
            timer_label.config(text= "BREAK", fg= RED)
            print("long break")
            count_down(long_break)
        else:
            timer_label.config(text= "BREAK", fg= PINK)
            print("short break")
            count_down(short_break)

        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        check_session = math.floor(reps/2)

        for _ in range(check_session):
            marks += test
        check_mark.config(text= marks)
# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(padx= 100, pady= 50, bg= YELLOW)

# create a canvas  to store the image graphics
canvas = Canvas(width= 200, height= 224, bg = YELLOW, highlightthickness= 0)

#save the photoimage in a variable
tomato_img = PhotoImage(file= "100days-python-coding/Day28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text= "00:00", fill= "white" ,font=(FONT_NAME, 35, "bold"))
canvas.grid(column= 1, row= 1)

timer_label = Label(text= "Timer", font= (FONT_NAME, 35, "bold"), bg= YELLOW )
timer_label.grid(column= 1, row= 0)
timer_label.config(fg= GREEN)

start = Button(text= "start", command= start_timer)
start.grid(column = 0, row = 2)
reset = Button(text= "reset", command= reset_timer)
reset.grid(column = 2, row = 2)

check_mark = Label(fg= GREEN,  bg= YELLOW)
check_mark.grid(column = 1, row= 2)
check_mark.config( pady= 20)





windows.mainloop()