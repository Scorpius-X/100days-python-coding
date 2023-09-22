# Rollercoaster ride calculator!

height = int(input("Please input your height?\n"))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("please input your age?\n"))
    bill = 0
    if age < 12:
        bill += 7
        print("you have to pay $7")
    elif age <= 18:
        bill += 10
        print("you have to pay $10")
    elif age > 18:
        bill += 12
        print("you have to pay $12")
    elif age >= 45 and age <= 50:
        bill += 0
        print("you are riding for free")
    want_photos = (input("Do you want photos yes or no? Y/N "))
    if want_photos == "Y":
        bill += 3

else:
    print("Sorry you can not ride the rollercoaster")

total_bill = f"The total bill is ${bill}."
print(total_bill)