import os
from time import sleep
from string import ascii_uppercase
import yaml

def openPrompt(func, msg:str=''): #Clears the screen and starts the given promt(function)
    if msg: #If given, prints a message
        print(msg) 
        sleep(1)
    os.system('cls')
    func()

def question(question:str, awnsers:list, letters:bool=True):#Makes a question
    index = ascii_uppercase if letters else [i for i in range(int('inf'))]#Makes the indexing letters if true, else just numbers
    print(question)
    sleep(0.5)
    for i in range(len(awnsers)):
        print(f"{index[i]}) {awnsers[i]}")
        sleep(0.05)
    return input('>>').lower()


def ballChoice():#The number of balls will be chosen in this prompt
    ballNum = input("Hoeveel bolletjes wilt u? >>")


def litreChoise():#The litle amount will be chosen in this prompt
    pass


def start():#Here will be chosen what kind of questions will be asked depending on what the user awnsers
    customerType = question('Wat voor klant bent u?', ['Particulier', 'Zakelijk'])

    if customerType == 'a': #If the user chooses 'particulier'(a)
        openPrompt(ballChoice)
    elif customerType == 'b': #If the user chooses 'zakelijk'(b)
        openPrompt(litreChoise)
    else:
        openPrompt(start, 'Dat is geen optie')

os.system('cls')
print("Welkom bij Papi Gelato!")
sleep(2)
openPrompt(start)