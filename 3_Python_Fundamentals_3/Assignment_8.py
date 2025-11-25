# Write a program to check whether two lists share no common elements.

def check_no_common_elemnets():

    list_1 = {1,2,3,4}
    list_2 = {5,6,7,4}

    set_1 = set(list_1)
    set_2 = set(list_2)
    return not (set_1.intersection(set_2))

print(check_no_common_elemnets())


# An empty set is False in boolean context
# A non-empty set is True in boolean context
# not reverses this, so not empty_set returns True



