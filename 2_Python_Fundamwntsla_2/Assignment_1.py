# Write a program that takes as input.
# Using conditional statements,calculate the final tax rate based on these rules
# If salary < 30, → 5%
# If salary is 30,000 – 70,→ 15%
# If salary > 70, → 25%

salary = int(input("Enter yor salary : "))

if (salary <= 30000):
    tax1 = (5/100) * salary
    print("Your tax deduction amount as 5 percentage is :", tax1)
elif (salary > 30000 and salary <= 70000):
    tax2 = (15/100) * salary
    print("Your tax deduction amount as 15 percentage is :", tax2)
else:
    tax3 = (25/100) * salary
    print("Your tax deduction amount as 25 percentage is :", tax3)

