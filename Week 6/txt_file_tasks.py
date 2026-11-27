import os
def cwd():
    path = os.getcwd()
    print(f"Current working directory is {path}")
    print(f"Directory contains the following files: {os.listdir(path)}")

def run():
    print("Processing")
    cwd()

if __name__ == "__main__":
    run()