import os
from os import name
import random
import time
import json
namelist = []
nameDict = {}

if not os.path.exists('data'):
    os.mkdir('data')
def asknames():
    global namelist
    time.sleep(0.1)
    name = input(f"Wat is de naam van persoon {len(namelist) + 1}? >>") #Asks the person's name

    if name in namelist: #If the name is in the list, don't add it
        print("Die naam is al gebruikt")
        asknames()
    else: 
        namelist.append(name)
        return

def giveTickets():
    global namelist, nameDict
    random.shuffle(namelist)
          

    for i in range(len(namelist) -1):
        nameDict.update({namelist[i] : namelist[i + 1]})
        print(f"{namelist[i]} heeft {namelist[i + 1]}")
        
    print(f"{namelist[len(namelist) - 1]} heeft {namelist[0]}")
    nameDict.update({namelist[-1] : namelist[0]})

    i = 0
    while True:
        if not os.path.exists(f'data/data{i}.json'):
            with open(f'data/data{i}.json', 'w') as file:
                parsed = json.dumps(nameDict)
                file.write(parsed)
            break
        else:
            i += 1

while len(namelist) <= 1: #Makes it so that the program has to have at least 2 names registered
    asknames()


print("voer een lege plaats in als je niet meer namen wilt")
while True: 
    time.sleep(0.1)
    name = input(f"Wat is de naam van persoon {len(namelist) + 1}? >>") #Asks the person's name

    if name == "":
        giveTickets()
        break
    elif not name in namelist: #If the name isnt in the list, add it
        namelist.append(name)
        continue
    elif name in namelist: #If the name is already in the list, dont add it
        print("Die naam is al gebruikt")
        asknames()
    else:
        print("Dat is geen optie")