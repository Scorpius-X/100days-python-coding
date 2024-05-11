"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
"""
print("Goodday!!, welcome to our pizza delivery service, what would you like to order?")
pizza_size = (input("Please input 'S' or 'M' or 'L' to determine your pizza size: ")).lower()
bill = 0
if pizza_size == "s":
    bill += 15
    print("You have selected a Small sized pizza and it costs $15")
elif pizza_size == "m":
    bill += 20
    print("You have selected a Medium sized pizza and it costs $20")
else:
    bill += 25
    print("You have selected a Large sized pizza and it costs $25")

print("Would you like to add pepperoni sauce?")
sauce = input("Please input yes or no: ").lower()

if sauce == "yes":
    if pizza_size == "s":
        bill += 2
        print("that would cost $2")
    else:
        bill += 3
        print("that would cost $3")
else:
    print("No problem")

print("Would you like to add extra cheese?")
extra_cheese = input("Please input yes or no: ").lower()
if extra_cheese == "yes":
    bill += 1
    print("That would be extra $1")
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your Total Bill is ${bill}")
else:
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your Total Bill is ${bill}")
