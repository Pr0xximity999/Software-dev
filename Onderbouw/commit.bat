@echo off
set /p dirLoc=[Gimme the dir]
set /p msg=[Gimme a comment]

cd %dirLoc% 

git add -A

git commit -a -m %msg%

git push
