# Prime numbers

start = int(input("Enter first number of the range"))
last = int(input("Enter last number of the range"))

counter = 0

for i in range(start, last+1):
    if i > 1:
        divisor = 2
        prime = True

        while divisor < i:
            if i%divisor==0:
                prime = False
                break
            divisor+=1
        if prime:
            print(i)