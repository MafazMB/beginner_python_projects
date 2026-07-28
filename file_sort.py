import os

def req_dir():
    current_dir=os.getcwd()
    print(f"Current dir: {current_dir}")
    os.chdir("/Users/mafazmbn/Desktop/Mafaz")
    new_dir=os.getcwd()
    print(f"New dir: {new_dir}")

req_dir()