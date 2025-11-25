# Input two lists of integers from the user.
# Merge them into one list and sort the result

user_1 = list(input("Enter a list of integer : "))
user_2 = list(input("Enter a list of integer : "))

print(type(user_2))

combine = user_1+user_2
print(combine)

combine.sort()
print(combine)


