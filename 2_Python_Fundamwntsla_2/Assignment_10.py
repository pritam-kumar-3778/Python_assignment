# Letʼs create a “Number guessing game”.
# Given a secret number(already decided by you),
# write a program that asks the user t oguess it and prints
# "Too high" If the guesses is above the number.
# "Too low" If the guesses is below
# "Correct!" If the guess is match

number = int(input("Guess a number : "))

decide_num = 120

if (number > decide_num):
    print("Too high")
if (number < decide_num):
    print("Too low")
if (number == decide_num):
    print("Correct!")