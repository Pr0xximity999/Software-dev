import random
import time
from typing import final
stashedDice = []
rolledDice = []
finalThrow = []
totalPoints = 0
threeOfAKind = False
pairs = False
alreadyMadeCombi = []

def checkIfCombiPossible(dices, combiType):
    global stashedDice, finalThrow, threeOfAKind, pairs, totalPoints, alreadyMadeCombi
    if combiType == "three of a kind":
        if combiType in alreadyMadeCombi: print("Deze combinatie heb je al gemaakt"); return False
        if len(dices) != 3:
            print("Kies alstublieft 3 dobbelstenen voor deze combinatie")
            return False
        else:
            for i in finalThrow:
                totalPoints += i
                alreadyMadeCombi.append(combiType)
                return True

    elif combiType == "four of a kind":
        if combiType in alreadyMadeCombi: print("Deze combinatie heb je al gemaakt"); return False
        if len(dices) != 4:
            print("Kies alstublieft 4 dobbelstenen voor deze combinatie")
            return False
        else:
            for i in finalThrow:
                totalPoints += i
                alreadyMadeCombi.append(combiType)
                return True

    elif combiType == "full house":
        if combiType in alreadyMadeCombi: print("Deze combinatie heb je al gemaakt"); return False
        if len(dices) != 5:
            print("Kies alstublieft 5 dobbelstenen voor deze combinatie")
            return False
        else:
            for i in range(5): #Checks if there's a triple
                for x in range(4):
                    for y in range(3):
                        if dices[i] == dices[x + 1]:
                            if dices[i] == dices[y + 2]:
                                threeOfAKind = True

            for i in range(5):
                for x in range(4):
                    if dices[i] == dices[x + 1]:
                        pairs = True
            if pairs == True and threeOfAKind == True:
                totalPoints += 25
                alreadyMadeCombi.append(combiType)
                return True
            else:
                print("Kan geen full house maken met deze stenen")

    elif combiType == "small straight":
        if combiType in alreadyMadeCombi: print("Deze combinatie heb je al gemaakt"); return False
        proceed = False
        if len(dices) != 4:
            print("Kies alstublieft 5 dobbelstenen voor deze combinatie")
            return False
        else:
            lowestNum = 7
            lowestNumIndex = 0
            for i in range(4):
                if dices[i] < lowestNum:
                    lowestNum = dices[i]
                    lowestNumIndex = i

            for i in range(4):
                if dices[i] == dices[lowestNumIndex] + 1 and not i == lowestNumIndex:
                    lowestNumIndex = i
                    proceed = True
                    break
            if proceed == False:
                print("Kan geen geldige combinatie maken")
                return False
            proceed = False

            for i in range(4):
                if dices[i] == dices[lowestNumIndex] + 1 and not i == lowestNumIndex:
                    lowestNumIndex = i
                    proceed = True
                    break
            if proceed == False:
                print("Kan geen geldige combinatie maken")
                return False
            proceed = False

            for i in range(4):
                if dices[i] == dices[lowestNumIndex] + 1 and not i == lowestNumIndex:
                    lowestNumIndex = i
                    proceed = True
                    break
            if proceed == False:
                print("Kan geen geldige combinatie maken")
                return False
            proceed = False
            totalPoints += 30
            alreadyMadeCombi.append(combiType)
            return True

    elif combiType == "large straight":
        if combiType in alreadyMadeCombi: print("Deze combinatie heb je al gemaakt"); return False
        if len(dices) != 5:
            print("Kies alstublieft 5 dobbelstenen voor deze combinatie")
            return False
        else:
            lowestNum = 7
            lowestNumIndex = 0
            for i in range(5):
                if dices[i] < lowestNum:
                    lowestNum = dices[i]
                    lowestNumIndex = i
            for i in range(5):
                if dices[i] == dices[lowestNumIndex] + 1 and not i == lowestNumIndex:
                    lowestNumIndex = i
                    proceed = True
                    break
            if proceed == False:
                print("Kan geen geldige combinatie maken")
                return False
            proceed = False

            for i in range(5):
                if dices[i] == dices[lowestNumIndex] + 1 and not i == lowestNumIndex:
                    lowestNumIndex = i
                    proceed = True
                    break
            if proceed == False:
                print("Kan geen geldige combinatie maken")
                return False
            proceed = False

            for i in range(5):
                if dices[i] == dices[lowestNumIndex] + 1 and not i == lowestNumIndex:
                    lowestNumIndex = i
                    proceed = True
                    break
            if proceed == False:
                print("Kan geen geldige combinatie maken")
                return False
            proceed = False
            totalPoints += 40
            alreadyMadeCombi.append(combiType)
            return True

    elif combiType == "yahtzee":
        if combiType in alreadyMadeCombi: print("Deze combinatie heb je al gemaakt"); return False
        if len(dices) != 5:
            print("Kies alstublieft 5 dobbelstenen voor deze combinatie")
            return False
        else:
            for i in range(4):         
                if dices[0] != dices[i + 1]:
                    print("Dit is geen geldige combinatie")
                    return False
            totalPoints = 50
            alreadyMadeCombi.append(combiType)
            return True

    elif combiType == "chance":
        if combiType in alreadyMadeCombi: print("Deze combinatie heb je al gemaakt"); return False
        if len(dices) != 5:
            print("Kies alstublieft 5 dobbelstenen voor deze combinatie")
            return False
        else:
            for i in finalThrow:
                totalPoints += i
                alreadyMadeCombi.append(combiType)
                return True


def throw(num):
    dice = []
    for i in range(num):
        number = random.randint(1, 6)
        dice.append(number)
    return dice

while True:
    for i in range(2):
        rolledDice = throw(5 - len(stashedDice))
        print("Uw dobbelstenen zijn:")
        for i in range(len(rolledDice)):
            print(f"nummer {i + 1} is een {rolledDice[i]}")
        
        proceed = False
        
        while proceed == False:
            takenNums = []
            takeDice = input("Wilt u een steen pakken? Y/N")
            if takeDice.lower() == "y": #If the user awnsered y on the question if he wanted to stash a dice
                while proceed == False:
                    chosenDice = int(input("Welk nummer steen wilt u pakken? >>"))
                    
                    if chosenDice > len(rolledDice) or chosenDice <= 0: #If the number is higher than the amount of rolled dices
                        print("Dat nummer is geen keuze")

                    elif chosenDice in takenNums: #If the user already has taken that number
                        print("Die steen heeft u al gepakt")

                    else:
                        takenNums.append(chosenDice)
                        stashedDice.append(rolledDice[chosenDice - 1])

                        while True:
                            repeat = input("Wilt u nog een andere steen pakken? Y/N >>")
                            if repeat.lower() == "y":
                                break
                            elif repeat.lower() == "n":
                                proceed = True
                                break
                            else:
                                print("Dat is geen keuze, voer Y/N in")
                                continue
                            
            elif takeDice.lower() == "n":
                proceed = True
                break
            else:
                print("Dat is geen keuze, voer Y/N in")
                continue

    while True:
        print("Welke combinatie wil je maken?")
        time.sleep(0.1)
        print("three of a kind")
        time.sleep(0.1)
        print("four of a kind")
        time.sleep(0.1)
        print("full house")
        time.sleep(0.1)
        print("small straight")
        time.sleep(0.1)
        print("large straight")
        time.sleep(0.1)
        print("yahtzee")
        time.sleep(0.1)
        print("chance")
        while True:
            chosenCombi = input(">>")
            if not chosenCombi in ["three of a kind", "four of a kind", "full house", "small straight", "large straight", "yahtzee", "chance"]:
                print("Dat is geen keuze")
                continue
            else:
                rolledDice = throw(5 - len(stashedDice))
                finalThrow = []
                finalThrow.append(rolledDice)
                finalThrow.append(stashedDice)
                print("Uw dobbelstenen zijn:")
                for i in range(len(finalThrow)):
                    print(f"Nummer {i} is {finalThrow[i]}")
                print("Welke dobbelstenen wil je hiervoor gebruiken?(voer het dobbelsteen nummer in)")
                print("Zet een spatie tussen de cijfers in")
                time.sleep(0.25)
                print("Voer 'andere combinatie' in als je en andere combinatie wilt")
                dices = input(">>")
                if dices == "andere combinatie":
                    break
                else:
                    if checkIfCombiPossible(dices, chosenCombi) == False:
                        continue