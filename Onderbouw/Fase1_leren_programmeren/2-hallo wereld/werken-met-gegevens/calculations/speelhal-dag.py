personen = float(input("Hoeveel vrienden heb je(plus jezelf):"))
speelHalKosten = 7.45
vrSeatKosten = 0.37
tijdVr = float(input("Voor hoeveel minuten wil je deze realiteit ontsnappen: "))

kosten = personen * (speelHalKosten + (tijdVr / 5) * vrSeatKosten)
print("De dag kost in totaal een geweldige, supere, toffe, leuke, hilarische " + str(kosten) + " euro als je met " + str(personen) + " bent en ze allemaal " + str(tijdVr) + " minuten in de vr booth zitten!")
#negeer de .00000000000000000000005