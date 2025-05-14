
def reverseCount(n):
    
    if n>0:
    def pos(n):
        print(n)
        pos(n-1)
    elif n<0:
    def pos(n):
        if n == 0:
            print("0 is a number")
            return
        else:
            print(n)
            pos(n-1)
        return

def main():
    num = int(input("Enter the number you want to start reversing: "))
    reverseCount(num)

if __name__ == '__main__':
    main()