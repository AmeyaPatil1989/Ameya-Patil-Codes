# Repeat Numbers:
# Use a for loop to iterate numbers 1 to 5, and a nested while loop to print each number repeatedly 
# (number of times = number itself)

start = 1
last = 5

for i in range(start, last+1):
    counter = 0
    while counter < i:
        print(i, end=" ")
        counter+=1
    print()