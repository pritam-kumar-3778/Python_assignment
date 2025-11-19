# Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit"

while True:
    num = int(input("Enter a number : "))
    if(num > 0):
        print("Posetive Number")
    elif(num < 0):
        print("Negetive Number")
    else:
        print("You put Zero")