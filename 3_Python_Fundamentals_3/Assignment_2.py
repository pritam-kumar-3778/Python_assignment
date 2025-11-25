# Given a list of integers compute the average of all numbers in the list

numbers = [1,4,5,5]

sum = 0
count = len(numbers)

for el in numbers:
    sum += el

print(f"Average of numbers = {sum / count}")