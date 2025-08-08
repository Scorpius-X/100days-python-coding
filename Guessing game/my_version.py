import random
from art import logo

answer = random.randint(1,100)


def game_level():
    should_guess = False

    if difficulty == "hard":
        attempts = 5
    else:
        attempts = 10

    while not should_guess:

        print(f"You have {attempts} attempts to make a guess")
        user_guess = int(input("Make a guess: "))

        if attempts == 1:
            should_guess = True
            print("You have exhausted you number of attempts, you lose!")
        elif user_guess == answer:
            should_guess = True
            print(f"You guessed right, the number is in fact {answer}")
        elif user_guess > answer:
            print("The number you guessed is too high!, try again")
        elif user_guess < answer:
            print("The number you guessed is too low!, try again")
        attempts -= 1



print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
# print(f"The number i'm guessing is {answer}")
difficulty = input("choose your difficulty, type in 'easy' or 'hard' to start: ").lower()
game_level()






