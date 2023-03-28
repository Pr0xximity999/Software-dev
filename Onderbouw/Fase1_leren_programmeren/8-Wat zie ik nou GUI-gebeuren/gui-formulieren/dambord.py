from tkinter import *

window = Tk()
window.geometry('480x510')
window.resizable(0,0)

for i in range(10):
    for x in range(10):
        if not i % 2:
            if not x % 2: tile = Label(window, bg='black')
            else: tile = Label(window, bg='white')
        if i % 2:
            if not x % 2: tile = Label(window, bg='white')
            else: tile = Label(window, bg='black')
        tile.grid(column=i, row=x)
        tile.configure(width=6, height=3)

window.mainloop()