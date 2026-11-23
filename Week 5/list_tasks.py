def movement():
    path = ["Move Forward", "Move Backwards", "Move Left", "Move Right"]
    return path

def menu():
    print("Please enter a direction")
    directions = movement()
    for index in range(len(directions)):
        print(f"{index}: {directions[index]}")
def run():
    menu()

if __name__ == "__main__":
    run()
