import sys

sys.path.append("C:\\Users\\HP\\Documents\\GitHub\\100days-python-coding")

from Clears_vscode_terminal.clear_terminal import clear_terminal
from art import logo



# lets define the function name to determine the highest bidder and bid


def find_highest_bid(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid

bids = {}
should_continue = True
print(logo)
print("Welcome to the Secret Auction Program!")
while should_continue:
    name = input("What is your name?: ")
    price = float(input("How much are you bidding?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n") == "yes"
    if not should_continue:
        winner, highest_bid = find_highest_bid(bids)
        print(f"The winner is {winner}, with a bid of ${highest_bid:.2f}")
    else:
        clear_terminal()




