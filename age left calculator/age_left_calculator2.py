#calculate ones age remaining from 90 yrs, using a year, a month, a week and days left.
#year = 365 days, week = 52 weeks, month = 12 months.

age = int(input("Please input your age :"))
remaining_age = 90 - age
days = 365 * remaining_age
weeks = 52 * remaining_age
months = 12 * remaining_age

result = f"You have {days} days, {weeks} weeks and {months} months left"
print(result)