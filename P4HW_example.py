# Example similiar to P4HW1

# List of available items (this is not needed in your homework)
availableItems = ["litter", "cat food", "feather", "collar", "litter box", "flea meds", "treat"]

# Get number of items to purchase
numItems = int(input("How many items will you purchase? "))

# Empty list to holf valid responses
cart = []

# Loop to get the items
for item in range(numItems):
    thisItem = input(f"Enter item #{item + 1}: ")
    # Loop to ensure thisItem is in availableItems
    while thisItem not in availableItems:
        print(f"{thisItem} is not in stock!")
        thisItem = input(f"Enter item #{item + 1} again: ")
    # Add the valid item to the cart
    cart.append(thisItem)

# Loop to print each item in the cart
print("Items we purchased are: ")
for product in cart:
    print(product)