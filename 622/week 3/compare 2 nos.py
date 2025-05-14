x0= float(input("Enter 1st nomber:"))
x1= float(input("Enter 2nd nomber:"))
x2= float(input("Enter 3rd nomber:"))

if x0>x1:
    if x0>x2:
        print("1st number is greatest")
    else:
        print("3rd number is the greatest")
elif x1>x2:
        print("2nd is the greatest")
else:
     print(" 3rd is the greatest")