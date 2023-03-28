from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

for i in range(0, 3):
    robotArm.grab()
    for x in range(0, 3 - i):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(0, 3 - i):
        robotArm.moveLeft()
robotArm.moveRight()
for i in range(0, 3):
    for x in range(0, 0 + i):
        robotArm.moveRight()
    robotArm.grab()
    for x in range(0, 0 + i):
        robotArm.moveLeft()
    robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()