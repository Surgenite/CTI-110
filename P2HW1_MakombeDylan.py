# Dylan Makombe
# 10/17/2024
# P2HW1
# This program calculates and displays travel expenses

# Display "This program calculates and displays travel expenses"
print("This program calculates and displays travel expenses")

# Declare Integer budget,
# Display "Enter budget: ", Input budget
budget = int(input("Enter Budget: "))

# Declare String travelDestination
# Display "Enter your travel destination: ", Input travelDestination
travel_destination = str(input("Enter your travel destination: "))

# Declare Integer gas, accommodation, food
# Display "How much do you think you will spend on gas? " Input gas
# Display "Approximately, how much will you need for accommodation/hotel? " Input accommodation
# Display "Last, how much do you need for food? " Input food
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

# Declare Integer expenses
# Set expenses = gas + accommodation + food
expenses = gas + accommodation + food

# Declare Integer result
# Set result = budget - expenses
result = budget - expenses

# Display Travel Expenses
print()
print("------------Travel Expenses------------")
print(f"{'Location:':<20}{travel_destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${accommodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("-" * 60)
print()
print(f"{'Remaining Balance:':<20}${result:,.2f}")

