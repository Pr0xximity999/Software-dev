import tkinter

window = tkinter.Tk()

window.title("hello")
window.geometry("150x100")
window.configure(bg= "dark blue")
btn = tkinter.Button(text="Hello tkinter!", bg="green", fg="purple")    

btn.pack(
    ipadx=10,
    ipady=10,
    expand = True
)

window.mainloop()