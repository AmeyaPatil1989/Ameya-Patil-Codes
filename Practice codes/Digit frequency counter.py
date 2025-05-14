start = int(input("Enter start of range"))
last = int(input("Enter end of range"))

print(f"Count frequency of digits from 0-9 in numbers between {start}-{last}")

for i in range(0,10):
    counter =0
    for j in range(start, last+1):
        while j>0:
            digit = j%10
            if digit == i:
                counter+=1
            j//=10
    print(f"The number {i} appers {counter} times")