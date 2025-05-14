# number = int(input("Enter the number "))

# a=0
# b=1


# print(f"The number {number} is ")

# while b < number:
#     c=b+a
#     a=b
#     b=c
    
# if b == number or number == 0:
#     print("Fibonacci number")
# else:
#     print("Not a fibonacci number")


# def fib(n):
#     if n<0:
#         print("Incorrect input")
#         return
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         a,b=0,1
#         for i in range(n-2):
#             a,b=b,a+b
#         return b

def fibRec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibRec(n-1) + fibRec(n-2)

def main():
    n = int(input("Enter the number of terms: "))
    print(fibRec(n))

if __name__ == "__main__":
    main()
