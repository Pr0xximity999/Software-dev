from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for i in range(0, 8):
    for x in range(0, 9):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(0, 8):
        robotArm.moveLeft()
    robotArm.grab()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()