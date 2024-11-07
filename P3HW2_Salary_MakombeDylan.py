# Dylan Makombe
# 10/29/2024
# P2HW2
# Program calculates paycheck based on OT or no OT

'''
Input: Get employee name from the user- String (name)
Input: Get hours worked from the user - int (hours)
Input: Get pay rate from user - float (pay_rate)

Output: print dotted line and employee name

If hours is greater than 40 (employee has OT)
    total hours worked is the variable hours (optional)
    (don't have to create pay rate, it already exists)
    create a variable (OT) that holds only the OT hours (hours - 40)
    create a variable for OT_pay_rate(pay_rate * 1.5)
    calculate pay for OT hours (OT * OT_pay_rate)
    calculate regular pay (pay_rate * 40)
    Calculate gross pay (pay for OT + regular pay)
else (No OT - hours has to be 40 or less)
    create a variable (OT) that holds only the OT hours which is zero
    Calculate pay for OT hours which is Zero
    calculate regular pay (pay_rate * hours)
    Calculate gross pay (same as regular pay)

Display the line of strings with width specifiers
print(f"{'Hours Worked' :<20} {'Pay Rate':<20}")
print(f"

'''
# Create variables asking the employee to enter details
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("-" * 40)
print(f"Employee name: {name}")

# Create an if-else statement to show the employee's gross pay with or without overtime
if hours > 40:
    OT = hours - 40
    OT_pay_rate = pay_rate * 1.5
    OT_pay = OT * OT_pay_rate
    regular_pay = pay_rate * 40
    gross_pay = OT_pay + regular_pay
else:
    OT = 0
    OT_pay = 0
    regular_pay = pay_rate * hours
    gross_pay = regular_pay

# Display the line of strings with width specifiers
print(f"{'Hours Worked':<20} {'Pay Rate':<20} {'OverTime':<20} {'OverTime Pay':<20} {'RegHour Pay':<20} {'Gross Pay'}")
print("-" * 125)
print(f"{hours:<20} {pay_rate:<20} {OT:<20} {OT_pay:<20} ${regular_pay:<20.2f} ${gross_pay:<20.2f}")


    
