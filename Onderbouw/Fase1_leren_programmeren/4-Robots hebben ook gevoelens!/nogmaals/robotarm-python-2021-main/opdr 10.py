from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = 5
# Jouw python instructies zet je vanaf hier:

#Grote flex ik doe het in 11 lines lol
for i in range(0, 5):
    robotArm.grab()
    for x in range(0, 9 - i * 2):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(0, 8 - i * 2):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()