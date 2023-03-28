mannenSnor = 0
vrouwenHaarKleur = ""
vrouwenHaarLen = 0

print("-----------------------------------------------------")
print("Hallo, en welkom bij dit sollicitatie gesprek!      |")
print("----------------------------------------------------|")
print("We gaan u een paar vragen stellen                   |")
print("Beandwoord deze erijk en simpel en in kleine letters|")
print("-----------------------------------------------------")
naam = input("Wat is uw naam? ")
dierendressuur = int(input("hoeveel jaar praktijkervaring met dieren-dressuur heeft u? " ))
jongleren = int(input("hoeveel jaar ervaring jongleren heeft u? " ))
acrobatiek = int(input("hoeveel jaar praktijkervaring met acrobatiek heeft u? " ))
diploma = input("Welk diploma heeft u? (niveau en soort) " )
vrachtWagenBewijs = input("Heeft u een geldig vrachtwagenbewijs? y/n ")
heeftHogeHoed = input("Heeft u een hoge hoed? y/n ")
gender = input("Bent u geboren als man of vrouw " )
if gender == "man":
    mannenSnor = int(input("Hoelang is uw snor(Als u die heeft)? " ))
elif gender == "vrouw":
    vrouwenHaarLen = int(input("Hoelang is uw haar? " ))
    vrouwenHaarKleur = input("Welke kleur is uw haar? " )
else:
    print("dat gender kennen wij niet dus u moet wel een alien zijn!")
    exit()
lengte = input("Hoe lang bent u in cm? ")
gewicht = int(input("Hoe zwaar bent u in kg? "))
certificaat = input("Heeft u een certificaat, zo ja welke? ")
leeftijd = int(input("Hoe oud bent u?  "))
lievelingskleur = input("Wat is uw lievelingskleur? ")
speeltFortnite = input("Speelt u fortnite? y/n ")


if (dierendressuur >= 4 or jongleren >= 5 or acrobatiek >= 3) and diploma == "mbo 4 ondernemen" and vrachtWagenBewijs == "y" and heeftHogeHoed == "y" and(mannenSnor >=  10 or (vrouwenHaarKleur == "rood" and  vrouwenHaarLen < 20 ) and lengte >= 150 and gewicht >= 90 and  certificaat == "overleven met gevaarlijk personeel"):
    print(f"Gefeliciteerd {naam}, u komt in aanmerking!")
    print("U komt nu in aanmerking voor een solicitatiegesprek en mag uw cv opsturen")
    input()
    exit()
else:
    print("Helaas, u bent niet aangenomen omdat u niet in aanmerking komt!")
    input()
    exit()
