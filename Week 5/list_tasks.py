def movement():
    path = ["Move Forward", "Move Backwards", "Move Left", "Move Right"]
    return path

def menu():
    print("Please enter a direction")
    directions = movement()
    for index in range(len(directions)):
        print(f"{index}: {directions[index]}")
    index = int(input())
    return directions[index]

def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")

if __name__ == "__main__":
    run()
