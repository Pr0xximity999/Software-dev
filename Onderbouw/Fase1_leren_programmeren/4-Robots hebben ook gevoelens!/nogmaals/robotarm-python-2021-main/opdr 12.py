from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for i in range(0, 9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for x in range(0, 10 - i):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0, 8 - i):
            robotArm.moveLeft()
    else: 
        robotArm.drop()    
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()