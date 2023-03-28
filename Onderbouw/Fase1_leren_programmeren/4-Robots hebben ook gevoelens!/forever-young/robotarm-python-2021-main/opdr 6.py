from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 3

def move(i, direction):
    if direction == "right":
        for x in range(0, i):
            robotArm.moveRight()
    if direction == "left":
        for x in range(0, i):
            robotArm.moveLeft()

# Jouw python instructies zet je vanaf hier:
move(7, "right")
for i in range(0, 8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    move(2, "left")




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()