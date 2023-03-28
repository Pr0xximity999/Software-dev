from time import sleep
with open('README.md', 'r')as file:
    for i in file.readlines()[1 : -1]:
        print(i)
        sleep(1)