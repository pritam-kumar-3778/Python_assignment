# Write a function to return the count the number of digits in a number, n

def count_digits(n):
    return len(str(abs(n)))

# Example usage
print(count_digits(-34567))    # Output: 5


# The abs() use for nevigate - value
# Ivf we don't use abs() here then it show the out put 6.