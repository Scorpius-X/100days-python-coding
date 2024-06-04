import random
from art import logo

HARD_GUESS = 5
EASY_GUESS = 10

def check_guess(random_guess, answer):
    if random_guess > answer:
        print("Too high")
        print("Guess again.")
        return False
    elif random_guess < answer:
        print("Too Low")
        print("Guess again.")
        return False
    elif random_guess == answer:
        print(f"You got it! The answer is {answer}")
        return True

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'. \n").lower()
    if level == "hard":
        return HARD_GUESS
    else:
        return EASY_GUESS

print(logo)
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100")
answer = random.randint(1, 100)
print(f"Pssst the answer is {answer}")
turns = set_difficulty()
keep_guessing = True
while keep_guessing and turns > 0:
    print(f"You have {turns} attempts remaining to guess.")
    random_guess = int(input("Make a guess: "))
    keep_guessing = not check_guess(random_guess, answer)
    turns -= 1
    if turns == 0 and keep_guessing:
        print("You've run out of guesses, you lose!")