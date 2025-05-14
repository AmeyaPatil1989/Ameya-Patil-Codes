# Count the number of fives

num = int(input("Enter a number: "))
count = 0
while num > 0:
    i = num % 10
    if i == 5:
        count+=1
    num //= 10

print(f"The number has {count} fives")

