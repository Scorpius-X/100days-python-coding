import random
from art import logo

def draw_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to display the current status
def display_status():
    print(f"Your cards: {sub_cards}, current score: {sum_of_choice}")
    print(f"Computer's deck : {comp_cards}, Computer's first card: {comp_cards[0]}, Computer's current score is {sum_of_comp_choice}")

sub_cards = []
sum_of_choice = 0
comp_cards = []
sum_of_comp_choice = 0
blackjack = 21

def hit_card():
    global sum_of_choice
    global sub_cards
    should_continue = True
    while should_continue:
        hit = input("Do you want to add more cards? Type 'yes' or 'no'.\n")
        if hit.lower() == "yes":
            random_card = draw_cards()
            sub_cards.append(random_card)
            sum_of_choice += random_card
            display_status()
            if sum_of_choice > blackjack:
                if 11 in sub_cards:
                    sub_cards.remove(11)
                    sub_cards.append(1)
                    sum_of_choice -= 10  # Adjust the sum after converting 11 to 1
                    display_status()
        else:
            should_continue = False
            display_status()
            print("Final hand.")

# Start the game
def start_game():
    global sum_of_choice
    global sub_cards
    global sum_of_comp_choice
    global comp_cards
    start_game = input("Type 'yes' to start game: ").lower() == 'yes'
    if start_game:
        print(logo)
        print("Welcome to BlackJack")

        # Draw initial cards for the player
        for _ in range(2):
            card = draw_cards()
            sub_cards.append(card)
            sum_of_choice += card

        # Draw initial cards for the computer
        for _ in range(2):
            card = draw_cards()
            comp_cards.append(card)
            sum_of_comp_choice += card

        # Display initial status
        display_status()

        # Check for initial blackjack
        if sum_of_choice == blackjack and sum_of_comp_choice == blackjack:
            print("It's a tie! Both you and the computer have Blackjack.")
        elif sum_of_choice == blackjack:
            print("Congratulations! You have a Blackjack and win!")
        elif sum_of_comp_choice == blackjack:
            print("Computer has a Blackjack. You lose.")
        else:
            # Continue game
            hit_card()

            # After the player finishes, it's the computer's turn
            while sum_of_comp_choice <= 16:
                comp_draw = draw_cards()
                comp_cards.append(comp_draw)
                sum_of_comp_choice += comp_draw
                if sum_of_comp_choice > blackjack and 11 in comp_cards:
                    comp_cards.remove(11)
                    comp_cards.append(1)
                    sum_of_comp_choice -= 10  # Adjust the sum after converting 11 to 1

            # Display final status
            display_status()

            # Determine winner after hitting cards
            if sum_of_choice <= blackjack:
                if sum_of_choice > sum_of_comp_choice or sum_of_comp_choice > blackjack:
                    print("You win!")
                elif sum_of_choice == sum_of_comp_choice:
                    print("It's a tie!")
                else:
                    print("You lose. Computer wins.")
            else:
                print("You went over 21. You lose.")
start_game()