
print(round(8/3, 2))
# the f string stays outside the quotation marks but the parameters stays inside the string.

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
age = input("what is your age ? ")
given_age = int(age)
remaining_age = 90 - given_age
days = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age * 12
result = f"You have a total of {days} days, {weeks} weeks and {months} months left."
print(result)
