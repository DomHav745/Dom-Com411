print("Program Started")
print("Please enter an ASCII code")
code = int(input())
if code >= 32 and code <= 126:
    print(f"The character represented by the ASCII code {code} is {chr(code)}")
else:
    print("Error. Please enter a number between 32 and 126")
print("Program Ended")
