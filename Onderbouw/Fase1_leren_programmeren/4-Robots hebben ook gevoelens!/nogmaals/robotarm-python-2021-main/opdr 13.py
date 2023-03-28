from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.speed = 3
robotArm.randomLevel(1,7)
color = ""
# Jouw python instructies zet je vanaf hier:
for i in range(0, 7):
    robotArm.grab()
    color = robotArm.scan()
    if color == "": break
    for x in range(0, 1 + i):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(0, 1 + i):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()