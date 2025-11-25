# Ask the user for a string and print
# 1 : All unique characters
# 2 : The count of unique characters

user = input("Enter a word : ") # madam
print(f"Your entered word is {user}")

# All unique characters

seen = set()
unique = set()
for val in user:
    if val in unique:
        seen.add(val)
    else:
        unique.add(val)

print("Unique elements:", unique)
# The count of unique characters
print("length of unique characters : ", len(unique))

# or using set

# user = input("Enter a string : ")
# unique_chars = set(user)
# print("Unique characters:", unique_chars)
# print("Count:", len(unique_chars))