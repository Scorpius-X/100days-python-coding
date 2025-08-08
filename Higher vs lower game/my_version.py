import random
from game_data import data
from art import logo, vs

def generate_comparisons(data):
    """Generate random comparisons about the celebrities"""
    global compared_choices_a, compared_choices_b, random_data_a, random_data_b
    random_data_a = random.choice(data)
    random_data_b = random.choice(data)

    """Ensures that b is not equal to a"""
    while random_data_b == random_data_a:
          random_data_b = random.choice(data)

    compared_choices_a = f"{random_data_a['name']}, a {random_data_a['description']} from {random_data_a['country']}"
    compared_choices_b = f"{random_data_b['name']}, a {random_data_b['description']} from {random_data_b['country']}"

def generate_new_b():
    """Generate a new random person for B and ensure it's different from A."""
    global random_data_b, compared_choices_b
    random_data_b = random.choice(data)
    # Make sure the new B is not the same as A
    while random_data_b == random_data_a:
        random_data_b = random.choice(data)
    compared_choices_b = f"{random_data_b['name']}, a {random_data_b['description']} from {random_data_b['country']}"

def compare_comparisons(rand_a, rand_b):
    """Determines the celebrity with the highest followers"""
    return rand_a if rand_a["follower_count"] > rand_b["follower_count"] else rand_b


def check_guess(guess):
     return random_data_a if guess == 'a' else random_data_b

should_continue = False
player_score = 0
print(logo)
generate_comparisons(data)

while not should_continue:
    print(f"Compare A: {compared_choices_a}")
    print(vs)
    print(f"Against B: {compared_choices_b}")
    guess = input("who has more followers? Type 'A' or 'B' : ").lower()
    correct_answer = compare_comparisons(random_data_a, random_data_b)
    guessed_data = check_guess(guess)
    if guessed_data == correct_answer:
        player_score += 1
        print("\n" * 20)
        print(logo)
        print(f"You're right! current score : {player_score}")

        # Make the current B the new A, since B was the correct answer
        random_data_a = random_data_b
        compared_choices_a = compared_choices_b

        # Generate a new random B for the next round
        generate_new_b()

    else:
        should_continue = True
        print(f"sorry that's wrong! final score : {player_score}")
