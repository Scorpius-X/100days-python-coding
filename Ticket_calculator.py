height = int(input("Please input your height in cm: "))
age = int(input("Please input your age: "))

if height > 120:
    print("Yes you can ride")
else:
    print("No sorry you can't ride")

ticket = 0

if age >= 18:
    ticket += 12
elif age >= 12 and age <= 18:
    ticket += 7
else:
    ticket += 5

photo = input("Do you want photos?, Please input yes or no: ").lower()

if photo == "yes":
    ticket += 3
    print(f"Your total bill is {ticket}$")
else:
    print(f"Your total bill is {ticket}$")

