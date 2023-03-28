groceryList = {}
def makelist():
    item = input("Wat wilt gij schenken aan uwzelf? >>")

    if not item in groceryList: 
        groceryList.update({item : 0})

    groceryList[item] += int(input("Hoevaak wil de dit toevoegen? >>"))

    if input("Wil je nog een product toevoegen? Y/N >>").lower() != "y": 
        print(groceryList)
        return
    makelist()
makelist()
    