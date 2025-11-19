# Write a function that prints the digit of anumber, n
# Eg :- if n = 345, It prints 3, 4 and 5

# function definition

def split_num(n):
    num_str = str(n)  #bcz String can iterate one by one
    for i in num_str:
        print(i)

split_num(345)