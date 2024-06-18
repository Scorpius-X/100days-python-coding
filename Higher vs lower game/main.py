#Create the higher / lower game , you made yesterday.
#import the needed modules
import sys

sys.path.append("C:\\Users\\HP\\Documents\\GitHub\\100days-python-coding")

from Clears_vscode_terminal.clear_terminal import clear_terminal
import random
from art import logo, vs
from game_data import data
#create a function to fetch details
def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_description} from {account_country}'

def check_answers(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
#make the whole program repeatable after a win

#display logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
#generate information
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    #generate comparables
    print(f"Compare A: {format_data(account_a)}")
    #display vs
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    #ask the user to guess the answer
    guess = input("Which of these have the highest followers? Type 'A' or 'B': ")
    #check comparables through the follwers count
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    #create a function that checks which has the highest followers
    is_correct = check_answers(guess, a_followers, b_followers)
    clear_terminal()
    print(logo)

    if is_correct:
        score += 1
        print(f"You got it right!, your score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry you got it wrong, your final score is {score}")

