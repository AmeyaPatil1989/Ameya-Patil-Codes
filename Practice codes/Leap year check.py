start = int(input("Enter start year: "))
last = int(input("Enter end year: "))

for year in range(start, last+1):
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

