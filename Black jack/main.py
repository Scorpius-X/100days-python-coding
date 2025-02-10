#creating a game of blackjack

import random
from art import logo

blackjack = 21

def draw_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def display_status(user_cards, sum_of_user_choice, comp_cards=None, sum_of_comp_choice=0, reveal_comp=False):
    print(f"Your cards: {user_cards}, Your score: {sum_of_user_choice}.")
    if comp_cards is not None:
        if reveal_comp:
            print(f"Computer's cards: {comp_cards}, Computer's score: {sum_of_comp_choice}")
        else:
            print(f"Computer's first card: {comp_cards[0]}")
    else:
        print("Computer's cards are hidden.")

def check_blackjack(sum_of_user_choice, sum_of_comp_choice):
    if sum_of_user_choice == blackjack and sum_of_comp_choice == blackjack:
        print("It's a tie with Blackjack!")
        return True
    elif sum_of_user_choice == blackjack:
        print("You win with a Blackjack!")
        return True
    elif sum_of_comp_choice == blackjack:
        print("You lose, computer wins with a Blackjack!")
        return True
    return False

def compare_cards(sum_of_user_choice, sum_of_comp_choice):
    if sum_of_user_choice > 21:
        print("You bust! You lose!")
    elif sum_of_comp_choice > 21:
        print("Computer busts! You win!")
    elif sum_of_user_choice > sum_of_comp_choice:
        print("You win!")
    elif sum_of_user_choice < sum_of_comp_choice:
        print("You lose!")
    else:
        print("It's a tie!")

def adjust_for_aces(cards, current_sum):
    while current_sum > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        current_sum -= 10
        print("Swaps Ace with 1")
    return current_sum

def hit_card(user_cards, sum_of_user_choice):
    while True:
        if input("Do you want to add more cards? Type 'yes' or 'no'.\n").lower() == "yes":
            random_card = draw_cards()
            user_cards.append(random_card)
            sum_of_user_choice += random_card
            sum_of_user_choice = adjust_for_aces(user_cards, sum_of_user_choice)
            display_status(user_cards, sum_of_user_choice)
            if sum_of_user_choice > blackjack:
                print("Bust")
                print("You lose")
                break
        else:
            break
    return sum_of_user_choice

def computer_turn(comp_cards, sum_of_comp_choice):
    while sum_of_comp_choice <= 16:
        random_card = draw_cards()
        comp_cards.append(random_card)
        sum_of_comp_choice += random_card
        sum_of_comp_choice = adjust_for_aces(comp_cards, sum_of_comp_choice)
    return sum_of_comp_choice

def start_game():
    while input("Type 'Yes' to Start or 'No' to End the game: \n").lower() == 'yes':
        print(logo)
        print("Welcome to BlackJack")

        user_cards = []
        sum_of_user_choice = 0
        comp_cards = []
        sum_of_comp_choice = 0

        for _ in range(2):
            user_cards.append(draw_cards())
            sum_of_user_choice += user_cards[-1]
            comp_cards.append(draw_cards())
            sum_of_comp_choice += comp_cards[-1]

        display_status(user_cards, sum_of_user_choice, comp_cards, sum_of_comp_choice)

        if not check_blackjack(sum_of_user_choice, sum_of_comp_choice):
            sum_of_user_choice = hit_card(user_cards, sum_of_user_choice)
            if sum_of_user_choice <= 21:
                sum_of_comp_choice = computer_turn(comp_cards, sum_of_comp_choice)
            display_status(user_cards, sum_of_user_choice, comp_cards, sum_of_comp_choice, reveal_comp=True)
            compare_cards(sum_of_user_choice, sum_of_comp_choice)

    print("Thanks and Goodbye")

start_game()