# Given a list,
# print all elements that appear more than once in the list

lst = [1, 2, 3, 4, 2, 5, 1, 6, 3]
seen = set()
duplicates = set()
for val in lst:
    if val in seen:
        duplicates.add(val)
    else:
        seen.add(val)
print("Duplicate elements:", duplicates)