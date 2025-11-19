# Write a function to return the sum of digits of a number, n

def sum_of_digits(n):
    # Convert n to absolute value to handle negative numbers
    n = abs(n)
    # Convert to string to iterate over each digit
    return sum(int(digit) for digit in str(n))

result = sum_of_digits(12345)
print(result)  # Output: 15
