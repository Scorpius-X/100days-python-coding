# Write a program that works out whether if a given number is an odd or even number.

number_check = int(input("Which number do you wanna check? "))
if number_check % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")