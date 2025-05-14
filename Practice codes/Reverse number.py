num = int(input("Enter a number: "))
revnum = 0

while num > 0:
    i = num % 10
    revnum = revnum * 10 + i
    num //= 10

print(f"Reversed number is: {revnum}")

if revnum % 2 == 0:
    print("Reversed number is even")
else:
    print("Reversed number is odd")
