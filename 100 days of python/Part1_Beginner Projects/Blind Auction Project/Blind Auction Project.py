#Ankush Joshi
#August 13, 2024
#Day 9/100 - Blind Auction Project
#Topic: Dictionaries

from art import gavel
print(gavel)
bids = {}
keepBidding = True

def compareBids(biddingDictionary):
    winner = ""
    highestBid = 0
    for bidder in biddingDictionary:
        bidAmount = biddingDictionary[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}")

    #using max function:
    #highestBid = max(biddingDictionary, key=biddingDictionary.get)
    #print(highestBid)

while keepBidding:
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    bids[name] = bid
    keepBidding = input("Are there any other bidders?: Type 'yes' or 'no':  ").lower()

    if keepBidding == 'yes':
        keepBidding = True
        print("\n" * 100)
    elif keepBidding == 'no':
        keepBidding = False
        compareBids(bids)
    else:
        print("Please type 'yes' or 'no': ")