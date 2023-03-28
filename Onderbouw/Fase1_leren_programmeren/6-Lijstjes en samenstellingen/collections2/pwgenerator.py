import random
pwList = []
password = ["(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","("]
lowerCaseAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercaseAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
specialChars = ["@", "#", "$", "%", "&", "_", "?"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]


def fillPW(listName:list, forRange:list=0, forbiddenIndex:list=[]):
    global password
    emptySpaces = 0
    if listName == lowerCaseAlphabet: #If the chosen list is the lowercase, just fill the empty spaces
        for i in password:
            if i == "(": emptySpaces += 1
        loopthing = emptySpaces
    else:
        loopthing = (random.randint(forRange[0], forRange[1]))

    for i in range(loopthing): #Loops for a random amount between two numbers
        while True:
            chosenPos = random.randint(0, len(password) -1) #Chooses a random position in the password

            if password[chosenPos] != "(" or chosenPos in forbiddenIndex: #If that space is occupied or forbidden, rechoose a position
                continue 

            password[chosenPos] = random.choice(listName) #Or else, put a random character in the location
            break
    return

for i in range(6):    
    fillPW(uppercaseAlphabet, [2, 6]) #Uppercase alphabet

    fillPW(specialChars, [3, 3], [0, 23]) #Special characters

    fillPW(numbers, [4, 7], [0, 1, 2]) #Numbers

    fillPW(lowerCaseAlphabet) #Lowercase alphabet

    finalPw = ""
    for i in range(len(password)):
        finalPw += password[i]
    pwList.append(finalPw)
    password = ["(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","(","("]
print(pwList)