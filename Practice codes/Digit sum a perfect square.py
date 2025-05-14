start = int(input("Enter start of range: "))
last = int(input("Enter a end of range: "))

for x in range(start, last+1):
    digitsum = 0
    temp = x
    
    while temp > 0:
        digitsum += temp%10
        temp//=10

    sqrchk = 1
    while sqrchk * sqrchk <= digitsum:
        if sqrchk * sqrchk == digitsum:
            print(f"{x} is a number whose sum of digits is a perfect square")
            print(f"Sum of the digits is {digitsum}")
            print(f"Sum of the digits is a perfect square of {sqrchk}")
            break
        sqrchk+=1
