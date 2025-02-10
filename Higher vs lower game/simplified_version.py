import random
from game_data import data
from art import logo, vs


celeb_a = random.choice(data)
celeb_b = random.choice(data)

"""Ensures that b != a"""
while celeb_b == celeb_a:
    celeb_b = random.choice(data)

should_continue = True
player_score = 0
print(logo)
while should_continue:
    print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']} from {celeb_a['country']}")
    print(vs)
    print(f"against B: {celeb_b['name']}, a {celeb_b['description']} from {celeb_b['country']}")
    guess = input("Who has the highest amount of followers?, Type 'A' or 'B' : ")

    if celeb_a['follower_count'] > celeb_b['follower_count']:
        answer = "a"
    else:
        answer = "b"

    if guess == answer:
        player_score += 1
        print("\n" * 20)
        print(logo)
        print(f"You got it right! your current score is : {player_score}")

        if answer == "a":
            celeb_b = random.choice(data)
        else:
            celeb_a = celeb_b
            celeb_b = random.choice(data)
        
        while celeb_b == celeb_a:
            celeb_b = random.choice(data)
    else:
        should_continue = False
        print(f"Sorry you got it wrong, your final score is : {player_score}")



