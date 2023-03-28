finished = False
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
groceryList = list()

def chechIfint(num):
    for i in range(len(num)):
        if num[i] in alphabet: print("Voer geen letter in alstublieft"); return False
    if float(num) % 1 != 0: print("Voer een heel getal in"); return False
    return True

def addToList(grocerytype, groceryquan:int):
    global groceryList
    grocery = [grocerytype, groceryquan]
    
    for i in groceryList:
        if i[0] == grocery[0]: i[1] += grocery[1]; return 

    groceryList.append(grocery)
    return 

def printList():
    global groceryList
    for i in groceryList:
        print(f"Je hebt {i[1]} keer {i[0]}")

    input()
    exit()

while finished == False:
    grocery = input("Wat wil je aan je boodschappenlijstje toevoegen? >>")
    groceryQuan = input("Hoeveel wil je hiervan? >>")
    if chechIfint(groceryQuan) == False: continue
    groceryQuan = int(groceryQuan)
    addToList(grocery, groceryQuan)

    while finished == False:
        proceed = input("Wilt u meer boodschappen toevoegen? Y/N >>")
        if proceed.lower() == "y": break
        elif proceed.lower() == "n": printList()
        else: print("Dat is geen optie, kies y of n"); continue
