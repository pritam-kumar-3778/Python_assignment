# Ask the user for a temperature in Celsius (string input).
# Convert it to Float, then calculate and print temperature in Fahrenheit

temp_celsius = input("Enter temp. in Celsius : ")

float_conversion = float(temp_celsius)

temp_fahrenheit = (float_conversion * (9/5)) + 32

print(temp_fahrenheit)