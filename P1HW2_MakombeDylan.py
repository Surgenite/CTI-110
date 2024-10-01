# Dylan Makombe
# 9/26/2024
# P1HW2
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
print("---------Travel Expenses--------")
print("Location:", travel_destination)
print("Initial Budget: ", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", result)

