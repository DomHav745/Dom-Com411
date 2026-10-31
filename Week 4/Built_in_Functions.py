print("Program Started")
print ("Please enter a standard character")
character = input()
if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("Error! Input must be 1 character")
print("Program Ended!")
