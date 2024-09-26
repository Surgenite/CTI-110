# Dylan Makombe
# 9/26/2024
# P1LAB1
# Get integer input from user and perform math calculations

# Display output to user
print("-----Calculating Exponents-----")
print()
print()

# Get info from user
base_value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print()
print()

# Calculate the value of the exponent math
final_value = base_value ** exponent

# Display result of the exponent 
print(base_value, "raised to the power of", exponent, "is", final_value, "!!")
print()
print()

print("-----Addition and Subtraction-----")
print()
print()

# Get more info from user
start_int = int(input("Enter a starting integer: "))
add_int = int(input("Enter an integer to add: "))
sub_int = int(input("Enter an integer to subtract: "))
print()
print()

# Calculate the math
result = start_int + add_int - sub_int

# Display the results
print(start_int, "+", add_int, "-", sub_int, "is equal to", result)
