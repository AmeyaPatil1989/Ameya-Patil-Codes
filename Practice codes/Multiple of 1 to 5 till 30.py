# for i in range(1,6):
#     multiple = 1
#     while multiple <= 30:
#         product = multiple * i
#         print(f"{i} x {multiple} = {product} ")
#         multiple+=1
# i+=1

# Outer loop from 1 to 5
for num in range(1, 6):
    multiple = num
    print(f"Multiples of {num}:", end=' ')
    
    # Inner loop generates multiples up to 30
    while multiple <= 30:
        print(multiple, end=' ')
        multiple += num  # Increment by the current number to get next multiple
    
    print()  # Newline after each set of multiples
