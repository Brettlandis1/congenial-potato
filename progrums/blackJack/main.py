import random
from card import *
from deck import *


def getScore(hand):
    score = 0
    for i in range(len(hand)):
        score += hand[i].value

    return score


deck1 = Deck()
# deck1.printDeck()
print("Shuffling cards.")
deck1.shuffle()
deck1.printDeck()

# print(len(deck1.cards))

# deal 2 cards
playerCards = [deck1.cards.pop(), deck1.cards.pop()]
dealerCards = [deck1.cards.pop(), deck1.cards.pop()]

# print(len(deck1.cards))

# get values
playerScore = getScore(playerCards)
dealerScore = getScore(dealerCards)

print(playerCards)
print(dealerCards)

print(playerScore)
print(dealerScore)
