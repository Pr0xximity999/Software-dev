from logging import exception


meerpizzas = False
nietMeerPizzas = False
groottePrijs = 0.0
toppingAantallen = list()
pizzaGroepInformatie = list()
verschillendePizzaAantallen = list()
enkelPizzaPrijs = 0.0
toppingPrijsChampignon = 0.05
toppingPrijsKaas = 0.15
toppingPrijsPepperoni = 0.50
toppingPrijsAnnanas = 0.20
toppingPrijsWater = 0.01
totalePizzaPrijs = 0

print("Hallo, en welkom bij mijn pizzawinkel!")

def checkIfWholeNumber (givenstring):
    givenstring
    try:
        givenstring = int()
        if givenstring <= 0:
            raise exception
    except:
        print("Geef een geldig getal op AUB")
        return False
    else:
        return True

while True:
    aantalChampignon = 0
    aantalKaas = 0
    aantalPepperoni = 0
    aantalAnnanas = 0
    aantalWater = 0
    if nietMeerPizzas == True: break
    meerpizzas = False
    print("--------------------")
    print("      klein|€ 3,00  |")
    print("     medium|€ 6,50  |")
    print("      groot|€ 10,00 |")
    print("extra-large|€ 13,50 |")
    print(" gigantisch|€ 15,00 |")
    print("--------------------")
    proceed = False
    while not proceed:
        print("Welke grootte pizza wilt u hebben?")
        #Vraagt hoe groot de pizzabodem is
        groottePizza = input().lower()
        proceed = True

        if groottePizza == "klein":
            groottePizza = "kleine"
            groottePrijs = 3.0

        elif groottePizza == "medium":
            groottePizza = "medium"
            groottePrijs = 6.50

        elif groottePizza == "groot":
            groottePizza = "grote"
            groottePizza = 6.10

        elif groottePizza == "extra-large" or groottePizza == "extra large":
            groottePizza = "extra large"
            groottePrijs = 13.50

        elif groottePizza == "gigantisch":
            groottePrijs = "gigantische"
            groottePrijs = 15.00
        else:
            print("Dat is geen geldige invoer")
            proceed = False
            continue

    #laat de keuze van de toppings zien en vraagt hoeveel pizza's je er mee wilt

    while True:
        if meerpizzas == True: break
        if nietMeerPizzas == True: break
        print("--------------------")
        print(" prijs per stuk/gram|")
        print("--------------------")
        print(" champignon|€ 0.05  |")
        print("       kaas|€ 0.15  |")
        print("  pepperoni|€ 0.50  |")
        print("    annanas|€ 0.20  |")
        print("      water|€ 0.01  |")
        print("--------------------")
        proceed = False
        while not proceed:
            print("Welke toppings wil je er op?")

            gekozenTopping = input()
            proceed = True
            aantalvariant = 0
            toppingPrijsVariant = 0

            
            #Checkt eerst of het een van de mogelijke toppings is
            if gekozenTopping == "champignon":
                gekozenTopping = "champignons"
                aantalvariant = aantalChampignon
                toppingPrijsVariant = toppingPrijsChampignon

            elif gekozenTopping == "kaas":
                gekozenTopping = "gram kaas"
                aantalvariant = aantalKaas
                toppingPrijsVariant = toppingPrijsKaas

            elif gekozenTopping == "pepperoni":
                gekozenTopping = "pepperoni"
                aantalvariant = aantalPepperoni
                toppingPrijsVariant = toppingPrijsPepperoni

            elif gekozenTopping == "annanas":
                gekozenTopping = "annanas"
                aantalvariant = aantalAnnanas
                toppingPrijsVariant = toppingPrijsAnnanas

            elif gekozenTopping == "water":
                gekozenTopping = "gram water"

            else:
                print("Dat is geen geldige invoer")
                proceed = False
                continue

            while True:
                aantalvariant += input("Hoeveel " + gekozenTopping + " wil je hebben op je pizza? ")
                if checkIfWholeNumber(aantalvariant) == False:
                    continue
                break
            enkelPizzaPrijs += aantalvariant * toppingPrijsVariant + groottePrijs

            meerToppings = input("Wilt u meer toppings hebben? y/n ")
            if meerToppings == "y": 
                continue

            else:
                #Berekend de prijs van de groep pizza's               
                aantalPizzas = int(input("Hoeveel pizza's wil u hiermee hebben? "))
                groepsPizzaPrijs = enkelPizzaPrijs * aantalPizzas

                #Voegt de pizzagroep en al de informatie toe een een lijst
                toppingAantallen
                pizzaGroepInformatie.append(aantalPizzas)
                pizzaGroepInformatie.append(groepsPizzaPrijs)
                pizzaGroepInformatie.append(aantalChampignon)
                pizzaGroepInformatie.append(aantalKaas)
                pizzaGroepInformatie.append(aantalPepperoni)
                pizzaGroepInformatie.append(aantalAnnanas)
                pizzaGroepInformatie.append(aantalWater)
                pizzaGroepInformatie.append(groottePrijs)

                meerpizzas = input("Wilt u meer pizza's hebben? y/n")
                if meerpizzas == "y":
                    meerpizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue
                else:
                    nietMeerPizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue
            
#Berekend de prijs van alle pizza's
i = 0
for x in verschillendePizzaAantallen:
    totalePizzaPrijs += x[1 + (i * 8)]
    totalePizzaPrijs += x[2 + (i * 8)] * toppingPrijsChampignon
    totalePizzaPrijs += x[3 + (i * 8)] * toppingPrijsKaas
    totalePizzaPrijs += x[4 + (i * 8)] * toppingPrijsPepperoni
    totalePizzaPrijs += x[5 + (i * 8)] * toppingPrijsAnnanas
    totalePizzaPrijs += x[6 + (i * 8)] * toppingPrijsWater
    i += 1

i2 = 0
print("De totale prijs van uw pizza('s) is €" + str(totalePizzaPrijs))
#Leest de prijzen op van de groepen pizza en laat per groep het beleg zien
print("Uw pizzalijst:")
for x in verschillendePizzaAantallen:
    print("|" + str(x[0 + (i2 * 8)]) + " Pizza's met:")
    print("|" + str(x[2 + (i2 * 8)]) + " champignons,")
    print("|" + str(x[3 + (i2 * 8)]) + " gram kaas,")
    print("|" + str(x[4 + (i2 * 8)]) + " stukken pepperoni,")
    print("|" + str(x[5 + (i2 * 8)]) + " stukken annanas,")
    print("|" + str(x[6 + (i2 * 8)]) + " gram water")
    print("|ten waarde van €" + str(x[1 + (i2 * 8)] + x[2 + (i2 * 8)] * toppingPrijsChampignon + x[3 + (i2 * 8)] * toppingPrijsKaas + x[4 + (i2 * 8)] * toppingPrijsPepperoni + x[5 + (i2 * 8)] * toppingPrijsAnnanas + x[6 + (i2 * 8)] * toppingPrijsWater))
    print("----------------------------")
    i2 += 1
print("Dit allemaal bij elkaar kost in totaal €" + str(totalePizzaPrijs))
print("Bedankt voor uw bestelling!")