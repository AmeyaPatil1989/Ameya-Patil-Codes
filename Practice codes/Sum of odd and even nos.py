number = int(input("Enter a number: "))

oddnum = 0
evennum = 0

while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        evennum +=digit
    else:
        oddnum +=digit
    number//=10

print("Sum of even digits = ", evennum)
print("Sum of odd digits = ", oddnum)