from string import ascii_lowercase
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import date

#Initializes the window
window = Tk()
window.configure(bg='white')
window.geometry('350x150')
window.resizable(0,0)


year = StringVar(window)
prevText = '2022'

def updateDays(arg1='', arg2='', arg3=''):
    global months
    if int(year.get()) % 4 == 0 and monthCombo.get() == 'Feb':
        dayCombo.configure(values=months[monthCombo.get()] + ['29'])
        
    if int(dayCombo.get()) > months[monthCombo.get()][-1]: 
        dayCombo.current(months[monthCombo.get()][-1])
        return
    dayCombo.configure(values=months[monthCombo.get()])


def numCheck(arg1, arg2, arg3):
    global prevText, year
    for i in year.get().lower():
        if i in ascii_lowercase + '!@#$%^&*()-_=+[{]}\|;:,<.>/?`~':
            messagebox.showwarning('Only numbers allowed', 'Please only enter in numbers')
            year.set(prevText)
            return
    prevText = year.get()
    updateDays()
    return

def calcDate(d2=tuple):
    d1 = date.today()
    d2 = date(int(yearCombo.get()), list(months.keys()).index(monthCombo.get()) + 1, int(dayCombo.get()))
    delta = d1 - d2 

    if delta.days > 0:
        messagebox.showwarning('Resultaat', f'Deze datum is {delta.days} dagen in het verleden')
    elif delta.days < 0:
        messagebox.showwarning('Resultaat', f'Deze datum is {-delta.days} dagen in de toekomst')
    else:
        messagebox.showwarning('Resultaat', f'Deze datum is vandaag')


#Makes the months with their respecting days
months = {  
            'Jan' : [i for i in range(1, 32)],
            'Feb' : [i for i in range(1, 29)], 
            'Mar' : [i for i in range(1, 32)], 
            'Apr' : [i for i in range(1, 31)], 
            'May' : [i for i in range(1, 32)], 
            'Jun' : [i for i in range(1, 31)], 
            'Jul' : [i for i in range(1, 32)], 
            'Aug' : [i for i in range(1, 32)], 
            'Sep' : [i for i in range(1, 31)], 
            'Oct' : [i for i in range(1, 32)], 
            'Nov' : [i for i in range(1, 31)], 
            'Dec' : [i for i in range(1, 32)]
        }


#Initializes the label
dateLabel = Label(window, text='Date', font=(30), bg='white')
dateLabel.pack()
dateLabel.place(relwidth=0.3, relx=0.35, rely=0, relheight=0.1)

#Initializes the combo boxes for the days and months, and the entry for the year
dayCombo = Combobox(window, values=[i for i in range(1, 32)])
dayCombo.current(0)
dayCombo.pack()
dayCombo.place(relwidth=0.2, relx=0.1, rely=0.35, relheight=0.15)

monthStringvar = StringVar()
monthStringvar.trace('w', updateDays)
monthCombo = Combobox(window, textvariable=monthStringvar, values=[i for i in months.keys()])
monthCombo.current(0)
monthCombo.pack()
monthCombo.place(relwidth=0.2, relx=0.4, rely=0.35, relheight=0.15)

year = StringVar(window, '2022')
year.trace('w', numCheck)
yearCombo = Entry(window, textvariable=year)
yearCombo.pack()
yearCombo.place(relwidth=0.2, relx=0.7, rely=0.35, relheight=0.15)

goBtn = Button(window, text='Go', command=calcDate )
goBtn.pack()
goBtn.place(relwidth=0.1, relx=0.45, rely=0.7, relheight=0.15)



window.mainloop()