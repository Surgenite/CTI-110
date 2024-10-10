# Dylan Makombe
# 10/10/2024
# P2LAB2
# Using Dictionaries

# Create a dictionary
cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

# Variable that hold only the keys from dictionary
keys = cars.keys()

# Show all the keys to the user
print(keys)
print()

# Get a car (key) from the user
selected_car = input("Enter a vehicle to see it's mpg: ")
print()

# Display the selected car and it's mpg
print(f"The {selected_car} gets {cars[selected_car]} mpg.")
print()

# Get the numbers of miles to drive the car
miles_planned = float(input(f"How many miles will you drive the {selected_car}? "))
print()

# Calculate gallons of gas needed
gas_needed = miles_planned / cars[selected_car]

# Display gallons needed to user
print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {selected_car} {miles_planned} miles.")
