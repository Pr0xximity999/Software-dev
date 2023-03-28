krosantjeAantal = float(input("Hoeveel kwaksons wilt gei kopen? >>"))
stokbroodAantal = float(input("Hoeveel broodstokken wil je aanschaffen? >>"))
kortingsbonAantal = float(input("Hoeveel bonnen met een neppe waarde heeft u in bezit? >>"))
krosantje = float(input("Hoeveel kost elk kwaksonnetje? >>"))
stokbrood = float(input("Hoeveel kost elk stokje brood? >>"))
kortingsbon = float(input("Hoeveel is de neppe kortingswaarde van die stukjes papier waard? >>"))

kosten = 17 * krosantje + 2 * stokbrood - 3 * kortingsbon
print("de kosten zijn " + str(kosten) + " euro, als je ")
print(str(krosantjeAantal) + " krosantjes en "+ str(stokbroodAantal)+" stokbroden koopt met "+ str(kortingsbonAantal)+" kortingsbonnen!")