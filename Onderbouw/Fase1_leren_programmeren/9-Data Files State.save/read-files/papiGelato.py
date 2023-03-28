import time
import yaml

totalIceCreamQuan = 0.0
iceCreamQuan = 0
cupQuan = 0
coneQuan = 0
i = 1
toppingCost = 0.0
toppingQuan = 0
chosenContainer = ""
flavour = ""
customerType = ""
litersIceCream = 0
totalLiterQuan = 0
iceType = ""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '']

with open('settings.yml', 'r') as file:
    prices = yaml.safe_load(file)

def sorryMessage():
    print("Sorry dat is geen optie die we aanbieden...")

def whatKindOfCustomer(): #Asks what kind of customer the user is
    global customerType
    print("Wat voor klant bent u?")
    print("A) Particulier")
    print("B) Zakelijk")
    customerType = input(">>")
    if customerType.lower() == "a" : customerType = "particulier";howMuchIceCream()
    elif customerType.lower() == "b": customerType = "zakelijk"; howMuchIceCream()
    else: print("Sorry dat snap ik niet, kies A of B alstublieft"); whatKindOfCustomer()

def howMuchIceCream(): #Handles the ice cream quantity, but depending on the customer type makes it if its balls or liters
    global iceCreamQuan, customerType, iceType
    time.sleep(0.5)
    #Asks the user how much balls of icecream they want
    print()
    if customerType == "particulier":
        iceType = "bolletje"
        print("----------Bolletjes----------")
    elif customerType == "zakelijk":
        iceType = "liter"
        print("---------liters ijs----------") 

    iceCreamQuan = str(input(f"Hoeveel {iceType}s ijs wilt u? >>"))
    if chechIfWholeNum(iceCreamQuan, iceType) == False: howMuchIceCream() 
    iceCreamQuan = int(iceCreamQuan)

    #If the user enters a different number
    if customerType == "zakelijk": chooseFlavour()
    elif iceCreamQuan >= 1 and iceCreamQuan <= 3:
        chooseFlavour()
    elif iceCreamQuan > 3 and iceCreamQuan < 8:
        print(f"Dan krijgt u van mij een bakje met {iceCreamQuan} bolletjes");time.sleep(1); chooseFlavour()
    elif iceCreamQuan > 8 :
        print("Sorry, maar zulke grote bakken hebben we niet"); howMuchIceCream()

    #If the user enters anything else
    else:
        sorryMessage(); howMuchIceCream()

def chooseFlavour(): #The user chooses their flavor here
    global i, totalLiterQuan, iceType, flavour, iceCreamQuan, cupQuan, chosenContainer
    i = 1
    totalLiterQuan = 0
    print()
    print("------------smaak------------")
    print("U heeft keuze uit 4 smaken:")
    time.sleep(0.1)
    print("A) Aardbei")
    time.sleep(0.1)
    print("C) Chocolade")
    time.sleep(0.1)
    print("V) Vanille")

    def ask():
        global i, flavour,  iceCreamQuan
        print(f"Welke smaak wilt u voor {iceType} nummero {i}?")
        flavour = input(">>")

        #If the user doenst choose one, repeat in the same iteration
        if flavour.lower() != "a" and flavour.lower() != "c" and flavour != "v":
            sorryMessage()
            time.sleep(0.5)
            print("Kies alstublieft A, C, of V")
            ask()
        elif customerType == "zakelijk":
            while True: 
                global totalLiterQuan           
                literQuan = str(input("Hoeveel liter wilt u met deze smaak?"))
                if chechIfWholeNum(literQuan, iceType) == False: continue
                literQuan = int(literQuan)
                totalLiterQuan += literQuan
                if totalLiterQuan > iceCreamQuan: print("Dat is meer ijs dan dat u heeft besteld.");totalLiterQuan -= literQuan; continue
                else: i += literQuan -1
                if i < iceCreamQuan: i += 1; ask()
                else: break      
        if i < iceCreamQuan: i += 1; ask()

    ask()
        

    #Chooses whether to send the user right to the checkout or let them choose their container based on the quantity of balls
    if customerType == "zakelijk": checkout()
    elif iceCreamQuan >= 1 and iceCreamQuan <= 3:
        coneOrCup()
    elif iceCreamQuan > 3 and iceCreamQuan < 8:
        cupQuan += 1
        chosenContainer = "bakje"
        print(f"Hier is uw bakje met {iceCreamQuan} bolletjes")
        chooseTopping()

def coneOrCup(): #Asks if the user wants a cone or cup
    global iceCreamQuan, cupQuan, coneQuan, chosenContainer
    print()
    print("-------Hoorntje of bakje-------")
    time.sleep(0.5)
    print(f"Wilt u deze {iceCreamQuan} bolletjes in:")
    time.sleep(0.1)
    print("A) een hoorntje")
    time.sleep(0.1)
    print("B) een bakje")
    
    chosenContainer = input(">>")
    if chosenContainer.lower() == "a": 
        chosenContainer = "hoorntje"
        coneQuan +=1
        print(f"Hier is uw {chosenContainer} met {iceCreamQuan} bolletjes")
        chooseTopping()
    elif chosenContainer.lower() == "b":
        cupQuan +=1 
        chosenContainer = "bakje"
        print(f"Hier is uw {chosenContainer} met {iceCreamQuan} bolletjes")
        chooseTopping()
    else: 
        sorryMessage()
        time.sleep(0.5)
        print("Kies alstublieft A of B")
        coneOrCup()

def chooseTopping(): #Lets the user pick a topping
    global toppingCost, toppingQuan, iceCreamQuan, chosenContainer

    creamPrice = prices['toppings']['slagroom'] 
    sprinklePrice = prices['toppings']['bottetjes']
    caramelConePrice = prices['toppings']['caramel']['hoorentje']
    caramelCupPrice = prices['toppings']['caramel']['bakje']

    print("")
    print("-----------topping-----------")
    print("Wilt u er nog een topping op?")
    time.sleep(0.1)
    print("A) Geen")
    time.sleep(0.1)
    print("B) Slagroom")
    time.sleep(0.1)
    print("C) Sprinkels")
    time.sleep(0.1)
    print("D) Caramel saus")
    topping = input(">>")

    #Calculates the topping cost based of the decision, quantity of balls and the container
    if topping.lower() == "a": repeatOrStop()   
    else: toppingQuan += 1
    if topping.lower() == "b": toppingCost += creamPrice; repeatOrStop()
    elif topping.lower() == "c": toppingCost += iceCreamQuan * sprinklePrice; repeatOrStop()
    elif topping.lower() == "d":
        if chosenContainer == "hoorntje": toppingCost += caramelConePrice; repeatOrStop()
        elif chosenContainer == "bakje": toppingCost += caramelCupPrice; repeatOrStop()

def repeatOrStop(): #Asks if the user is done or want to order again
    global totalIceCreamQuan
    global iceCreamQuan

    time.sleep(0.5)
    print()
    repeatOrder = input("Wilt u nog meer bestellen? Y/N >>")
    if repeatOrder.lower() == "y": totalIceCreamQuan += iceCreamQuan; howMuchIceCream()

    elif repeatOrder.lower() == "n":totalIceCreamQuan += iceCreamQuan; checkout() 

    else: sorryMessage(); time.sleep(1); print("Kies alstublieft Y of N"); repeatOrStop()

def checkout(): #The user gets their receipt here
    global totalIceCreamQuan, iceCreamQuan, coneQuan, cupQuan, toppingCost, toppingQuan, customerType

    creamLitrePrice = prices['liter']
    creamBallPrice = prices['bolletjes']
    conePrice = prices['hoorentjes']
    cupPrice = prices['bakje']
    btw = prices['btw']

    print()
    print()
    print()
    print()
    print()
    print("---------['Papi Gelato']---------")
    if customerType == "particulier":
        print(f"Bolletjes     {totalIceCreamQuan} x €{creamBallPrice}  = €" + "%.0f" %(totalIceCreamQuan * creamBallPrice))
        if coneQuan > 0:
            print(f"Hoorntje      {coneQuan} x €{conePrice}    = €"+ "%.0f" %float(coneQuan *conePrice))
        if cupQuan > 0:
            print(f"Bakje         {cupQuan} x €{cupPrice}    = €" + "%.0f" %float(cupQuan * cupPrice))
        if toppingQuan > 0:
            print(f"topping       1 x €{toppingCost}     = €"+ "%.0f" %toppingCost)
        print("                         --------- +")
        print(f"Totaal                     = €" + "%.0f" % float(totalIceCreamQuan * creamBallPrice + coneQuan * conePrice + cupQuan * cupPrice + toppingCost))

    elif customerType == "zakelijk":
        print(f"Liter          {iceCreamQuan} x €{creamLitrePrice}  = €{iceCreamQuan * creamLitrePrice}")
        print("                         --------- +")
        print(f"Totaal                   = {float(iceCreamQuan * creamLitrePrice)}")
        print(f"BTW({btw}%)                  = {float((iceCreamQuan * creamLitrePrice) * (btw / 100))}")
    print("Bedankt en tot ziens!")
    input()
    exit()

def chechIfWholeNum(checkNum, iceType): #Checks if the inputted number's a whole number and contains no letters
    #If the input contains letters
    for i in range(len(checkNum)):
        if checkNum[i] in alphabet: print("Voer geen letters in alstublieft, alleen getallen"); return False
    
    #If the user enters a decimal number
    if float(checkNum) % 1 != 0: print(f"Helaas, wij werken alleen met hele {iceType}s, voer een heel getal in"); return False
    else: checkNum = int(checkNum)

    #If the user enters zero
    if checkNum <= 0:print(f"Je moet ten minste 1 {iceType} kiezen"); return False


#The user starts here
print("Welkom bij Papi Gelato!")
time.sleep(1)

whatKindOfCustomer()