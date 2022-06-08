from datetime import datetime
from tkinter import *
import screen_brightness_control as sbc
import random
from winsound import PlaySound, SND_FILENAME, SND_ASYNC, SND_LOOP, SND_PURGE
import os
import winsound

MAX_FREQUENCY = 15000  # Максимальная частота звука 2500Гц
MIN_FREQUENCY = 2000 

def on_five_minute(endTime):
    message = 'До судного дня: \n' + str(endTime)
    label1.config(text=message)
    width_random = random.randint(450, 1200)
    height_random = random.randint(150, 1500)
    size=str(width_random) + "x" +str(height_random)
    root.geometry(size)
    
    

def schedule():
    now_time = datetime.now()
    delta = deadDay - now_time
    on_five_minute(delta)
    root.after(100, changeBrightness)
    root.after(100, degenerate)
    root.after(100, schedule)

def changeBrightness():
    bright = random.randint(0, 100)
    sbc.set_brightness(bright)

def degenerate():
    frequency = random.randint(MIN_FREQUENCY, MAX_FREQUENCY)
    duration = random.randint(10, 50)
    winsound.Beep(frequency, duration)

#PlaySound("C:/Users/user/Desktop/Death2.wav", SND_FILENAME | SND_LOOP | SND_ASYNC)
#os.system('wget -O http://example.com/path/to/audio | aplay')
deadDay = datetime.strptime("02/06/22 10:30", "%d/%m/%y %H:%M")
root = Tk()
root.title("Я наблюдаю за тобой снаружи всех измерений...")
root.geometry("450x200")
root.configure(bg="black")
label1 = Label(fg = "red", bg ="black", font="Times 30")
label1.pack()
schedule()
root.mainloop()
