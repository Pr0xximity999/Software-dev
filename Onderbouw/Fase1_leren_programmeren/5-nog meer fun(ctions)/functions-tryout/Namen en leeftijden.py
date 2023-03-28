def naamEnLeeftijd(naam:str, leeftijd:int):
    print(f"Hallo {naam}, je leeftijd is {leeftijd} jaar") 
       
while True:
    invoerNaam = input("Wat is je naam? >>")
    if invoerNaam == "stop": exit()
    invoerLeeftijd = input("Hoe oud ben je? >>")
    if invoerLeeftijd == "stop": exit()
    invoerLeeftijd = int(invoerLeeftijd)
    naamEnLeeftijd(invoerNaam, invoerLeeftijd)  