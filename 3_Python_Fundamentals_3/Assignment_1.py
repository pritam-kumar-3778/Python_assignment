# Ask the user for a string and check whether it is a palindrome or not.
# Eg- “madam”, “racecar” etc

user = input("Enter a word for check whether it is a palindrome or not : ")

change_userType = list(user)
copy_user = change_userType.copy()
copy_user.reverse()

if(change_userType == copy_user):
    print(f"{user} is a palindrome")
else:
    print(f"Opps {user} is not a Palindrome")