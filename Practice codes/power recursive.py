def power(a,b):
    b=int(b)
    if b == 0:
        return 1
    elif b > 0:
        return a * power(a, b-1)
    else:
        return 1/(a*power(a,-b-1))

num = int(input())
pow = float(input())
print(power(num, pow))