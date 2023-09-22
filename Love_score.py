import random

random_float = random.random() * 5
print("{:.1f}".format(random_float))
print(int(random_float))

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")