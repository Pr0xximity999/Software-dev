from random import shuffle
cardType = ["aas", "heer", "vrouw", "boer", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
cardVariant = ["schoppen", "klaver", "ruiten", "harten"]
def makedeck():
    cards = ["joker", "joker"]
    for t in cardType:
        for v in cardVariant:
            cards.append(f"{t} {v}")
    return cards
cards = makedeck()
shuffle(cards)   
for i in range(7):
    print(cards.pop(i))
print(cards)
      


