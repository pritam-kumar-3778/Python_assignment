# Write a function is_prime(n), that returns True 
# if n is a prime number and false other wise, using a loop.

def is_prime(n):
    # Handle special cases
    if n <= 1:
        return False
    # Check for factors from 2 to n-1
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


print(is_prime(7))   # Output: True
print(is_prime(10))  # Output: False
