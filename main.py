from tkinter import *
import time
from playsound import playsound


global time_text 
global outputString
global t
t = 3600

def Refresh():
    global t, mins, secs
    if (t == 0):
        playsound("content/omg.mp3")
        t = 3600
    t -= 1
    mins, secs = divmod(t, 60)
    outputString = '{:02d}:{:02d}'.format(mins, secs)
    time_text.configure(text= outputString)
    main.after(1000, Refresh)

main = Tk()
main.title("BreakTime")

main.geometry("800x500")
start_time = time.time()
mins, secs = divmod(t, 60)
outputString = '{:02d}:{:02d}'.format(mins, secs)
label_text = Label(main, text="Break Time Timer", font=('Arial', 20))
label_text.pack(padx = 10, pady = 20)
time_text = Label(main, text = outputString, font=('Arial', 100))


time_text.pack(padx = 0, pady = 100)



Refresh()
main.mainloop()