def display_chars():
    with open("library.txt", "r") as file:
        print(file.readlines(0))

display_chars()
