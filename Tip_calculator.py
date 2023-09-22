print("welcome to the tip calculator!")
bill = float(input("what was the total bill? "))
tip = int(input("what percentage tip whould you like to give? 10, 12, or 15? "))
people =int(input("how many people to split the bill? "))
total_bill = (tip / 100) * bill + bill
tip_per_person = total_bill/ people
final_bill = "{:.2f}".format(tip_per_person)
print(f"Each person is to pay a sum of ${final_bill}")