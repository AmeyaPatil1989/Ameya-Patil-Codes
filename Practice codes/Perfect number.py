number = int(input("Enter a number:  "))
sumofdivisor=0
for i in range(1, number):
    if number%i==0:
        sumofdivisor+=i

if sumofdivisor == number:
    print("{} is a perfect number".format(number))
else:
    print("{} is not a perfect number".format(number))
