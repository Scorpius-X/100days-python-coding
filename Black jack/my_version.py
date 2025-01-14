import random
from art import logo

def draw_cards():
    """Returns a random card from a deck of cards"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the total score of the cards and returns the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return  sum(cards)

def compare_cards(u_score, comp_score):
    """Compares the user and computer score in order to determine the winner"""
    if u_score == comp_score:
        return "It's a Tie!"
    if u_score == 0:
        return "You win with a blackjack!"
    if comp_score == 0:
        return "You lose!, computer wins!"
    if u_score > 21:
        return "You went over, you lose!"
    if comp_score > 21:
        return "You win!, Computer went over"
    if u_score > comp_score:
        return "You win!"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_card = []
    computer_card = []

    computer_score = -1
    user_score = -1

    is_game_over = False

    for i in range(2):
        user_card.append(draw_cards())
        computer_card.append(draw_cards())

    """User setup"""
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards are {user_card} and your score is {user_score}")
        print(f"Computer's first card is: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            user_should_deal = input("Please input Y to deal or N to pass: ").lower()
            if user_should_deal == "y":
                user_card.append(draw_cards())
            else:
                is_game_over = True

    """Computer setup( ensures that the computer keeps drawing only if no bj has been hit )"""
    if computer_score != 0:
        while computer_score < 17:
            computer_card.append(draw_cards())
            computer_score = calculate_score(computer_card)

    # Final results
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare_cards(user_score, computer_score))

while input("Do you want to play a game of blackjack? type 'y' to start or 'n' to end : ").lower() == "y":
    print("\n" * 20)
    play_game()
