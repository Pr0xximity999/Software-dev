from string import ascii_lowercase
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Spinbox
import random


#Initialize the window size, background color and makes it unresizable
window = Tk()
window.geometry('600x400')
window.configure(bg='white')
window.resizable(0,0)

points = 0

theWord = StringVar(window)

def guess():
    global spinboxes, points
    guessed = True
    falseLetters = 0
    for i in range(len(theWord.get())):
        if theWord.get()[i] != spinboxes[i].get():
            falseLetters += 1
            guessed = False
    if guessed:
        messagebox.showwarning('You won!', 'Congrats, you won!')
        if messagebox.askyesno('Retry?', 'Do you want to play again?'):
            theWord.set('')
            clearScreen()
            setup()
        else:
            window.destroy()
    else:
        messagebox.showwarning('Wrong awnser!', f'Please try again, \nyou had {falseLetters} letters wrong\nyou lost {falseLetters} points')
        points -= falseLetters
        if points <= 0:
            messagebox.showwarning('You lost!', 'Too bad!')
            if messagebox.askyesno('Retry?', 'Do you want to play again?'):
                theWord.set('')
                clearScreen()
                setup()
                return
        updateScore()

def clearScreen():
    whiteBlock = Label(window, bg='white')
    whiteBlock.pack()
    whiteBlock.place(relwidth=1,relheight=1)

def updateScore():
    global pointLabel
    pointLabel.configure(text=f'Points: {points}')

def start():
    global points, pointLabel, spinboxes
    clearScreen()

    #Makes the stringvars for the spinboxes
    spinboxes = []
    #Places all the spinboxes
    wordLen = len(theWord.get())
    for i in range(wordLen): 
        ranNum = random.randint(0, 3)
        spinboxsv = StringVar(window)
        spinboxes.append(spinboxsv)
        sb = Spinbox(   
                    window,
                    values=[theWord.get()[i] if x == ranNum else random.choice(ascii_lowercase) for x in range(4)], 
                    textvariable=spinboxsv, 
                    wrap=True, 
                    font=(20))
        sb.configure(state='readonly')
        sb.place(relheight=0.2, relwidth=0.9 / wordLen , rely=0.4, relx=0.025 + (0.95 / wordLen * i))

    points = wordLen * wordLen
    pointLabel = Label(window, text=f'Points: {points}', font=(20), bg='white')
    pointLabel.pack()
    pointLabel.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.2)

    guessBtn = Button(window, text='Guess', command=guess)
    guessBtn.pack()
    guessBtn.place(relwidth=0.2, relheight=0.1, relx=0.4, rely=0.8)


def setup():
    #Initializes the start screen labels, entry, and stringvar
    global theWord, startLabelBottom
    startLabelTop = Label(window, text='Enter a word', bg='white', font=(30))
    startLabelTop.pack()
    startLabelTop.place(relwidth=0.4, relx=0.3, rely=0.05)

    theWord.trace('w', updateStart)

    startEntry = Entry(window, textvariable=theWord)
    startEntry.pack()
    startEntry.place(relwidth=0.5, relx=0.25, rely=0.4)

    startLabelBottom = Label(window, text='4 - 7 letters required', bg='white')
    startLabelBottom.pack()
    startLabelBottom.place(relwidth=0.4, relx=0.3, rely=0.6)

    startButton = Button(window, text='start', command=startCheck)
    startButton.pack()
    startButton.place(relwidth=0.1, relx=0.45, rely=0.8)

#Updates the number of letters on the start screen
def updateStart(arg1='', arg2='', arg3=''):
    global startLabelBottom, theWord
    startLabelBottom.configure(text=f'{len(theWord.get())} letters')

#Checks if the given word is valid(4-7 words and only letters)
def startCheck():
    global theWord
    if len(theWord.get()) < 4 or len(theWord.get()) > 7:
        messagebox.showerror('Invalid option', 'Please use 4 to 7 letters')
        setup()
        return
    else:
        for i in theWord.get():
            onlyletters = True
            if not i in ascii_lowercase:
                onlyletters = False
        if not onlyletters:
            messagebox.showerror('Invalid option', 'Please only use letters')
            setup()
            return
        else:
            theWord.set(theWord.get().lower())
            start()

setup()
window.mainloop()