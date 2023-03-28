from RobotArm import RobotArm

robotArm = RobotArm('assessment2')
robotArm.speed=1

# Jouw python instructies zet je vanaf hier:
def moveArm(direction:str, length:int):
    if direction == "right":
        for i in range(length):
            robotArm.moveRight()

    elif direction == "left":
        for i in range(length):
            robotArm.moveLeft()

def moveBlock(direction:str, length:int):
    robotArm.grab()
    if direction == "right":
        for i in range(length):
            robotArm.moveRight()  
        robotArm.drop()
        for i in range(length):
            robotArm.moveLeft()
    elif direction == "left":
        for i in range(length):
            robotArm.moveLeft()
        robotArm.drop()
        for i in range(length):
            robotArm.moveRight()

# Onderstaande code pas je NIET aan
moveArm("right", 3)
moveBlock("left", 3)
moveBlock("right", 6)
moveBlock("right", 2)
moveBlock("right", 6)
moveBlock("left", 1)
moveBlock("left", 3)

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()