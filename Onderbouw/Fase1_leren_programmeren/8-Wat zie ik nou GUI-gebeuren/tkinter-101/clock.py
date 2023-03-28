import tkinter
from time import *


window = tkinter.Tk()
window.configure(bg="black")

window.geometry("400x200")
textbox = tkinter.Label(window, bg="black",  fg="dark Grey", font=("Helvetica",75))
textbox.pack(side="top", pady=30)

def clock():
    global textbox
    textbox.config(text=strftime("%H:%M:%S"))
    textbox.after(100, clock)

clock()


window.mainloop()