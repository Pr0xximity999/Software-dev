import tkinter as tk
import os
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
    if not os.path.exists('actions.log'):
        with open('actions.log', 'w') as file:
            file.write(f'The light has been turned {buttonstates[0]}\n')
    else:
        with open('actions.log', 'a') as file:
            file.write(f'The light has been turned {buttonstates[0]}\n')
    button.config(text=f"Turn the screen {buttonstates[1]}")
    window.config(bg=screenstates[0])

#Pre-Defines the background and the button
window.config(bg=screenstates[0])
button.config(text=f"Turn the screen {buttonstates[1]}",command=updateState)


# schijf hier tussen je code

window.mainloop()