from art import logo

def find_the_highest_bidder(anybids):
    highest_bid = 0
    winner = ""
    for bidder in anybids:
        bid_amount = anybids[bidder][1]
        bid_items = anybids[bidder][0]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner for the item {bid_items} is {winner}, with the highest bid of ${highest_bid}.")



trade_items = {}

print(logo)
print("Welcome to the Secret Mafia Auction Program.")

istrue = True

start_trade = input("Would you like to make a trade? enter yes or no: ").lower()
if start_trade == "yes":
    while istrue:

        items = input("What item would you like to trade in the Auction house: ").title()
        cost = int(input("What is your starting price? :$ "))

        trade_items[items] = cost

        additems = input("Would you like to add any else? Yes/No: ").lower()

        if additems == "no":
            istrue = False

    print("Here are the Items up for Bidding.")
    for item, price in trade_items.items():
        print(f"item: {item}, with a starting price of : ${price}")


    start_bid = input("would you like to start bidding?: ").lower()

    if start_bid == "yes":

        bids = {}
        continue_bidding = True
        while continue_bidding:
            name = input("Please input your name: ")
            bid_item = input("Please input the name of item you are bidding for: ")
            bid_price = int(input("Please input your bid?: $"))
            bids[name] = [bid_item, bid_price]
            should_continue = input("Are there any other bidders? Yes/No: ").lower()
            if should_continue == "no":
                find_the_highest_bidder(bids)
                continue_bidding = False

    else:
        istrue = False

else:
    print("No Trades were made")
