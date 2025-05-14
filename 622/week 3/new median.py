
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
    fm1 = a
elif b != smallest and b != largest:
    fm1 = b
elif c != smallest and c != largest:
    fm1 = c
elif d != smallest and d != largest:
    fm1 = d
elif e != smallest and e != largest:
    fm1 = e
else:
    fm1 = f

if b != smallest and b != largest and b != fm1:
    fm2 = b
elif c != smallest and c != largest and c != fm1:
    fm2 = c
elif d != smallest and d != largest and d != fm1:
    fm2 = d
elif e != smallest and e != largest and e != fm1:
    fm2 = e
else:
    fm2 = f

if c != smallest and c != largest and c != fm1 and c != fm2:
    fm3 = c
elif d != smallest and d != largest and d != fm1 and d != fm1:
    fm3 = d
elif e != smallest and e != largest and e != fm1 and e != fm1:
    fm3 = e
else:
    fm3 = f

if d != smallest and d != largest and d != fm1 and d != fm2 and d != fm3:
    fm4 = d
elif e != smallest and e != largest and e != fm1 and e != fm2 and e != fm3:
    fm4 = e
else:
    fm4 = f

if fm1>fm2 and fm1>fm3 and fm1>fm4:
    biggest = fm1
elif fm2>fm1 and fm2>fm3 and fm2>fm4:
    biggest = fm2
elif fm3>fm1 and fm3>fm2 and fm3>fm4:
    biggest = fm3
else:
    biggest = fm4

if fm1<fm2 and fm1<fm3 and fm1<fm4:
    least = fm1
elif fm2<fm1 and fm2<fm3 and fm2<fm4:
    least = fm2
elif fm3<fm1 and fm3<fm2 and fm3<fm4:
    least = fm3
else:
    least = fm4

if fm1 != biggest and fm1 != least:
    m1 = fm1
elif fm2 != biggest and fm2 != least:
    m1 = fm2
elif fm3 != biggest and fm3 != least:
    m1 = fm3
else:
    m1 = fm4


if fm2 != biggest and fm2 != least and fm2 != m1:
    m2 = fm2
elif fm3 != biggest and fm3 != least and fm3 != m1:
    m2 = fm3
else:
    m2 = fm4




# Step 5: Compute the median as the average of the 3rd and 4th smallest numbers
median = (m1 + m2) / 2

# Step 6: Print the result
print("The median is:", median)

