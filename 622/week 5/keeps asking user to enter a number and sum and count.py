# keeps asking user to enter a number until user types in exit 
# and count the number of times user has enters numbers and sums the values

i = 0
total = 0

while True: 
    value = input("Enter Value or type exit to stop:")

    if value.lower()=="exit":
        print("thanks for entering the values!")
        break
    elif value.isnumeric():
        i+=1
        total = total + float(value)
    else:
        print("your input is invalid")
        pass


print(i," ", total)

