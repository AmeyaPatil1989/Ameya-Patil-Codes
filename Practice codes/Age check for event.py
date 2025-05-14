not_allowed = 0
allowed_with_guardian = 0
allowed = 0

while True:
    age = int(input("Enter person's age (-1 to exit): "))
    
    if age == -1:
        break  # Exit condition
    
    if age < 18:
        print("❌ Entry not allowed (Underage).")
        not_allowed += 1
    elif 18 <= age < 21:
        accompanied = input("Accompanied by someone 21 or older? (yes/no): ").lower()
        if accompanied == 'yes':
            print("✅ Entry allowed (Accompanied).")
            allowed_with_guardian += 1
        else:
            print("❌ Entry not allowed (Unaccompanied).")
            not_allowed += 1
    else:
        print("✅ Entry allowed. Welcome!")
        allowed += 1

print("\nEntry Summary:")
print(f"Underage : {not_allowed}")
print(f"Ages 18-20 allowed with guardian: {allowed_with_guardian}")
print(f"Ages 21 and above: {allowed}")
