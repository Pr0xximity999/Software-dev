from logging import exception
from string import ascii_lowercase, ascii_uppercase
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Combobox
from random import randint, choice

window = Tk()
window.resizable(0,0)
window.geometry('450x400')
window.title('Registration window')
widgets = {}

showinfo('Welcome', 'Welcome to this registration for the annual gamer convention')
showinfo('Welcome', 'You will need to awnser a few questions before your registration will be accepted')

def dialog(text:str, width:int, height:int, buttonFunc, buttonText:str='ok'):
    dialog = Toplevel(height=height, width=width)
    lbl = Label(dialog, text=text)
    lbl.place(relheight=0.5, relwidth=0.5, relx=0.35, rely=0.35)
    btn = Button(dialog, text=buttonText, command=buttonFunc)
    btn.place(relx=0.8, rely=0.9, relheight=0.1, relwidth=0.2)

selected = False
def tick(arg1='', arg2='', arg3=''):
    global selected
    if widgets[arg1].get() == 'sus':
        showwarning('sussy', 'AMOGUS')
    if widgets['watches anime'].get() == 'yes' and not selected:
        selected = True
        gridAlign(frame2, Entry, 'favourite anime', 'What is your favourite anime')
    


#places a widget on the grid with the correct question and options
def gridAlign(frame:Frame, widget, questionName:str, question:str, options:list=[], afterText:str=''):
    global widgets
    #Defines the current row
    currentRow = frameWidgetCount[frame]
    frameWidgetCount[frame] = frameWidgetCount[frame] + 1

    #Defines the stringvar and question label
    stringV = StringVar(name=questionName)

    #A label just for the spacing
    spaceLbl = Label(frame, width=5)
    spaceLbl.grid(column=1, row=currentRow)

    #The label for the question text
    questionLbl = Label(frame, text=question)
    questionLbl.grid(column=0, row=currentRow, sticky=W, pady=5)

    #The label for the optional text behind the widget
    afterlbl = Label(frame, text=afterText)
    afterlbl.grid(column=4, row=currentRow, sticky=W)

    #Makes the correct widget and places them on the grid
    if widget == Entry:
        widget = Entry(frame, textvariable=stringV)    

    elif widget == Combobox:
        widget = Combobox(frame, values=options, textvariable=stringV, state='readonly')

    elif widget == Spinbox:
        widget = Spinbox(frame, from_=options[0], to=options[-1], textvariable=stringV, state='readonly')

    elif widget == Radiobutton:
        for i in range(len(options)):
            widget = Radiobutton(frame, text=options[i], value=options[i], variable=stringV, tristatevalue='x')
            widget.deselect()
            widget.grid(row=currentRow, column=i + 2, sticky=W)
            widgets.update({questionName: stringV})
        stringV.trace('w', tick)

        return
    
    else:
        raise exception('Choose a valid widget')
            
    #And lastly, adds them to a dictionairy
    widget.grid(column=2, row=currentRow, columnspan=2, sticky=W)
    widgets.update({questionName: stringV})
    stringV.trace('w', tick)
    
    
#The frames for the window
frame1 = Frame(window) 
frame2 = Frame(window)
endframe = Frame(window)

frameList = [frame1, frame2]

frameWidgetCount = {
    frame1  :   0,
    frame2  :   0
}
frameNum = -1
def nextFrame():#Switches aroundthe frames
    global frameNum
    currentframe = frameList[frameNum]
    currentframe.place(relx=1.1, rely=1.1)
    frameNum += 1
    currentframe = frameList[frameNum]
    currentframe.place(relheight=1, relwidth=1, relx=0, rely=0)

def prevFrame():#Switches aroundthe frames
    global frameNum
    currentframe = frameList[frameNum]
    currentframe.place(relx=1.1, rely=1.1)
    frameNum -= 1
    currentframe = frameList[frameNum]
    currentframe.place(relheight=1, relwidth=1, relx=0, rely=0)

def finish():#When the user is finished
    showinfo('loading', 'calculating awnsers...')
    if widgets['country'].get().lower() == 'brazil': #Easter egg
        showerror('hm?', 'well, well, well \nwhat do we have here mh?')
        showerror('oh no', 'oh..')
        showerror('oh no', 'oh no')
        showerror('oh no', 'no no no')
        showerror('oh no', 'NO')
        showerror('oh no', 'BRAZIL?!')
        showerror('oh no', 'NO')
        showerror('go away', 'GET OUT')
        showerror('go away', 'BEGONE')
        exit()
    if widgets['favourite youtuber'].get().lower() == 'dream': #Easter egg No. 2
        showerror('hm?', 'well, well, well \nwhat do we have here mh?')
        showerror('oh no', 'oh..')
        showerror('oh no', 'i see..')
        showerror('oh no', 'dream, you say hm?')
        showerror('oh no', 'NO')
        showerror('oh no', 'go spread your stanning somewhere else')
        showerror('oh no', 'bye bye kiddo')
        exit()
    if widgets['favourite game'].get().lower() == 'gensin impact': #Easter egg No. 3
        showerror('hm?', 'well, well, well \nwhat do we have here mh?')
        showerror('oh no', 'oh..')
        showerror('oh no', 'is that..')
        showerror('oh no', 'g-gensin??')
        showerror('oh no', 'NO')
        showerror('oh no', 'whyy')
        showerror('got em', 'gensin impact?')
        showerror('got em', 'more like, gayshit infact')
        showerror('got em', 'HA!')
        exit()
    
    allowed = True

    for k, v in widgets.items():
        if v.get() == '':
            allowed = False

    if widgets['is gamer'].get().lower() == 'no':
        allowed = False
    if widgets['plays fortnite'].get().lower() == 'yes':
        allowed = False
    elif int(widgets['age'].get()) < 15:
        allowed = False
    elif widgets['watches anime'].get() == 'yes':
            if widgets['favourite anime'].get().lower() == 'jojo':
                allowed = False
    
    showinfo('ok so', 'so, your registration has been...')
    if not allowed:
        showwarning('denied', 'denied due to some of the fields having invalid awnsers')
        showwarning('denied', 'too bad')
        exit()

    else:
        showwarning('accepted', 'accepted. \ngood job and have fun at the conference!')
    row = 0
    for k, v in widgets.items():
        lbl1 = Label(endframe, text=k)
        lbl2 = Label(endframe, text=v.get())

        lbl1.grid(column=0, row=row)
        lbl2.grid(column=1, row=row, sticky=E, padx=100)
        row += 1
    
    codeLbl = Label(endframe)
    code = ''.join([str(randint(0, 9)) if randint(0, 1) else choice(ascii_lowercase) if randint(0, 1)   else choice(ascii_uppercase) for i in range(32)])
    codeLbl.configure(text=f'registration code: {code}')
    codeLbl.grid(columnspan=2, row=row, column= 0)

    endbtn = Button(endframe, text='Exit', command=lambda:exit())
    endbtn.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)
    
    endframe.place(relwidth=1, relheight=1)
        




#Frame 1 stuff
gridAlign(frame1, Entry, 'name', 'What is your name')   #The name question

gridAlign(frame1, Spinbox, 'age', 'How old are you', [0, str('inf')], 'years')   #The age question

gridAlign(frame1, Entry, 'country', 'Where do you live(Country)')   #The country question

gridAlign(frame1, Radiobutton, 'is gamer', 'Are you a gamer', ['yes', 'no'])  #The gamer question

gridAlign(frame1, Radiobutton, 'plays fortnite', 'Do you play fortnite', ['yes', 'no'])  #The most important question question

gridAlign(frame1, Combobox, 'keyboard type', 'What kind of keyboard do you have', ['mechnical', 'membrame'])


#Frame 2 stuff
gridAlign(frame2, Entry, 'favourite game', 'What is your favourite game') #The game question

gridAlign(frame2, Entry, 'favourite youtuber', 'Who is your favorite youtuber') #The youtuber question

gridAlign(frame2, Radiobutton, 'favourite console', 'What is your favourite machine to play on', ['pc', 'XBox'])
gridAlign(frame2, Radiobutton, 'favourite console', '', ['Playstation', 'KFC console'])

gridAlign(frame2, Radiobutton, 'watches anime', 'Do you watch anime', ['yes', 'no']) #the anime question


#The buttons for going to the next frame or finishing the questioning
for i in frameList:
    btn = Button(i)
    btn.configure(text='Next page', command=nextFrame) if i != frameList[-1] else btn.configure(text='Finish', command=finish)
    btn.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)

for i in frameList:
    btn = Button(i)
    if i != frameList[0]:
        btn.configure(text='Previous page', command=prevFrame)  
        btn.place(relx=0.0, rely=0.9, relwidth=0.2, relheight=0.1)
nextFrame()
window.mainloop()