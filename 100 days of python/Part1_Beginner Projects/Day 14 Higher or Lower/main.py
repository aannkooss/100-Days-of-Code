#Ankush Joshi
#August 31, 2024
#Day 14/100 - Higher Lower Game

import random
from art import logo, vs
from game_data import data


def accountFormatter(account):
    accountName = account["name"]
    accountDescription = account["description"]
    accountCountry = account["country"]
    return f"{accountName}, a {accountDescription}, from {accountCountry}"

def checkAnswer(account1, account2, guess):
    if account1["follower_count"] > account2["follower_count"]:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
gameOver = False
account2 = random.choice(data)

while not gameOver:
    account1 = account2
    account2 = random.choice(data)

    if account1 == account2:
        account2 = random.choice(data)

    print(f"Compare A: {accountFormatter(account1)}")
    print(vs)
    print(f"Against B: {accountFormatter(account2)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    isCorrect = checkAnswer(account1, account2, answer)
    if isCorrect:
        score += 1
        print(f"You're Right! Current Score: {score}\n")
        gameOver = False
    else:
        print(f"Sorry that is incorrect. Final Score: {score}\n")
        gameOver = True



