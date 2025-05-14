string = input("Enter a string: ")
uppercase_count = 0

for i in string:
    if i >= 'A' and i <= 'Z':
        uppercase_count += 1

print(f" Number of uppercase letters: {uppercase_count}")