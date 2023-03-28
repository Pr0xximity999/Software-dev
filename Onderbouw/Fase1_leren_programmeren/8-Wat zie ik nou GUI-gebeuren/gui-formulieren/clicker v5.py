from tkinter import *
from time import sleep

UpLastPressed = False
DownLastPressed = False
autoclicker = False

num = 0
window = Tk()
window.configure(bg='grey')
window.title('Clicker')
window.geometry('250x250')


#updates the background and text
def update(event=''):
    global text, window, num, checkBox, checkBox
    text.configure(text="%.0f" %num)

    #Updates the background depending on the number's value
    color = ''
    if num == 0:
        color = 'grey'
    elif num > 0:
        color = 'green'
    else:
        color = 'red'
    checkBox.configure(bg=color)
    window.configure(bg=color)
    checkBox.update()

#Some event functions
def yellow(event=''):
    global checkBox
    checkBox.configure(bg='yellow')
    window.configure(bg='yellow')

def tripleOrNah(event=''):
    global num, UpLastPressed, DownLastPressed
    if UpLastPressed:
        num *= 3
    if DownLastPressed:
        num /= 3
    update()


#The functions for handling the increment and decrement of the on screen number
def increment(event=''):
    global num, UpLastPressed, DownLastPressed, checkBox
    checkBox.configure(state='active', bg='green')
    UpLastPressed = True
    DownLastPressed = False
    num += 1
    update()

def decrement(event=''):
    global num, UpLastPressed, DownLastPressed, checkBox
    checkBox.configure(state='active', bg='red')
    UpLastPressed = False
    DownLastPressed = True
    num -= 1
    update()

def autoClicker():
    global autoclicker, UpLastPressed, DownLastPressed
    
    if not autoclicker:
        autoclicker = True
        while autoclicker:
            if UpLastPressed:
                sleep(0.2)
                increment()
            elif DownLastPressed:
                sleep(0.2)
                decrement()
            
    elif autoclicker:
        autoclicker = False


#Sets up the top and bottom button, the checkbox and the number

checkBox = Checkbutton(window, text='Autoclicker', bg='grey', state='disabled', command=autoClicker)
checkBox.pack()
checkBox.place(relx=0.5, rely=0.1, anchor=CENTER, relwidth=0.4, relheight=0.1)

upBtn = Button(text="up", command=increment)
upBtn.pack() 
upBtn.place(relx=0.5, rely=0.25, anchor=CENTER, relwidth=0.95, relheight=0.15)    

text = Label(window, text=num, font=("Helvetica", 20))
text.pack()
text.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.95, relheight=0.15) 

downBtn = Button(text="down", command=decrement)
downBtn.pack() 
downBtn.place(relx=0.5, rely=0.8, anchor=CENTER, relwidth=0.95, relheight=0.15)  

#Label events
text.bind('<Double-Button-1>', tripleOrNah)
text.bind('<Enter>', yellow)
text.bind('<Leave>', update)

#Window event
window.bind('<Up>', increment)
window.bind('<+>', increment)
window.bind('<Down>', decrement)
window.bind('-', decrement)
window.bind('<space>', tripleOrNah)

window.mainloop()