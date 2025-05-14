# ask user to provide a number that calculates the factorial

# value = int(input("Enter value:"))
# i = 1
# total = 1
# if value < 0:
#     print("Enter a positive value")
# else:
#     while i<value:
#         total = total * i
#         i+=1

# print("factorial is", total)


product = 1
count = 1
countnon = 0
while True:
    n = input("please provide an input")

    if n.lower()=="exit":
        print("thanks for playing the game!")
        break

    elif n.isnumeric():
        while count <= int(n):
            product = product * count
            count+=1
        print("the product is:", product)
        print("the count is:", count)
    else:
        print("yout input is not a number")
        pass
    print(countnon)