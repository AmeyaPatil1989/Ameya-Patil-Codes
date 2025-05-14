num1 = float(input("Enter first number:"))
num2 = float(input("Enter first number:"))
num3 = float(input("Enter first number:"))
num4 = float(input("Enter first number:"))
num5 = float(input("Enter first number:"))
num6 = float(input("Enter first number:"))

if num1>=num2 and num1>=num3 and num1>=num4 and num1>=num5 and num1>=num6:
    l = num1
elif num2>=num1 and num2>=num3 and num2>=num4 and num2>=num5 and num2>=num6:
    l = num2
elif num3>=num1 and num3>=num2 and num3>=num4 and num1>=num5 and num3>=num6:
    l = num3
elif num4>=num1 and num4>=num2 and num4>=num3 and num4>=num5 and num4>=num6:
    l = num4
elif num5>=num1 and num5>=num2 and num5>=num3 and num5>=num4 and num5>=num6:
    l = num5
else:
    l = num6

if num1<=num2 and num1<=num3 and num1<=num4 and num1<=num5 and num1<=num6:
    s = num1
elif num2<=num1 and num2<=num3 and num2<=num4 and num2<=num5 and num2<=num6:
    s = num2
elif num3<=num1 and num3<=num2 and num3<=num4 and num1<=num5 and num3<=num6:
    s = num3
elif num4<=num1 and num4<=num2 and num4<=num3 and num4<=num5 and num4<=num6:
    s = num4
elif num5<=num1 and num5<=num2 and num5<=num3 and num5<=num4 and num5<=num6:
    s = num5
else:
    s = num6

if num1 != l and num1 != s:
    mid1 = num1
elif num2 != l and num2 != s:
    mid1 = num2
elif num3 != l and num3 != s:
    mid1 = num3
elif num4 != l and num4 != s:
    mid1 = num4
elif num5 != l and num5 != s:
    mid1 = num5
else:
    mid1 = num6

if num2 != l and num2 != s and num2 != mid1:
    mid2 = num2
elif num3 != l and num3 != s and num3 != mid1:
    mid2 = num3
elif num4 != l and num4 != s and num4 != mid1:
    mid2 = num4
elif num5 != l and num5 != s and num5 != mid1:
    mid2 = num5
else:
    mid2 = num6

if num3 != l and num3 != s and num3 != mid1 and num3 != mid2:
    mid3 = num3
elif num4 != l and num4 != s and num4 != mid1 and num4 != mid2:
    mid3 = num4
elif num5 != l and num5 != s and num5 != mid1 and num5 != mid2:
    mid3 = num5
else:
    mid3 = num6


if num4 != l and num4 != s and num4 != mid1 and num4 != mid2 and num4 != mid3:
    mid4 = num4
elif num5 != l and num5 != s and num5 != mid1 and num5 != mid2 and num4 != mid3:
    mid4 = num5
else:
    mid4 = num6

median = (mid3 + mid4)/2

print("The median is :", median)
