bill_amount = float(input("Enter the bill amount: $"))
num_people = int(input("Enter number of people splitting the bill: "))

# Determine appropriate tip percentage
if bill_amount < 50:
    tip_percent = 0.10
elif bill_amount < 150:
    tip_percent = 0.15
else:
    tip_percent = 0.18

tip_amount = bill_amount * tip_percent
total_amount = bill_amount + tip_amount
per_person = total_amount / num_people

print(f"\n Bill Amount: ${bill_amount:.2f}")
print(f" Tip ({int(tip_percent*100)}%): ${tip_amount:.2f}")
print(f" Total amount with tip: ${total_amount:.2f}")
print(f" Each person pays: ${per_person:.2f}")
