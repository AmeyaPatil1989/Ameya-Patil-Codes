first = 1
last = 20
counter = 0
for i in range(first, last+1):
    if i%2==0:
        print(i)
        counter+=1
    i+=1
print("Total even nos: ", counter)