
while True:
    value = input("Enter a positive value: ")
    
    if value.isnumeric() and value.isnumeric() > 0:
        print("the number {} is positive".format(value))
        break
    else:
        print("Enter positive value again")

