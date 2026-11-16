import tkinter
from tkinter import simpledialog
from datetime import datetime, time 

def get_team_name():
    team_name = simpledialog.askstring(
    "Team Name",
    "Enter your team name:"
    )
    team_name += " (Assiut)"
    return team_name

# create a team name on screen
def create_label_for_name(screen, name):
    team_name_label = tkinter.Label(
        screen, 
        text = name,
        fg = "white",
        bg = "black",
        font = ("Arial", 30))

    team_name_label.place(relx = 0.49, rely = 0.85, anchor="center") # (740, 720)

def get_data(date):
    [hours, minutes, seconds] = [0, 0, 0]
    if date > 0:
        hours = date // (60 * 60)
        data = date % (60 * 60)
        minutes = data // 60
        seconds = data % 60 
    return [int(hours), int(minutes), int(seconds)]

def fix(n):
    ret = ""
    if n < 10:
        ret += "0"
    ret += str(n)
    return ret

def update_time(screen, timer, timer_label):
    [hours, minutes, seconds] = get_data(timer)

    timer_label.config(text=f'- {fix(hours)}:{fix(minutes)}:{fix(seconds)}')
    if seconds == 0 and minutes == 0 and hours == 0:
        screen.destroy()
    
    screen.after(1000, update_time, screen, timer - 1, timer_label)

# make an interface
screen = tkinter.Tk()

screen.title("Welcome to ACPC")
screen.geometry("1550x850")

background = tkinter.PhotoImage(file = "background1.png")
background_label = tkinter.Label(screen, image = background)
background_label.pack()

create_label_for_name(screen, get_team_name())

final_time = simpledialog.askstring(
    "Contest time",
    "What time does the contest start? (HH:MM)"
)
final_time = datetime.strptime(final_time, "%H:%M")
final_time = final_time.replace(
    year = datetime.now().year,
    month = datetime.now().month,
    day = datetime.now().day
)

timer = int((final_time - datetime.now()).total_seconds())

timer_label = tkinter.Label(
    screen,
    fg = "white",
    bg = "black",
    font = ("Arial", 70) 
    )
timer_label.place(relx=0.47, rely=0.06, anchor="center")

update_time(screen, timer, timer_label)
screen.mainloop()