import os
import json
from tkinter import *
import random
from tkinter.messagebox import showinfo, showwarning

keys = ['w', 'a', 's', 'd', 'space', 'Button-1', 'Double-Button-1', 'Triple-Button-1']
chosenkey = ''
done = False
window = Tk()
window.geometry('600x400')
entrySV = StringVar()
board = ''
dialog = ''
startBtn = Button() 
tempBtn = Button()
retryBg = Button()
retryBgText = Button
retryYesBtn = Button()
retryNoBtn = Button()
time = 2
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

def restart(arg=''):
    global board, time, done, score, tempBtn
    score = 0
    done = False
    time = 20
    board.destroy()
    tempBtn.destroy()
    setup()


def leaderBoard(): #displays the highscores and the corresponding playername
    global board
    board = Toplevel()
    board.geometry('200x300')
    names = []
    scores = []
    with open('highscores.json', 'r') as file:
        data = json.load(file)

        for name in data['name']:
            names.append(name)
        for score in data['highscore']:
            scores.append(score)

    for i in range(len(names)): #places the names and scores onto the scoreboard
        lbl = Label(board, text=f'#{i + 1}')
        lbl.place(relx=0.05, rely=i / 12, relwidth=0.1, relheight=0.1)
        lbl = Label(board, text=f'{names[i]}: {scores[i]} points')
        lbl.place(relx= 0.15, rely=i / 12, relwidth=0.85, relheight=0.1)
    exitbtn = Button(board, text='exit', command=window.destroy)
    exitbtn.place(relx=0.05, rely=0.85, relwidth=0.2, relheight=0.1)
    retrybtn = Button(board, text='retry', command=restart)
    retrybtn.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.1)


def save():
    global newname, entrySV, dialog
    dialog.destroy()
    newname = entrySV.get().lower()
    highscore = []
    name = []
    with open('highscores.json', 'r') as file:
        data = json.load(file)
        if data['name'][0] != 'Placeholder':
            highscore, name = data['highscore'], data['name']
        if len(name) == 10:
            highscore.pop(0)
            name.pop(0)
        highscore.append(score)
        name.append(newname)
        highscore.reverse()
        name.reverse()
    
    with open('highscores.json', 'w') as file:
        file.write(json.dumps({
            'highscore' : highscore,
            'name' : name
            }))
    leaderBoard()


def entryPrompt(title, question, continueFunc=''): #A function for making entry prompts
    global newname, entrySV, dialog
    dialog = Toplevel(window, name=title.lower())
    dialog.geometry('200x100')
    dialog.resizable(0,0)
    textBox = Label(dialog, text=question)
    textBox.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)
    entrySV = StringVar()
    input = Entry(dialog, textvariable=entrySV)
    input.place(relx=0.2, rely=0.60, relwidth=0.6, relheight=0.2)
    btn = Button(dialog, text='confirm', command=continueFunc)
    btn.place(relx=0.65, rely=0.85, relwidth=0.3, relheight=0.2)

    

#Asks if the user wants to retry
def checkScore():
    global score, retryBgText, retryYesBtn, retryNoBtn
    update()
    if not os.path.exists('highscores.json'):
        with open('highscores.json', 'w') as file:
            file.write(json.dumps({
                "highscore" : [-1],
                "name" : ['Placeholder']
                }))

    with open('highscores.json', 'r') as file:
        highscore = json.load(file)['highscore']

    if score > highscore[-1]:
        showwarning('Congrats', 'New highscore!')
        entryPrompt('Enter name', 'Enter your name', save)
    else:
        leaderBoard()

#The countdown 
def countDown():
    global time, done, timer
    if time > 0:
        time -= 1
        timer.configure(text=f'Time remaining: {time}')
        window.after(1000, countDown)
    else:
        checkScore()
        done = True
        return

#Unbinds the keys
def update(event=''):
    global chosenKey, score, points, done, tempBtn
    if not done:
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

    tempBtn.pack()
    tempBtn.place(relx=ranX, rely=ranY, relwidth=0.15, relheight=0.1)

    chosenKey = random.choice(keys)
    formattedKey = chosenKey.replace('-', ' ') 
    formattedKey = formattedKey.replace('Button 1', 'click me')
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