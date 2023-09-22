# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# import re
# my_string = "Mary had a little lamb"
# len(re.findall("a", my_string))

print("Welcome to the love calculator!")
name1 = input("Please input the first name? ")
name2 = input("Please input the second name? ")
love_calc = (name1 + name2)
true_love = love_calc.lower()

t = true_love.count("t")
r = true_love.count("r")
u = true_love.count("u")
e = true_love.count("e")
true = t + r + u + e

l = true_love.count("l")
o = true_love.count("o")
v = true_love.count("v")
e = true_love.count("e")
love = l + o + v + e
love_score = int(f"{true}{love}")
if love_score < 10 or love_score > 90 :
    print(f"Your score is {love_score}, you go together like coke and mentos.")
# you can also try something like 40 < love_score < 50
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")