import tkinter
from time import sleep
colors = ["white", "yellow", "orange", "red", "purple", "black"]
window = tkinter.Tk()

window.geometry("50x50")
for i in range(1, 8):
    sleep(2)
    if i == 7:
        print("Boom!")
        window.destroy()
        break
    size = str(f"{50 * i}x{50 * i}")
    window.configure(bg = colors[i - 1])
    window.geometry(size)
    print(f"{7 - i}")
    window.update()

window.mainloop()