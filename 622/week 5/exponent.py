# startValue=int(input("Please provide the number of start value:"))
# stopValue = int(input("Please provide the number of stop value:"))
# stepValue = int(input("Please provide the number of step value:"))
startNum = int(input("Please provide starting number:"))

# if startValue < 0:
#     iterationNum = abs(startValue)

# if stopValue < 0:
#     iterationNum = abs(stopValue)

if startNum < 0:
    startNum = abs(startNum)

product = 1

iterator = 1

for iterator in range(20, 0, 2):
    product = product * startNum * (iterator)
    print(product)