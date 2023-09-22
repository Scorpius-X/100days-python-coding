# Creating a tip calculator
# asks for the total bill
# asks for the percentage of payment
# asks for how the bill is going to be split
# gives a result of the bills each person should pay

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
totalus = float(total_bill)

percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentus = float(percentage_tip) / 100

bill_split = input("How many people to split the bill? ")
billy = int(bill_split)

initial_bill = totalus * percentus
final_bill = (initial_bill + totalus)/billy
result = round(final_bill)
print(f"Each person should pay a total of ${result}")