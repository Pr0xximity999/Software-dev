from cProfile import label
from cgitb import text
from glob import glob
from tkinter import *
import random
from tkinter import font

keys = ['w', 'a', 's', 'd', 'space', 'Button-1', 'Double-Button-1', 'Triple-Button-1']
chosenkey = ''
done = False
window = Tk()
window.geometry('600x400')
startBtn = Button() 
tempBtn = Button()
retryBg = Button()
retryBgText = Button
retryYesBtn = Button()
retryNoBtn = Button()
time = 20
score = 0

#The top color bar
topColor = Label(window, bg='grey')
topColor.pack()
topColor.place(relwidth=1, relheight=0.1)

#The timer
timer = Label(window,bg = 'grey', fg='white', text=f'Time remaining: {time}', font=(20))
timer.pack()
timer.place(relx = 0.05, relwidth=0.3, relheight=0.1)

#The points
points = Label(window,bg = 'grey', fg='white', text=f'Points: {score}', font=(20))
points.pack()
points.place(relx = 0.7, relwidth=0.3, relheight=0.1)

def restart():
    global time, score, retryBg, retryBgText, retryYesBtn, retryNoBtn, tempBtn, timer, points, done
    retryBg.destroy()
    retryBgText.destroy()
    retryYesBtn.destroy()
    retryNoBtn.destroy()
    tempBtn.destroy()
    time = 20
    timer.configure(text=f'Time remaining: {time}')
    score = 0
    done = False
    setup()

#Asks if the user wants to retry
def retryprompt():
    global score, retryBg, retryBgText, retryYesBtn, retryNoBtn
    #The background color
    retryBg = Label(window, bg='teal')
    retryBg.pack()
    retryBg.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)

    #The text
    retryBgText = Label(window, bg='teal', fg='white', text=f'Points: {score} \nRetry?', font=(30))
    retryBgText.pack()
    retryBgText.place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.1)

    #The Yes button
    retryYesBtn = Button(text='yes', command=restart)
    retryYesBtn.pack()
    retryYesBtn.place(relx=0.3, rely=0.4, relwidth=0.15, relheight=0.1)

    #The No button
    retryNoBtn = Button(text='no',command=exit)
    retryNoBtn.pack()
    retryNoBtn.place(relx=0.6, rely=0.4, relwidth=0.15, relheight=0.1)

#The countdown 
def countDown():
    global time, done, timer
    if time > 0:
        time -= 1
        timer.configure(text=f'Time remaining: {time}')
        window.after(1000, countDown)
    else:
        retryprompt()
        done = True
        return

#Unbinds the keys
def update(event=''):
    global chosenKey, score, points
    if chosenKey in 'wasdspace':
        score += 1
        window.unbind(f'<{chosenKey}>')
    else:
        score += 2
        tempBtn.unbind(f'<{chosenKey}>')
    if done:
        return
    points.configure(text=f'Points: {score}')
    placeBtn()

#Places a new button at a new location with a new requirement
def placeBtn():
    global tempBtn, chosenKey, tempBtn
    if done:
        update()
        return
    ranX = random.randint(20, 80) / 100
    ranY = random.randint(10, 70) / 100

    chosenKey = random.choice(keys)
    formattedKey = chosenKey.replace('-', ' ') 
    formattedKey = formattedKey.replace('Button 1', 'click me')
    tempBtn.pack()
    tempBtn.place(relx=ranX, rely=ranY, relwidth=0.15, relheight=0.1)

    if chosenKey in 'wasdspace':
        tempBtn.configure(text=f'Press {formattedKey}')
        window.bind(f'<{chosenKey}>', update)
    else:
        tempBtn.configure(text=f'{formattedKey}')
        tempBtn.bind(f'<{chosenKey}>', update)

#Destroys the start button and calls the random button
def start():
    global startBtn
    startBtn.destroy()
    placeBtn()
    countDown()

#Starting setup
def setup():
    global startBtn, tempBtn
    tempBtn = Button()
    startBtn = Button(text='Click to start', command=start)
    startBtn.pack()
    startBtn.place(relx=0.40, rely=0.5, relwidth=0.15, relheight=0.1)


setup()
window.mainloop()