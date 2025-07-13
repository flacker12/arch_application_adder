import os
import sys

path = os.getcwd()
file = sys.argv[1]
user = os.getlogin()

name=input("Enter the name of application: ")


os.system(f"touch /home/{user}/.local/share/applications/{file}.desktop")
os.system(f'echo "[Desktop Entry]\nExec={path}/{file}\nName={name}\nType=Application" > /home/{user}/.local/share/applications/{file}.desktop')
print("done")
