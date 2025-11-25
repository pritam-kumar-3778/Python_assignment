# Given a tuple of integers, create
# - A tuple of all even numbers
# - A tuple of odd even numbers

nums = (2,4,5,6,7,8,9)

for el in nums:
    if(el % 2 == 0):
        print("Even :",el)
    else:
        print("Odd : ",el)