import time
seconde = 30
while True:
    if seconde == 0: print("Blastoff!"); exit()
    print(f"{seconde}..")
    time.sleep(1)
    seconde -= 1