
# Step 1: Input six numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))
e = float(input("Enter fifth number: "))
f = float(input("Enter sixth number: "))

# Step 2: Find the smallest value
if a <= b and a <= c and a <= d and a <= e and a <= f:
    smallest = a
elif b <= a and b <= c and b <= d and b <= e and b <= f:
    smallest = b
elif c <= a and c <= b and c <= d and c <= e and c <= f:
    smallest = c
elif d <= a and d <= b and d <= c and d <= e and d <= f:
    smallest = d
elif e <= a and e <= b and e <= c and e <= d and e <= f:
    smallest = e
else:
    smallest = f

# Step 3: Find the largest value
if a >= b and a >= c and a >= d and a >= e and a >= f:
    largest = a
elif b >= a and b >= c and b >= d and b >= e and b >= f:
    largest = b
elif c >= a and c >= b and c >= d and c >= e and c >= f:
    largest = c
elif d >= a and d >= b and d >= c and d >= e and d >= f:
    largest = d
elif e >= a and e >= b and e >= c and e >= d and e >= f:
    largest = e
else:
    largest = f

# Step 4: Find the four middle numbers
if a != smallest and a != largest:
    first_middle = a
elif b != smallest and b != largest:
    first_middle = b
elif c != smallest and c != largest:
    first_middle = c
elif d != smallest and d != largest:
    first_middle = d
elif e != smallest and e != largest:
    first_middle = e
else:
    first_middle = f

if b != smallest and b != largest and b != first_middle:
    second_middle = b
elif c != smallest and c != largest and c != first_middle:
    second_middle = c
elif d != smallest and d != largest and d != first_middle:
    second_middle = d
elif e != smallest and e != largest and e != first_middle:
    second_middle = e
else:
    second_middle = f

if c != smallest and c != largest and c != first_middle and c != second_middle:
    third_middle = c
elif d != smallest and d != largest and d != first_middle and d != second_middle:
    third_middle = d
elif e != smallest and e != largest and e != first_middle and e != second_middle:
    third_middle = e
else:
    third_middle = f

if d != smallest and d != largest and d != first_middle and d != second_middle and d != third_middle:
    fourth_middle = d
elif e != smallest and e != largest and e != first_middle and e != second_middle and e != third_middle:
    fourth_middle = e
else:
    fourth_middle = f

# Step 5: Compute the median as the average of the 3rd and 4th smallest numbers
median = (third_middle + fourth_middle) / 2

# Step 6: Print the result
print("The median is:", median)

