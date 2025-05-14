number = int(input("Enter number"))

counter = 0

while number > 0:
    number = number // 10
    counter+=1

print(f"Digits = {counter}")

