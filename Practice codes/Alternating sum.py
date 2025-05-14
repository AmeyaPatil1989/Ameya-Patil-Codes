number = int(input("Enter a number till where you want the calculate: "))

total = 0
for i in range(1, number+1):
    if i%2==1:
        total+=i
    else:
        total-=i
print(f"Alternating sum value = ", total)
