from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:


for i in range(0, 10):
    robotArm.grab()
    color = robotArm.scan()
    if color == "blue":
        for x in range(1, 10 - i):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(1, 9 - i):
            robotArm.moveLeft()
    else: robotArm.moveRight(); color = ""


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()