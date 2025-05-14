print("Co-prime numbers with 20 from range 1-20")

for i in range(1,21):
    factor = 1
    for divisor in range(2, i + 1):
        if i % divisor == 0 and 20 % divisor == 0:
            factor = divisor
        
    if factor==1:
        print(f"{i} is coprime with 20")
    else:
        print(f"{i} is not  
            coprime with 20")
i+=1
