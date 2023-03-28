import random
import time
score = 0
guessed = False

print("Raad mijn getal die tussen de 0 en 1000 valt")

for i in range(1, 21):#Loopt 20 keer
    if replay.lower == "n": break
    print(f"ronde {i}")
    randomNum = random.randint(0, 1000)#Geeft een random getal tussen de 0 en 1000

    for x in range(1, 11):#Loopt 10 keer
        print(f"Poging {x}")
        guess = int(input(">>"))

        #Maakt je score 1 hoger als je het geraden hebt
        if guess == randomNum: score += 1; print("Gefeliciteerd, je hebt het geraden!"); guessed = True; break 

        #checkt de som en of hij dichtbij zit
        sum = guess - randomNum
        if sum <= 20 and sum >= -20: print("Je bent heel erg warm")
        elif sum <= 50 and sum >= -50: print("Je bent warm")
        if guess < randomNum: print("Je moet hoger raden")
        elif guess > randomNum: print("Je moet lager raden")

    if guessed == False:
        print("Je hebt het niet geraden, helaas!")
        time.sleep(1)
        print(f"Het getal was {randomNum}")
        time.sleep(1)
    guessed = False
    replay = input("Wil je nog een keer spelen? y/n >>")
    if replay.lower == "n": break
print(f"Je score is {score} punten")
input("Press any key to exit...")