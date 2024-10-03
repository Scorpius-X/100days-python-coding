import random

def draw_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def display_cards():
    print(f"Your cards: {user_card}, current score: {sum_of_user_draw}")
    print(f"Computers first card: {computer_card[0]}")

def hit_card():
    draw_cards()

blackjack = 21

user_card = []
sum_of_user_draw = 0

computer_card = []
sum_of_computer_draw = 0

for i in range(2):
    user_card.append(draw_cards())
    sum_of_user_draw += user_card[-1]
    computer_card.append(draw_cards())
    sum_of_computer_draw += computer_card[-1]

display_cards()

def check_blackjack():
    if sum_of_user_draw and sum_of_computer_draw == blackjack:
        print("It's a Tie!")
    elif sum_of_user_draw == blackjack:
        print("Congratulations! you win! Blackjack")
    elif sum_of_computer_draw == blackjack:
        print("You lose!, computer wins Blackjack")

def compare_cards():
    if sum_of_user_draw < blackjack and sum_of_computer_draw > blackjack:
        print("Congratulations!, you win!")
    elif sum_of_user_draw < blackjack and sum_of_computer_draw < blackjack:
        print("Congratulations!, you win!")
    else:
        print("You lose!, Computer wins!")






