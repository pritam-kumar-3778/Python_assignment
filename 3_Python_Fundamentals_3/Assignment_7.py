# Write a program that takes a string from the user 
# and prints the number of spaces in the string.

user = input("Write a sentense : ")
print(f"You wrote, {user}")

calculate_space = user.count(" ")
print(f"The spaces in your sentense : {calculate_space}")