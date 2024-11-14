# Dylan Makombe
# 11/12/2024
# P4HW1
# The program is to display a letter grade for the calculated average

# Get number of items to purchase
numModules = int(input("How many scores do you want to enter? "))

# Create the list with the values in it
module = []

# Loop to get the items
for score in range(numModules):
    grade = float(input(f"Enter score #{score + 1}: "))
    # Loop to ensure grade
    while grade < 0 or grade > 100:
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")
        grade = int(input(f"Enter score #{score + 1} again: "))
    module.append(grade)


# Display Result
print("----------------Result----------------")
print(f"Lowest Grade: {min(module)}")
module.remove(min(module))
print(f"Modified: {module}")
average = sum(module)/len(module)
print(f"Scores Average:{average:.2f}")


# Determine letter grade based on average
if average >= 90:
    letter_grade = "A"

elif average >= 80:
    letter_grade = "B"

elif average >= 70:
    letter_grade = "C"

elif average >= 60:
    letter_grade = "D"

elif average <= 59:
    letter_grade = "F"

# Display the grade and average
print(f"Grade: {letter_grade}")
print("-" * 40)

