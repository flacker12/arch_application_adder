import os
import sys

path = os.getcwd()
file = sys.argv[1]

name=input("Enter the name of application: ")


os.system(f"touch /home/daffuk/.local/share/applications/{file}.desktop")
os.system(f'echo "[Desktop Entry]\nExec={path}/{file}\nName={name}\nType=Application" > /home/daffuk/.local/share/applications/{file}.desktop')
print("done")
