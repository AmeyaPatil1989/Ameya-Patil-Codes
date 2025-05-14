total_vehicles = 0
total_revenue = 0
toll_fee = 10  # Flat fee per vehicle

while True:
    total_vehicles += 1
    total_revenue += toll_fee
    print(f"Vehicle {total_vehicles}: Paid ${toll_fee}. Total revenue: ${total_revenue}")

    another = input("Process another vehicle? (yes/no): ").strip().lower()
    if another != "yes":
        break

print(f"Total vehicles processed: {total_vehicles}, Total revenue: ${total_revenue}")
