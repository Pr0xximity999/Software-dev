a = int(input("Geef me een heel getal: "))
b = int(input("Geef me nog een heel getal: "))

if a > b:
    max = a
    min = b
    print(f"a is het grootste getal: {max}")
    print(f"Het minimum is {min} en het maximum {max}")
elif a < b:
    max = b
    min = a
    print(f"a is het kleinste getal: {min}")
    print(f"Het minimum is {min} en het maximum {max}")
else:
    max = b
    min = a
    print("a en b zijn even groot")
    print(f"Het minimum is {min} en het maximum {max}")
