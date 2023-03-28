# name of student:
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #Vraagt naar het aantal wat de user betaald had moeten hebben
paid = int(float(input('Paid amount: ')) * 100) #Vraagt naar het aantal wat de user heeft betaald
change = paid - toPay #berekend het wisselgeld

if change > 0: #als er wisselgeld is, voer dit uit
  coinValue = 500 #Begin met het hoogste
  
  while change > 0 and coinValue > 0: #Als het wisselgeld en de waarde van de wisselmunten geen 0 zijn, loop dit
    nrCoins = change // coinValue #Berekent het aantal munten

    if nrCoins > 0 and coinValue <= 50: #Als de muntwaarde minder of gelijk is aan 50, voer dit uit(zodat het in centen word gelaten zien)
      print('return maximal ', nrCoins, ' coins of ', str(coinValue / 100), ' cents!' ) #Print het aantal munten van een waarde die je terug krijgt
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #Vraagt hoeveel van deze munt je terug geeft
      change -= nrCoinsReturned * coinValue #berekent de nieuwe waarde die je na dit nog terug moet geven

    if nrCoins > 0 and coinValue > 50: #Als de muntwaarde meer is dan 50, voer dit uit(zodat het in euro's word gelaten zien)
      print('return maximal ', nrCoins, ' coins of ', str(int(coinValue / 100)), ' euro!' ) #Print het aantal munten van een waarde die je terug krijgt
      nrCoinsReturned = int(input('How many coins of ' + str(int(coinValue / 100)) +  ' euro did you return? ')) #Vraagt hoeveel van deze munt je terug geeft
      change -= nrCoinsReturned * coinValue #berekent de nieuwe waarde die je na dit nog terug moet geven

# verlaagt de muntwaarde zodat er steeds en lagere muntwaarde word gevraagd
    if coinValue == 500:
        coinValue = 200
    elif coinValue == 200:
        coinValue = 100
    elif coinValue == 100:
        coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #als je nog een kleine waarde terug moet betalen, laat dat het hier zien
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')