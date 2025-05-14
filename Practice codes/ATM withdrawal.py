daily_limit = 500  # Maximum total withdrawal limit
total_withdrawn = 0  # Track total withdrawals

while True:
    print(f"\nTotal withdrawn today: ${total_withdrawn} / ${daily_limit}")
    amount = int(input("Enter the withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount! Please enter a positive amount.")
    elif total_withdrawn + amount > daily_limit:
        print(f"Limit reached! You can only withdraw up to ${daily_limit - total_withdrawn} more.")
    else:
        total_withdrawn += amount
        print(f"Transaction successful! You have withdrawn ${amount}.")
    
    # Stop further transactions if limit is reached
    if total_withdrawn >= daily_limit:
        print("Daily limit reached! No more transactions allowed.")
        break

    # Ask for another transaction
    another_transaction = input("Do you want another transaction? (yes/no): ").strip().lower()
    
    if another_transaction != "yes":
        print("Thank you for using the ATM. Have a great day!")
        break  # Exit the loop if the user does not want another transaction
