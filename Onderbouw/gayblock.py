from cProfile import label
from tkinter import *
from tkinter import messagebox

def gay(event):
    messagebox.showwarning('GAY', 'you now have the gay')

def unGay(event):
    messagebox.showwarning('NO MORE GAY', 'you now have the yag')

window = Tk()
window.geometry('1000x1000')
text = Label(window, text="Gay", bg='dark grey')
text.pack()
text.place(relx=0.5, rely=0.5, anchor=CENTER) 

text.bind('<Enter>', gay)
window.bind('<Control_L><g><a><y>', unGay)

window.mainloop()