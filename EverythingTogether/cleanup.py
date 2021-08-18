from config import load_options
import os
import shutil

def cleanup():
    del_temp()
    move_files()

def del_temp():
    os.chdir("Temp")
    files = os.listdir()
    for file in files:
        os.remove(file)
    os.chdir("..")

def move_files():
    where_to = load_options().get("directory")
    files = os.listdir("Archive")
    print(files)
    for f in files:
        shutil.move(os.path.join("Archive", f),os.path.join(where_to,f))