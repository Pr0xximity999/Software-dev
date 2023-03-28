from fileinput import close
import keyboard
f = open("keyReader.txt", "x")
f.close()
while True:
    if keyboard.read_key():
        f = open("keyreader.txt", "w")
        f.write(keyboard.read_key())
        f.close