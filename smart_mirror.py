from tkinter import *
from tkinter.messagebox import *
from bs import current_forcast
import time
import datetime

#settings
background_color="black"
font_color="white"
greeting = "Welcome: Miles Olson"
weather = "77 Degrees"
current_time = "2:22"
#variables
fullscreen_state = False
last_weather_update= ''
time1 = ''
date1 = ''
last_weather_number = ''
last_weather_words = ''

class keybinds:
    def toggle_fullscreen(self, event=None):
        global fullscreen_state
        if fullscreen_state == False:
            fullscreen_state = True
            root.wm_attributes('-fullscreen','true')
        else:
            fullscreen_state = False
            root.wm_attributes('-fullscreen','false')
    def end_program(self, event=None):
        quit()

def update():
    """This runs every seconds to update the program"""
    global time1
    global date1
    global last_weather_update
    time2 = time.strftime('%I:%M:%S %p')
    date2 = time.strftime('%x')
    if date2 != date1:
        date1 = date2
        thedate.config(text=date2)
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        #Track the last time their was a weather update and set it to current time
    clock.after(1, update)

def updateweather():
    global last_weather_words
    global last_weather_number
    new_weather_number = current_forcast.current_number_numbers()
    new_weather_words = current_forcast.current_weather_words()

    if last_weather_words != new_weather_words:
        last_weather_words = new_weather_words
        weather_words.config(text=new_weather_words)
    if last_weather_number != new_weather_number:
        last_weather_number = new_weather_number
        weather_number.config(text=new_weather_number)
    weather_number.after(1,update)




root = Tk()
root.option_add('*font', ('verdana', 22, 'bold'))
root.title("Smartmirror")
root.geometry("800x500")


row_1 = Frame(root)
Label(row_1, text=greeting, bg='black',foreground='white', font=('elianto', 40)).pack(side=TOP, fill=BOTH, expand=1)
row_1.pack(fill=BOTH)

row_2= Frame(root)
row_2.configure(bg='black')
weather_number = Label(row_2, text='',bg='black',foreground='white', font=('elianto', 40))
weather_number.pack(side=LEFT, fill=X, expand=1)
clock = Label(row_2, text="", bg='black',foreground='white', font=('elianto', 100))
clock.pack(side=RIGHT, fill=X, expand=1)
row_2.pack(fill=X)

row_3= Frame(root)
weather_words=Label(row_3, text=last_weather_words, bg='black',foreground='white', font=('elianto', 30))
weather_words.pack(side=LEFT, fill=BOTH, expand=1)
thedate = Label(row_3, text='12/2/2019', bg='black',foreground='white', font=('elianto', 40))
thedate.pack(side=RIGHT, fill=X, expand=1)
row_3.pack(fill=X)

row_blank= Frame(root)
Label(row_blank, text='', bg='black',foreground='white', font=('elianto', 40)).pack(side=LEFT, fill=BOTH, expand=1)
row_blank.pack(fill=BOTH, expand=1)

row_last = Frame(root)
Label(row_last, text='Press SPACE to toggle fullscreen, Press q to quit. ', bg='black',foreground='white', pady = 10, font=('elianto', 20)).pack(side=LEFT, fill=BOTH, expand=1)
row_last.pack(fill=BOTH)

root.bind("<space>", keybinds.toggle_fullscreen)
root.bind("<q>", keybinds.end_program)
updateweather()
update()
root.mainloop()
