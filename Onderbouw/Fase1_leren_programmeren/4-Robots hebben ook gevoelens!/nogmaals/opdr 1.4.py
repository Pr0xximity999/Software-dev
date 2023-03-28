dag = input("Zeg een dag van de week>>")
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

i = 0
while True:
    if dag == dagen[i - 1]: exit()
    print(dagen[i])
    i += 1