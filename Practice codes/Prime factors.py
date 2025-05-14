start = int(input("Enter start of range: "))
last = int(input("Enter end of range: "))

for i in range(start, last+1):
    print(f"\nThe factors of the numbers for {i} are :", end=' ')
    factor = 2
    temp = i
    while temp > 1:
        if temp % factor == 0:
            print(factor, end =' ')
            temp//=factor
        else:
            factor+=1
i+=1