import sys

sys.path.append("C:\\Users\\HP\\Documents\\GitHub\\100days-python-coding")

from Clears_vscode_terminal.clears_terminal import clear_terminal
from art import logo



# def auction_board(partaker_name, bid_price):


print(logo)
print("Welcome to the secret auction program!")
should_continue = True
auction = {}
while should_continue:
    partaker_name = input("What is your name? ")
    bid_price = (input("How much are you bidding?: "))
    auction[partaker_name] = bid_price
    max_key = max(auction, key=auction.get)
    max_value = auction[max_key]
    other_bids = input("Are there any other bidder? 'yes' or 'no': ").lower()
    if other_bids == "no":
        should_continue = False
        print(f"the winner is {max_key} with a bid of ${max_value}.")
        break
    else:
        clear_terminal()
