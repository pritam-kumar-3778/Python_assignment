# Letʼs create a Simple calculator.That performs arithmetic operations.
# Createa function calculator(a,b,operation) that performs addition,subtraction,multiplication, or division based on the Operation parameter.

# Operation parameter can have values '+', '-', '*', '/'

def calculator(a,b, operation):
    if (operation == '+'):
        return a + b
    elif(operation == '-'):
        return a - b
    elif(operation == '*'):
        return a * b
    elif(operation == '/'):
        return a / b
    else:
        print("Invalid input")

print(calculator(2,5,'*'))
