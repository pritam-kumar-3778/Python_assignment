# Given a list of words : 
# words =["apple","banana","kiwi","cherry","mango"]
# Create a dictionary that maps each word to its length.
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

words =["apple","banana","kiwi","cherry","mango"]
dict = {}

for el in words:
    dict[el] = len(el)

print(dict)

