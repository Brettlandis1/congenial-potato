from Card import *


class CardHand:

    def __init__(self, _name, _isDealer):
        self.cards = []
        self.name = _name
        # the card score the CardHand has each hand
        self.score = 0
        self.isDealer = _isDealer
        print("Initialized", self.__repr__())

    def __repr__(self):
        return f'CardHand(cards={self.cards} name={self.name} score={self.score} isDealer={self.isDealer})'

    def calculateScore(self):
        self.score = 0
        for card in self.cards:
            print(card.__repr__())

            self.score += card.value

        print("Player", self.name, "score:", self.score)
        return self.score

    def hit(self, newCard):
        self.cards.append(newCard)
