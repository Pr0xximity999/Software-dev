import time
import webbrowser
weetVanToaster = False
falseStart = 0
inventory = list()
alInKelderGeweest = False
alInKeukenGeweest = False
alInKoelkastGeweest = False

def startGame():
    #Je word wakker
    print("Je word wakker, je gaat rechtop zitten, voor je staat je nieuwe pc die je gister hebt gekocht")
    time.sleep(3)
    print("Maar je hebt trek dus je wilt eerst een tosti eten")
    time.sleep(1)
    print("Wat ga je doen?")
    #De slaapkamer loop
    while True:
        action = input(">>")

        #Je springt uit het raam
        if action == "raam" or action == "spring":
            time.sleep(0.5)
            print("Je springt uit het raam")
            time.sleep(1)
            print("Je breekt je nek")
            time.sleep(1)
            exit()

        #Je gaat weer slapen
        if action == "ga slapen" or action == "slaap":
            time.sleep(0.5)
            print("Je hebt besloten om weer te gaan slapen")
            time.sleep(1)
            print("Geen idee waarom tho, ik bedoel je hebt net geslapen")
            time.sleep(1)
            print("Waarom zou je dat dan weer doen")
            time.sleep(1)
            print("Beetje jammer dit")
            time.sleep(1)
            print("Je sterft in je slaap omdat je verhongerd")
            time.sleep(0.5)
            exit()
        
        #Je zet de computer aan
        elif "pc" in action or "computer" in action or "game" in action:
            time.sleep(0.5)
            print("Je hebt besloten je pc aan te zetten")
            time.sleep(1)
            print("Omdat je je pc pas gister heb gekocht staan er nog alleen maar minecraft, fortnite en een internet browser op")
            
            #De loop die je in de computeropties houd
            while True:
                action = input(">>")

                #Je opent minecraft
                if "minecraft" in action:
                    
                    print("Je gaat minecraft spelen, maar je hebt teveel trek dus je kan je niet goed concentreren")
                    time.sleep(2)
                    print("Je gaat dood in minecraft en sterft van het ragen")
                    exit()

                #Je opent fortnite
                elif "fortnite" in action:
                    time.sleep(0.5)
                    print("Je opent fortnite, maar er land een meteoor op je huis en je sterft")
                    time.sleep(1)
                    exit()

                #Je opent het internet
                if "internet" in action:
                    while True:
                        time.sleep(0.5)
                        print("Je besluit het internet te openen, je hebt 3 sites opgeslagen.")
                        time.sleep(2)
                        print("De namen zijn: ramdownloader.com, youtube.com en pizzapapa.com")
                        time.sleep(2)
                        print("Welke open je?")
                        action = input(">>")

                        #Je opent ramdownloader.com
                        if action == "ramdownloader.com":
                            time.sleep(0.5)
                            print("Je opent ramdownloader.com en download 1 terrabyte extra aan ram")
                            time.sleep(2)
                            print("Je computer explodeert door het groot aantal ram dat nu op je computer staat")
                            time.sleep(3)
                            print("Je sterft")
                            time.sleep(0.5)
                            exit()
                        
                        #Je opent youtube en word gerickrolld
                        elif action == "youtube.com" or action == "youtube":
                            time.sleep(0.5)
                            print("Je opent het youtube tabblad die je hebt opgeslagen")
                            time.sleep(1)
                            print("Aan het laden...")
                            time.sleep(1)
                            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                            time.sleep(7)
                            print("Je bent gerickrolld...")
                            time.sleep(1)
                            print("Je springt uit het raam")
                            time.sleep(1)
                            exit()
                        
                        #je opent pizzapapa
                        if action == "pizzapapa.com" or action == "pizzapapa":
                            time.sleep(0.5)
                            print("Je besluit een pizza te bestellen")
                            time.sleep(1)
                            import pizzaCalculator
                            pizzaCalculator()

                #Je sluit de computer af
                elif action == "sluit computer af" or action == "zet computer uit" or action == "sluit pc af" or action == "zet computer uit":
                    print("Je besluit de computer weer af te sluiten en staat op uit je stoel")
                    time.sleep(2)
                    break

                else:
                    print("Dat is geen commando")                 
                    continue

        #Je gaat je kamer uit      
        elif "verlaat" in action or "uit" in action:
            time.sleep(0.5)
            print("Je verlaat je kamer")
            time.sleep(1)
            print("Voor je staat de wc deur en links van je de trap naar beneden")

            #De pre-trap loop
            while True:
                action = input(">>")

                #Je gaat naar de wc
                if "wc" in action or "voren" in action:
                    time.sleep(0.5)
                    print("Je besluit naar de wc te gaan")
                    action = input(">>")
                    #Je gaat poepen zonder je broek naar beneden
                    if "poep" in action:
                        time.sleep(0.5)
                        print("Je besluit te poepen, terwijl je nog je broek naar boven hebt")
                        time.sleep(2)
                        print("Je sterft van broekpoeperij")
                        time.sleep(1)
                        exit()

                    #Je gaat plassen zonder je broek naar beneden
                    elif "plas" in action:
                        time.sleep(0.5)
                        print("Je besluit te plassen, terwijl je nog je broek naar boven hebt")
                        time.sleep(2)
                        print("Je sterft van broekplasvergiftiging")
                        time.sleep(1)
                        exit()

                    #Je doet je broek naar beneden
                    elif "broek" in action:
                        time.sleep(0.5)
                        print("Je hebt je broek naar beneden gedaan")
                        action = input(">>")
                        #Je gaat poepen zonder de bril naar beneden
                        if "poep" in action:
                            time.sleep(0.5)
                            print("Je besluit te poepen, terwijl de bril nog niet naar beneden is")
                            time.sleep(2)
                            print("Je sterft van voet poep infectie")
                            time.sleep(1)
                            exit()

                        #Je gaat plassen zonder de bril naar beneden
                        elif "plas" in action:
                            time.sleep(0.5)
                            print("Je besluit te plassen, terwijl de bril nog niet naar beneden is")
                            time.sleep(2)
                            print("Je sterft van de radioactieve stoffen in je plas")
                            time.sleep(1)
                            exit()
                        
                        #Je doet de bril omhoog
                        elif "bril" in action:
                            time.sleep(0.5)
                            print("Je hebt de wcbril omhoog gedaan")
                            action = input(">>")
                            #Je poept/plast
                            if "poep" in action or "plas" in action:
                                time.sleep(0.5)
                                print("Gefeliciteerd, je hebt succesvol geplast!")
                                time.sleep(1)
                                print("Maar je sterft nogsteeds omdat ik daar zin in heb")

                            else:   
                                print("Dat is geen commando")                 
                                continue 
                        else:   
                            print("Dat is geen commando")                 
                            continue 
                    else:   
                        print("Dat is geen commando")                 
                        continue 
                        

                #Je springt naar beneden
                elif "spring" in action:
                    time.sleep(0.5)
                    print("Je springt van de trap af en breekt je nek")
                    time.sleep(1)
                    exit()

                #Je gaat naar beneden
                elif "beneden" in action or "trap" in action or "links" in action:
                    time.sleep(0.5)
                    print("Je loopt naar beneden")
                    time.sleep(1)
                    print("Links van je is de kelderdeur, voor je de deur naar buiten en rechts de keuken")

                    while True:    
                        action = ""                            
                        action = input(">>")
                    
                        #Je gaat naar de kelder
                        if "kelder" in action or "links" in action:
                            
                            time.sleep(0.5)
                            if alInKelderGeweest == False:
                                print("Je loopt naar de kelder en gaat naar beneden")
                                time.sleep(1)
                                print("Je weet dat er hier ingredienten liggen, wat doe je?")
                            else: print("Je staat weer in de kelder")
                            #Kelder loop
                            while True:
                                if not "uit" in action or "verlaat" in action: action = input(">>")
                                #Je zoekt voor ingredienten
                                if "zoek" in action and alInKelderGeweest == False:
                                    time.sleep(0.5)
                                    print("Je zoekt voor ingredienten en vind curry en iets wat op ham lijkt")
                                    time.sleep(2)
                                    print("Wat pak je?")

                                    #Post-zoek kelder loop
                                    while True:
                                        action = input(">>")

                                        #Je pakt de curry
                                        if "curry" in action or "pak" in action and (not "curry" in inventory):
                                            time.sleep(0.5)
                                            print("Je pakt de curry")
                                            time.sleep(0.5)
                                            print("Curry toegevoegd aan inventory")
                                            inventory.append("curry")

                                        #Je pakt de curry, maar je hebt het al
                                        elif "curry" in action or "pak" in action and "curry" in inventory:
                                            time.sleep(0.5)
                                            print("Je hebt de curry al gepakt")
                                            
                                        #Je pakt de ham
                                        elif "ham" in action or "pak" in action and (not "ham" in inventory):
                                            time.sleep(0.5)
                                            print("Je pakt de..")
                                            time.sleep(1)
                                            print("Tja..")
                                            time.sleep(1)
                                            print("Is dit wel ham?")
                                            time.sleep(1)
                                            print("ham(?) toegevoegd aan inventory")
                                            inventory.append("ham")

                                        #Je pakt de ham, maar je hebt het al
                                        elif "ham" in action or "pak" in action and "ham" in inventory:
                                            time.sleep(0.5)
                                            print("Er ligt geen ham meer")

                                        #Je verlaat de kelder
                                        elif "uit" in action or "verlaat" in action:
                                            alInKelderGeweest = True                                            
                                            time.sleep(0.5)
                                            print("Je gaat de kelder uit en staat weer onder aan de trap naar boven")
                                            break
                                #Je verlaat de kelder(ik moest dubbel breaken)        
                                elif "uit" in action or "verlaat" in action:
                                    break

                                #Je zoekt als je al hebt gezocht voor ingredienten
                                elif "zoek" in action and alInKelderGeweest == True:
                                    time.sleep(0.5)
                                    print("Je heb de hele kelder al doorgezocht")

                                else:   
                                    print("Dat is geen commando")                 
                                    continue 

                        #Je gaat naar buiten 
                        elif "voren" in action or "buiten" in action or "buren" in action or "deur" in action and (not "sleutel" in inventory):
                            time.sleep(0.5)
                            if not "sleutel" in inventory:
                                time.sleep(0.5)
                                print("De voordeur is op slot, je hebt een sleutel nodig")
                                time.sleep(2)
                                print("Misschien ligt er eentje in de keuken")
                                time.sleep(1)
                                continue
                            elif "sleutel" in inventory and weetVanToaster == False:
                                time.sleep(0.5)
                                print("Je doet de voordeur open, maar...")
                                time.sleep(1)
                                print("Waarom zou je naar buiten gaan?")
                                time.sleep(1)
                                print("Je besluit binnen te blijven")
                                continue
                            elif "sleutel" in inventory and weetVanToaster == True and (not"toaster" in inventory):
                                time.sleep(0.5)
                                print("Je doet de voordeur open en gaat naar de buren toe om een tosti ijzer te lenen")
                                inventory.append("tostiIjzer")
                                time.sleep(3)
                                print("Je staat weer binnen voor de deur")
                                time.sleep(2)
                                print("Tosti ijzer toegevoegd aan inventory")
                                continue
                            elif "sleutel" in inventory and weetVanToaster == True and "toaster" in inventory:
                                time.sleep(0.5)
                                print("Je hebt nog geen tosti gemaakt, dus je hoeft het tosti ijzer nog niet terug te brengen")
                                time.sleep(3)
                                continue
                            else:   
                                print("Dat is geen commando")                 
                                continue 
                        
                        #Je gaat naar de keuken
                        elif "keuken" in action or "rechts" in action:
                            time.sleep(0.5)
                            if "buiten" in action or "buren" in action:
                                break

                            elif alInKeukenGeweest == False:
                                print("Je loopt naar de keuken, je hoort de koelkast zachtjes zoemen")
                                time.sleep(1)
                                print("Je ziet sleutels op de keukentafel zitten")
                                time.sleep(1)
                                print("Nu kan je eindelijk je tosti maken")
                                alInKeukenGeweest = True
                            else: print("Je loopt terug de keuken in")
                            while True:
                                
                                if not "maak" in action or not "tosti" in action: action = input(">>")

                                if "buiten" in action or "buren" in action:
                                    time.sleep(0.5)                                      
                                    break

                                #Je opent de koelkast
                                if "koelkast" in action and "open" in action:
                                    
                                    if alInKoelkastGeweest == False:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast, een koele wind zucht langs je nek")
                                        time.sleep(1)
                                        print("Tot je verbazing ligt er alleen maar brood, melk en kaas in")
                                        time.sleep(2)
                                        alInKoelkastGeweest = True
                                    #Checkt of je al iets uit de koelkast hebt gepakt
                                    elif "brood" in inventory and "kaas" in inventory and "melk" in inventory:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast")
                                        time.sleep(1)
                                        print("Hij is leeg")
                                        time.sleep(1)
                                        print("Je sluit de koelkast weer")
                                        time.sleep(1)
                                    elif "brood" in inventory and "kaas" in inventory:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast")
                                        time.sleep(1)
                                        print("Er ligt nog melk in")
                                        time.sleep(1)
                                    elif "brood" in inventory and "melk" in inventory:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast")
                                        time.sleep(1)
                                        print("Er ligt nog kaas in")
                                        time.sleep(1)
                                    elif "kaas" in inventory and "melk" in inventory:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast")
                                        time.sleep(1)
                                        print("Er ligt nog brood in")
                                        time.sleep(1)
                                    elif "brood" in inventory:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast")
                                        time.sleep(1)
                                        print("Er ligt nog kaas en melk in")
                                        time.sleep(1)
                                    elif "melk" in inventory:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast")
                                        time.sleep(1)
                                        print("Er ligt nog kaas en brood in")
                                        time.sleep(1)
                                    elif "kaas" in inventory:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast")
                                        time.sleep(1)
                                        print("Er ligt nog brood en melk in")
                                        time.sleep(1)
                                    else:
                                        time.sleep(0.5)
                                        print("Je opent de koelkast")
                                        time.sleep(1)
                                        print("Er ligt nog brood, kaas en melk in")
                                        time.sleep(1)

                                    while True:
                                        action = input(">>")

                                        #Je pakt de kaas
                                        if "kaas" in action and (not "kaas" in inventory):
                                            time.sleep(0.5)
                                            print("Je pakt een plak kaas uit het bakje, vreemd, het is het laatste plakje")
                                            inventory.append("kaas")
                                            time.sleep(2)
                                            print("Kaas toegevoegd aan inventory")
                                            continue

                                        #Je pakt de kaas maar je hebt de kaas al
                                        elif "kaas" in action and "kaas" in inventory:
                                            time.sleep(0.5)
                                            print("Er ligt geen kaas meer in de koelkast")
                                            continue
                                        
                                        #Je pakt het brood
                                        elif "brood" in action and (not "brood" in inventory):
                                            time.sleep(0.5)
                                            print("Je pakt de 2 laatste broodjes die er lagen")
                                            time.sleep(1)
                                            print("(Iemand moet weer eens naar de winkel gaan)")
                                            time.sleep(1)
                                            inventory.append("brood")
                                            print("Brood toegevoegd aan inventory")
                                            continue

                                        #Je pakt het brood maar je hebt het brood al
                                        elif "brood" in action and "brood" in inventory:
                                            time.sleep(0.5)
                                            print("Er ligt geen brood meer in de koelkast")
                                            continue

                                        #Je pakt melk
                                        elif "melk" in action and (not "melk" in inventory):
                                            time.sleep(0.5)
                                            print("Je pakt het pak melk uit de koelkast")
                                            inventory.append("melk")
                                            print("Melk toegevoegd aan inventory")
                                            continue

                                        #Je pakt melk maar hebt het al gepakt
                                        elif "melk" in action and "melk" in inventory:
                                            time.sleep(0.5)
                                            print("Je hebt het laatste pak melk al gepakt")
                                            continue

                                        #Je sluit de koelkast
                                        elif "sluit" in action or "dicht" in action:
                                            time.sleep(0.5)
                                            print("Je doet de koelkast dich")
                                            break

                                        elif "maak" in action or "tosti" in action:
                                            time.sleep(0.5)
                                            break

                                        else:   
                                            print("Dat is geen commando")                 
                                            continue 

                                #Je pakt de sleutel
                                if "sleutel" in action and "pak" in action:
                                    time.sleep(0.5)
                                    print("Je pakt de sleutel van de keukentafel")
                                    inventory.append("sleutel")
                                    print("Sleutel toegevoegd aan inventory")
                                    continue
                                
                                #Je maakt de tosti
                                elif "maak tosti" in action or "maak" in action or "tosti" in action:

                                    #De maak tosti loop
                                    while True:

                                        #Je hebt geen tosti ijzer
                                        if not "tostiIjzer" in inventory:
                                            time.sleep(0.5)
                                            print("Je hebt geen tosti ijzer, dus je kan geen tosti maken...")
                                            time.sleep(2)
                                            print("Misschien hebben de buren een tosti ijzer?")
                                            time.sleep(1)
                                            weetVanToaster = True
                                            action = ""
                                            break

                                        #Je hebt geen kaas
                                        elif not "kaas" in inventory:
                                            time.sleep(0.5)
                                            print("Je hebt geen kaas voor je tosti")
                                            time.sleep(1)
                                            print("Misschien ligt er wat in de koelkast?")
                                            action = ""
                                            break
                                        
                                        #Je hebt geen brood
                                        elif not "brood" in inventory:
                                            time.sleep(0.5)
                                            print("Je hebt geen brood voor je tosti..")
                                            time.sleep(1)
                                            print("Misschien ligt er wat in de koelkast?")
                                            action = ""
                                            break

                                        #Je hebt alleen maar kaas en ham
                                        elif not "ham" in inventory and not "curry" and not "melk" in inventory:
                                            print("Je maakt je tosti")
                                            time.sleep(1)
                                            print("Hij smaakt wel een beetje saai..")
                                            time.sleep(1)
                                            print("Wat ham en curry zou lekker zijn geweest")
                                            exit()

                                        #Er zit melk op je tosti    
                                        elif "melk" in inventory:
                                            time.sleep(0.5)
                                            print("Je eet je tosti op")
                                            time.sleep(1)
                                            print("Je sterft omdat je lactose intollerant bent en er zit melk op je tosti")
                                            time.sleep(3)
                                            print("Misschien geen melk pakken...")
                                            exit()
                                        
                                        #Je mist curry
                                        elif not "melk" in inventory and not "curry" in inventory:
                                            time.sleep(0.5)
                                            print("Je eet je tosti op")
                                            time.sleep(1)
                                            print("Hij is lekker, maar er mist wat...")
                                            time.sleep(1)
                                            print("Misschien wat curry erbij de volgende keer")
                                            exit()
                                        
                                        #Je mist ham
                                        elif not "melk" in inventory and not "ham" in inventory:
                                            time.sleep(0.5)
                                            print("Je eet je tosti op")
                                            time.sleep(1)
                                            print("Hij is redelijk lekker, maar er mist wat")
                                            time.sleep(1)
                                            print("Misschien wat ham erbij de volgende keer...")
                                            exit()

                                        #Je hebt alles
                                        else:
                                            time.sleep(0.5)
                                            print("Je eet je tosti")
                                            time.sleep(1)
                                            print("Hij is heerlijk!")
                                            time.sleep(1)
                                            print("Beter kan gewoon niet!")
                                            time.sleep(1)
                                            print("True ending gehaald")
                                            exit()
                                            

                                #Je loopt de keuken uit
                                elif "uit" in action and "keuken" in action:
                                    time.sleep(0.5)
                                    print("Je loopt de keuken uit")
                                    time.sleep(1)
                                    break

                                else:   
                                    print("Dat is geen commando")                 
                                    continue 
                        else:   
                            print("Dat is geen commando")
                            time.sleep(0.5)
                            print("Probeer dingen als 'maak tosti' of 'open koelkast'")                     
                            continue 
                else:   
                    print("Dat is geen commando")
                    time.sleep(0.5)
                    print("Probeer dingen als 'ga naar beneden' of 'ga naar de wc'")                 
                    continue   
        else:   
            print("Dat is geen commando")
            time.sleep(0.5)
            print("Probeer dingen als 'zet pc aan' of 'loop uit de kamer' ")                
            continue        

#intro
print("Hallo en welkom bij mijn hoge qualiteit spel waar je een tosti moet maken!")
time.sleep(3)
print("(Of sterft op verschillende manieren)")
time.sleep(1)
print("de commando's in dit spel zijn heel simpel(zoals 'maak tosti', of 'Loop naar beneden')")
time.sleep(3)
print("Je moet alles in kleine leters typen, dus geen hoofdletters")
time.sleep(2)

#Startcommando
while True:
    print("Typ start om te starten")
    startCommando = input(">>")
    if startCommando == "start": startGame()
      
    elif startCommando == "Start" or startCommando == "START" and falseStart == 0:
        falseStart += 1
        time.sleep(0.5)
        print("Wat zei ik nou net?")
    elif startCommando == "Start" or startCommando == "START" and falseStart == 1:
        falseStart += 1
        time.sleep(0.5)
        print("...")
        time.sleep(1)
        print("TYP START ZONDER HOOFDLETTER")
    elif startCommando == "Start" or startCommando == "START" and falseStart == 2:
    
        falseStart += 1
        time.sleep(0.5)
        print("Weet je wat? laat maar")
        time.sleep(1)
        print("Ik wil niet dat je mijn spel speelt")
        time.sleep(1)
        print("Doei")
        exit()
    else:   
        print("Dat is geen commando")                 
        continue  