def table(num:int = 0):
    for i in range(1, 11):
        print(f"{i} X {num} is {i * num}")

number = int(input("Type a whole number >>"))
table(number)
input("Press any key to exit..")
