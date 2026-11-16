print("Programme Started")
print("Please enter a character")
character = input()
if len(character) == 1:
    print(f"The ASCII code for {character} is: {ord(character)}")
else:
    print("Error. Only 1 character required")
print("Program Ended")
