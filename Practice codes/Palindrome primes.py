
print("Palindrome primes from 1-500")

for i in range(1, 501):
    reverse = 0
    temp = i
    while temp > 0:
        j = temp%10
        reverse = reverse * 10 + j
        temp//=10
    if reverse == i:
        if i > 1:
            divisor = 2
            prime = True
            while divisor < i:
                if i % divisor == 0:
                    prime = False
                    break
                divisor+=1
            if prime:
                print(f"{i} is palindrome and a prime number")
    i+=1
