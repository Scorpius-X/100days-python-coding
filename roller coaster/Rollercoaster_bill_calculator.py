print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120 :
    print("you can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age > 18:
        print("you have to pay $12")
    elif age <= 18:
        print("you have to pay $7")
    elif age < 12:
        print("you have to pay $5")
else:
    print("Sorry you can not ride this rollercoaster.")