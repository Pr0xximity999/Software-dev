from RobotArm import RobotArm

robotArm = RobotArm('assessment1')
robotArm.speed=4

# Jouw python instructies zet je vanaf hier:
def moveArm(movement:str):
    movementList = movement.split(', ')
    for i in range(len(movementList)):
        if movementList[i][0] == "l":
            for i in range(int(movementList[i][1])):
                robotArm.moveLeft()
        elif movementList[i][0] == "r":
            for i in range(int(movementList[i][1])):
                robotArm.moveRight()
        elif movementList[i][0] == "g":
            robotArm.grab()
        elif movementList[i][0] == "d":
            robotArm.drop()
#The left column
moveArm("r4, g, l3, d, r3, g, l3, d, r3, g, l4, d, r1, g, l1, d, r1, g, l1, d")
#The right column
moveArm("r5, g, r3, d, l3, g, r3, d, l3, g, r4, d, l1, g, r1, d, l1, g, r1, d")

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()