import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

#Defines the state of the color of the background and the text of the button
buttonstates = ["off", "on"]
screenstates = ["black", "yellow"]

def updateState():#Updates the text of the button and the color of the background
    global buttonstates, screenstates, button
    buttonstates.reverse()
    screenstates.reverse()  
    print(f'the screen is {buttonstates[0]}')
    button.config(text=f"Turn the screen {buttonstates[1]}")
    window.config(bg=screenstates[0])

#Pre-Defines the background and the button
window.config(bg=screenstates[0])
button.config(text=f"Turn the screen {buttonstates[1]}",command=updateState)


# schijf hier tussen je code

window.mainloop()