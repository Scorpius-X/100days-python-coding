import random

def draw_card():
    """Randomly picks a card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(card):
    """Calculates the score of the cards in a deck"""
    if sum(card) == 21 and len(card) == 2:
        return 0
    elif 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare_score(play_score, comp_score):
    if play_score == 0:
        return "You win!"
    if comp_score == 0:
        return "computer wins!"
    if play_score == comp_score:
        return "It's a Tie!"
    if play_score > 21:
        return "You lose!, you went over 21"
    if comp_score > 21:
        return "You win!, Computer went over 21"
    if play_score > comp_score:
        return "You win!"
    else:
        return "You lose!"

def display_stats(play_card, comp_card, play_score, comp_score, reveal_comp = True):
    print(f"Your cards are: {play_card} and your score is: {play_score}")
    if reveal_comp:
        return f"computer cards are: {comp_card} and computer score is: {comp_score}"
    else:
        return f"Computer first card is {comp_card[0]}"


def start_game():
    player_card = []
    computer_card = []
    player_score = -1
    computer_score = -1
    should_draw = False

    for _ in range(2):
        """draws cards twice for the player and the computer"""
        player_card.append(draw_card())
        computer_card.append(draw_card())


    """user draws card"""
    while not should_draw:
        player_score = calculate_score(player_card)
        computer_score = calculate_score(computer_card)
        print(display_stats(play_card= player_card, comp_card= computer_card, play_score= player_score, comp_score= computer_score, reveal_comp= False))

        if player_score == 0 or player_score >= 21:
                should_draw = True

        else:
            if input("Do you want to draw or pass, type 'y' to draw and 'n' to pass: ").lower() == 'y':
                player_card.append(draw_card())

            else:
                should_draw = True

    """computer draws card"""
    if computer_score != 0:
        while computer_score < 17:
            computer_card.append(draw_card())
            computer_score = calculate_score(computer_card)

    print(display_stats(play_card= player_card, comp_card= computer_card, play_score= player_score, comp_score= computer_score, reveal_comp= True))
    print(compare_score(play_score= player_score, comp_score= computer_score))


while input("You want to start game?, input 'y' to start and 'n' to end: ") == 'y':
    print("\n" * 20)
    start_game()


