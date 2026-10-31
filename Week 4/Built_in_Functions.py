print("Program Started!")
print("Please enter an ASCII code")
Number = int(input())
if Number >= 32 and Number <= 126:
    print(f"The character represented by the ASCII value {Number} is {chr(Number)}")
else:
    print("The character cannot be displayed")
print("The program has ended")
