#Ankush Joshi
#August 16, 2024
#11/100 - BlackJack Game

from art import logo
import random

def checkWinner(cardList1, cardList2):
    isBust = False

    if checkBust(cardList1):
        isBust = True
        print(f"Your final hand: {cardList1}\n > Total: {sum(playerCards)}")
        print("BUST! You lose")
    else:
        isBust = False
    if checkBust(cardList2):
        bust = True
        print(f"Computer's final hand: {cardList2}\n > Total: {sum(computerCards)}")
        print("Computer BUSTS! You Win")
    else:
        isBust = False

    if not isBust:
        if sum(cardList1) > sum(cardList2):
            print(f"Your final hand: {cardList1}\n > Total: {sum(playerCards)}")
            print(f"Computer's final hand: {cardList2}\n > Total: {sum(computerCards)}")
            print("You win!")
        elif sum(cardList1) < sum(cardList2):
            print(f"Your final hand: {cardList1}\n > Total: {sum(playerCards)}")
            print(f"Computer's final hand: {cardList2}\n > Total: {sum(computerCards)}")
            print("You lose")
        else:
            print(f"Your final hand: {cardList1}\n > Total: {sum(computerCards)}")
            print(f"Computer's final hand: {cardList2}")
            print("It's a tie")
    print(">--< >--< >--< >--< >--< >--< >--< >--< >--< >--<")

def checkBust(cardList):
    total = 0
    bust = False
    if sum(cardList) > 21:
        bust = True
    else:
        bust = False

    return bust
def pickCards(cardList):
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    cardList.append(card1)
    cardList.append(card2)
    return card1, card2

def checkBlackjack(cardList):
    blackjack = False
    if cardList == [1,10] or cardList == [10,1] or cardList == [11,10] or cardList == [10,11]:
        blackjack = True
    else:
        blackjack = False

    return blackjack

gameOver = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while not gameOver:
    playerCards = []
    computerCards = []
    choice = input("Would you like to play a game of Blackjack? Type 'yes' or 'no': ").lower()
    if choice == 'no':
        print("Exiting...")
        gameOver = True
    elif choice == 'yes':
        print(logo)
        pickCards(playerCards)
        pickCards(computerCards)
        computerCards = [1,1]

        print(f"Your cards: {playerCards}")
        print(f"Computer's first card: {computerCards[0]}")

        if checkBlackjack(playerCards):
            print(f"Your final hand: {playerCards}\n > Total: {sum(playerCards)}")
            print("BLACKJACK! You win!")

        elif checkBlackjack(computerCards):
            print(f"Computer's Final Hand: {computerCards}\n > Total: {sum(computerCards)}")
            print("BLACKJACK! Computer wins!")


        deal = ''
        while deal not in ['y', 'n']:
            deal = input("Type 'y' to get another card, type 'n' to pass ")
            if deal not in ['y', 'n']:
                print("Please type 'y' or 'n'")
        if deal == 'n':
            print(">--< >--< >--< >--< >--< >--< >--< >--< >--< >--<")
            playerTotal = sum(playerCards)
            computerTotal = sum(computerCards)
            while computerTotal < 17:
                newCard = random.choice(cards)
                computerCards.append(newCard)
                computerTotal = sum(computerCards)
            #print(f"Computer's Hand: {computerCards}")
            if computerTotal > 21:
                print(f"Computer's final hand: {computerCards} \n> Total: {computerTotal}")
                print("BUST! You win")
            elif computerTotal <= 21:
                checkWinner(playerCards, computerCards)

        elif deal == 'y':
            playerCard3 = random.choice(cards)
            playerCards.append(playerCard3)
            bust = checkBust(playerCards)

            if bust:
                print(f"Your final hand: {playerCards}\n > Total: {sum(playerCards)}")
                print(f"Computer's final hand: {computerCards}\n > Total: {sum(computerCards)}")
                print("BUST! You lose")
            else:
                checkWinner(playerCards, computerCards)
        else:
            print("Please type 'y' or 'n'")

    else:
        print("Please enter 'yes' or 'no' only ")


