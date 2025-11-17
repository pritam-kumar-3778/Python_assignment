# The user enters a string containing a number. Eg "45"• 
# Convrt it to
# an integer 
# a float
# a string again 
# Print all three values with their types

user = input("Enter a number : ")

int_convert = int(user)
float_convert = float(user)
str_convert = str(user)

print("Value is : ", int_convert, type(int_convert))
print("Value is : ", float_convert, type(float_convert))
print("Value is : ", str_convert, type(str_convert))