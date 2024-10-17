'''
# In-class examples using lists

# Create an empty list
myfam = []

# Add values to the list
myfam.append("Dylan")
myfam.append("Denzel")
myfam.append("Donovan")
myfam.append("Mom")
myfam.append("Dad")
myfam.append("Grandma")

# Display List
print(myfam)

# Print item at index 3
print(myfam[3])

# Print items from index 1 to 3 (must give 4)
print(myfam[1:4])

# Remove item from list by its value
myfam.remove("Denzel")

print(myfam)

# Remove item from list by its index
myfam.pop(4)

print("Remove Grandma...")
print(myfam)
'''

num1 = int(input("gimme a number: "))
num2 = int(input("gimme a number: "))
num3 = int(input("gimme a number: "))
num4 = int(input("gimme a number: "))

# Create the list with the values in it
numbers = [num1, num2, num3, num4]

print(numbers)

# Functions that use lists

# Gives back  the number of items in the list
print(f"There are {len(numbers)} items in the list.")

# Get the highest value in the list
print(f"The highes value in the list is {max(numbers)}")

# Get the lowest value in the list
print(f"The lowest value in the list is {min(numbers)}")

# Get the sun of all values in the list
print(f"The sum of values in the list is {sum(numbers)}")

# Get average
average = sum(numbers)/len(numbers)

# Display average
# Get the sun of all values in the list
print(f"The average of values in the list is {average}")






















