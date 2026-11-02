import os

def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print(f"The directory contains the following files: \n{os.listdir(path)}")
cwd()

def run():
    print("Processing...")
    cwd()
run()
