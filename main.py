"""Final Project: Secret Bidder"""
from ascii import title

# TODO 1: Make an empty dictionary and while parameters
bid_log = {}
still_bidding = True


# TODO 3: Making a function to find highest bid
def highest_bid():
    max_bid = 0
    for bidder in bid_log:
        if bid_log[bidder] > max_bid:
            max_bid = bid_log[bidder]
            winner = bidder
    print('\n' * 100)
    print(title)
    print(f"\nThe winner is {winner} with ${max_bid} bid.")


# TODO 2: Saving the bidder
bidder_count = 1
while still_bidding:
    print(title)
    print("Welcome to the blind bidding")
    print(f"Bidder Count: [{bidder_count}]")
    # Inputting bid data from user
    name = input("Please enter your name:\t")
    bid_value = int(input("Please enter your bid:\t$"))
    other_bidder = input("Is there any other bidder? [Y/N] ")
    # Saving bid data to bid_log
    bid_log[name] = bid_value

    # Stopping the while loop
    if other_bidder.upper() == 'N':
        still_bidding = False
        highest_bid()
    else:
        bidder_count += 1
        print('\n' * 20)
