from Card import *
import random

SUITS = ['spades', 'hearts', 'clubs', 'diamonds']
CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
CARDS_PER_SUIT = 13


class Deck:
    def __init__(self):
        self.cards = []

        self.cardId = 0

        self.initSuit(SUITS[0])
        self.initSuit(SUITS[1])
        self.initSuit(SUITS[2])
        self.initSuit(SUITS[3])

        print("Deck initialized")

    def printDeck(self):
        for card in self.cards:
            print(card.__repr__())

    def shuffle(self):
        #print("Shuffling cards.")
        random.shuffle(self.cards)

    def dealCard(self):
        nextCard = self.cards.pop()
        print("dealing card", nextCard.__repr__())
        return nextCard

    def initSuit(self, suit):
        ''' return 13 cards of specific suit'''

        # first create regular cards
        for i in range(len(CARD_VALUES)):
            currentCard = Card(self.cardId, CARD_VALUES[i], suit, "numeric")
            self.cards.append(currentCard)
            self.cardId += 1

        # create face cards
        self.cards.append(Card(self.cardId, 10, suit, "jack"))
        self.cardId += 1

        self.cards.append(Card(self.cardId, 10, suit, "queen"))
        self.cardId += 1

        self.cards.append(Card(self.cardId, 10, suit, "king"))
        self.cardId += 1

        self.cards.append(Card(self.cardId, 11, suit, "ace"))
        self.cardId += 1
