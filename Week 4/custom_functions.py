def sum_weights(character, inventory):
    total_weight = character + inventory
    return total_weight

def avg_weights(character, inventory):
    average_weight = sum_weights(character, inventory) / 2
    return average_weight

def run():
    print("What is the weight of the character?")
    character = float(input())
    print("What is the weight of the inventory?")
    inventory = float(input())
    print("What would you like to calculate, sum or average?")
    action = input()
    if action == "sum":
        answer = sum_weights(character, inventory)
        print(f"The sum of weights is...{answer}")
    elif action == "average":
        answer = avg_weights(character, inventory)
        print(f"The average of weights is...{answer}")
    else:
        print("I'm not sure what you mean")
run()