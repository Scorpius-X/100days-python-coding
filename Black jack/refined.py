import random

def draw_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def display_status(sub_cards, sum_of_choice, comp_cards, sum_of_comp_choice, reveal_comp=False):
    print(f"Your cards: {sub_cards}, current score: {sum_of_choice}")
    if reveal_comp:
        print(f"Computer's cards: {comp_cards}, Computer's score: {sum_of_comp_choice}")
    else:
        print(f"Computer's first card: {comp_cards[0]}")

def hit_card(sub_cards, sum_of_choice, comp_cards, sum_of_comp_choice):
    should_continue = True
    while should_continue:
        hit = input("Do you want to add more cards? Type 'yes' or 'no'.\n").lower()
        if hit == "yes":
            random_card = draw_cards()
            sub_cards.append(random_card)
            sum_of_choice += random_card
            if sum_of_choice > 21 and 11 in sub_cards:
                sub_cards.remove(11)
                sub_cards.append(1)
                sum_of_choice -= 10  # Adjust the sum after converting 11 to 1
            display_status(sub_cards, sum_of_choice, comp_cards, sum_of_comp_choice)
            if sum_of_choice > 21:
                should_continue = False
                print("You went over 21. You lose.")
        else:
            should_continue = False
            display_status(sub_cards, sum_of_choice, comp_cards, sum_of_comp_choice, reveal_comp=True)
            print("Final hand.")
    return sum_of_choice

def start_game():
    play_again = True
    while play_again:
        if input("Type 'yes' to start game or 'no' to quit: ").lower() != 'yes':
            play_again = False
            print("Thanks for playing!")
            break

        print("Welcome to BlackJack")

        sub_cards = []
        sum_of_choice = 0
        comp_cards = []
        sum_of_comp_choice = 0

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
        display_status(sub_cards, sum_of_choice, comp_cards, sum_of_comp_choice)

        # Check for initial blackjack
        if sum_of_choice == 21 and sum_of_comp_choice == 21:
            print("It's a tie! Both you and the computer have Blackjack.")
        elif sum_of_choice == 21:
            print("Congratulations! You have a Blackjack and win!")
        elif sum_of_comp_choice == 21:
            print("Computer has a Blackjack. You lose.")
        else:
            # Continue game
            sum_of_choice = hit_card(sub_cards, sum_of_choice, comp_cards, sum_of_comp_choice)

            # After the player finishes, it's the computer's turn
            while sum_of_comp_choice <= 16:
                comp_draw = draw_cards()
                comp_cards.append(comp_draw)
                sum_of_comp_choice += comp_draw
                if sum_of_comp_choice > 21 and 11 in comp_cards:
                    comp_cards.remove(11)
                    comp_cards.append(1)
                    sum_of_comp_choice -= 10  # Adjust the sum after converting 11 to 1

            # Display final status
            display_status(sub_cards, sum_of_choice, comp_cards, sum_of_comp_choice, reveal_comp=True)

            # Determine winner after hitting cards
            if sum_of_choice <= 21:
                if sum_of_choice > sum_of_comp_choice or sum_of_comp_choice > 21:
                    print("You win!")
                elif sum_of_choice == sum_of_comp_choice:
                    print("It's a tie!")
                else:
                    print("You lose. Computer wins.")
            else:
                print("You went over 21. You lose.")

start_game()
