# Dylan Makombe
# 10/24/2024
# P3HW1
# Enter and store grades in a list

# Create variables and ask user to enter grades
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
print()

# Create the list with the values in it
modules = [module1, module2, module3, module4, module5, module6]

# Create get average variable
average = sum(modules)/len(modules)

# Display Result
print("--------------------Result--------------------")
print(f"{'Lowest Grade:':<20}{min(modules)}")
print(f"{'Highest Grade:':<20}{max(modules)}")
print(f"{'Sum of Grades:':<20}{sum(modules)}")
print(f"{'Average:':<20}{average:.2f}")
print("-" * 60)


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
print(f"Your grade is: {letter_grade}")








