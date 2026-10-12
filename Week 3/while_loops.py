print ("How many Obstacles should I avoid?")
Obstacles = int(input())
count = 1
while count <= Obstacles:
    print("Avoiding...", end ="")
    print (f"Done! {count} Obstacles avoided.")
    count += 1
print ("All obstacles have been avoided!")