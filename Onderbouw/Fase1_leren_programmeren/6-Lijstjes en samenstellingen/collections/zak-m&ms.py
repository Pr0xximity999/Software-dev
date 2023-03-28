import random
import string
alphabet = []
string.ascii_lowercase = alphabet
colors = ["oranje", "blauw", "groen", "bruin"]


def makeMnmBagList(mnmQuan: int = 1):
    global colors
    bag = []
    for i in range(mnmQuan):
        chosenColor = random.choice(colors)
        bag.append(chosenColor)
    tmp = list(bag)
    bag.sort(key=lambda x: tmp.count(x))
    bag.reverse()
    return bag


def makeMNmBagDict(mnmQuan: int = 1):
    bag = dict()
    for i in range(mnmQuan):
        chosenColor = random.choice(colors)
        if chosenColor in bag.keys():
            bag[chosenColor] += 1
        else:
            bag[chosenColor] = 1
    bag = {k: v for k, v in sorted(bag.items(), key=lambda item: item[1], reverse=True)}

    return bag


def start():
    quantity = input("Hoeveel M&M's wil je? >>")

    for i in range(len(quantity)):
        if quantity[i] in alphabet:
            print("Voer geen nummer in alstublieft")
            start()
    if float(quantity) % 1 != 0:
        print("Voer een heel getal in")
        start()
    else:
        quantity = int(quantity)
    listType(quantity)


def listType(quantity):
    colType = input("Wil je de lijst zien als een list of dict? L/D >>")

    if colType.lower() == "d":
        bag = makeMNmBagDict(quantity)
    elif colType.lower() == "l":
        bag = makeMnmBagList(quantity)

    print(bag)


start()
input()
