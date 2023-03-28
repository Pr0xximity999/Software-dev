import random
newDeck = list()
cardType = ["aas", "heer", "vrouw", "boer", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
cardVariant = ["schoppen", "klaver", "ruiten", "harten"]
cards = list()
jokeraantal = 2

for i in cardVariant:
    for x in cardType:
        cards.append(i+ " " + x)

    cards.append("joker")
    cards.append("joker")

def randomizeDeck():
    for i in range(54):
        usednums = list()
        while True:
            ranNum = random.randint(0,54)
            for i in usednums:
                if ranNum in i: continue
            usednums.append(ranNum)
            break
        newDeck.append(cards[ranNum])

def printDeck():
    for i in range(1, 8):
        print(f"Kaart {i}: {newDeck[i]}")
        newDeck.remove(newDeck[i])
    print(f"Deck ({len(newDeck)}): {newDeck}")
    
randomizeDeck()
printDeck()