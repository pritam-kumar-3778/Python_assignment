# Take two numbers as input from the user and print their sum,difference,product,and quotien

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    quotient = num1 / num2  

    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The difference when {num2} is subtracted from {num1} is: {difference}")
    print(f"The product of {num1} and {num2} is: {product}")
    print(f"The quotient when {num1} is divided by {num2} is: {quotient}")