# Take a decimal number as input (55.6) and output its
# integer part : 55
# factorial part : .6

number = float(input("Enter a floating value : "))

integer_part = int(number)
fractional_part = number - integer_part

print("Integer part is :", integer_part)
print("Fractional part is :", fractional_part)