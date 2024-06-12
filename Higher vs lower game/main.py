import random
import sys

sys.path.append("C:\\Users\\HP\\Documents\\GitHub\\100days-python-coding")

from Clears_vscode_terminal.clears_terminal import clear_terminal

from art import logo
from game_data import data
from art import vs

#create a format function
def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description} from {account_country}"
#create a function to check answers
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

#display logo
print(logo)

score = 0

game_should_continue = True
account_b = random.choice(data)
#generate data information
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)


    #display comparables
    print(f"Compare A: {format_data(account_a)}")
    #display vs
    print(vs)

    print(f"Against B: {format_data(account_b)}")

    #generate guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #generate followers count
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    clear_terminal()
    #display logo
    print(logo)


    is_correct = check_answer(guess, a_followers, b_followers)
    if is_correct:
        score += 1
        print(f"You got it right!, your score is {score}.")
    else:
        game_should_continue = False
        print(f"Sorry you got it wrong, your final score is {score}.")
