
string = input("Enter a string: ")

print("ASCII values:")
for char in string:
    ascii_val = ord(char)
    print(f"{char}: {ascii_val}")