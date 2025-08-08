import random

names_string = input("Give me everybodys names, seperated by a coma. ")
names = names_string.split(", ")
roulette = random.randint(0, len(names))
print(f"{names[roulette]} is going to buy the meal today!")
