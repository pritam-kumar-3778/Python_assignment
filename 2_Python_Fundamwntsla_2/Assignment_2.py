# Write a function that takes two integers a and b and prints all even numbers between them(inclusive)

def even_calculate(a,b):
    # Ensure a is the smaller number
    start = min(a,b)
    end = max(a,b)

    for i in range(start, end+1):
        if(i % 2 == 0):
            print(i)

even_calculate(2,10)


# min(a, b) returns the smaller of the two numbers
# max(a, b) returns the larger of the two numbers
