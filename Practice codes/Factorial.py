# num = int(input("Enter number"))
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)

# def factorial(n):
#     if n==0:
#         return 1
#     result = 1
#     for i in range (1, n+1):
#         result *= i
#     return result 

def factRec(n):
    if n==0:
        return 1
    else:
        return n * factRec(n-1)

def main():
    n = int(input("Enter a number"))
    print("Factorial of", n, "is", factRec(n))

if __name__ =="__main__":
    main()