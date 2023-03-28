from random import choice, shuffle
from tkinter import *

items = "scooter-car-playstation-bomb-nuke-grenade-tv-candy cane-waterpistol-tsar bomba-a spotify subscription-a girlfriend"

itemList = items.split('-')
shuffle(itemList)


def grabbel():
    global itemList, text
    if not itemList:
        text.configure(text = '[Box is empty]')
        return
    text.configure(text= 
    f'''congrats, you won a: \n{itemList.pop(0)}''')


window = Tk()
window.configure(bg='white')
window.geometry('400x300')

text = Label(window, text='', bg='white', font=("Helvetica", 30))
text.pack()
text.place(relx=0.5, rely=0.2, anchor=CENTER) 

btn = Button(text="grabbelen", width=100, height=6, command=grabbel)
btn.pack() 
btn.place(relx=0.5, rely=0.85, anchor=CENTER)    


window.mainloop()