print("Welcome to the Rollercoaster Ride")
height = int(input("Please input your height in cm: "))
age = int(input("Please input your age: "))

if height > 120:
    print("Yes you can ride")
    ticket = 0
    if age >= 18:
        ticket += 12
        print("Adult tickets cost $12")
    elif age >= 12 and age <= 18:
        ticket += 7
        print("Youth tickets cost $7")
    else:
        ticket += 5
        print("children tickets cost $5")
    photo = input("Do you want photos?, Please input yes or no: ").lower()
    if photo == "yes":
        ticket += 3
        print("photos ticket cost $3")
        print(f"Your total bill is {ticket}$")
    else:
        print(f"Your total bill is {ticket}$")




else:
    print("No sorry you can't ride")









