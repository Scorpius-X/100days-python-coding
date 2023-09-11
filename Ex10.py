# Build a pizza order machine.

pizza_size = (input("What size of pizza do you want? Small, medium or large?\nplease input S, M or L "))
add_pepperoni = (input("Do you want pepperoni sauce, yes or no? Y/N "))
extra_cheese = (input("Do you want extra cheese? Y/N "))

bill = 0
if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill for your pizza order is : ${bill}.")