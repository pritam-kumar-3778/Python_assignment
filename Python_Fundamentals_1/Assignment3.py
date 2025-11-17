# Ask the user to enter two integers and one float.Convert them all to floats and print their average.

int1 = int(input("Enter the first number: "))
int2 = int(input("Enter the second number: "))
float1 = float(input("Enter a float number: "))

int_to_float1 = float(int1)
int_to_float2 = float(int2)

average = (int_to_float1 + int_to_float2 + float1) / 3
print(average)