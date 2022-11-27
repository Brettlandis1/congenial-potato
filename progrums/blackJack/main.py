from Card import *
from Deck import *
from Player import *
from Dealer import *

deck1 = Deck()
deck1.shuffle()

player = Player("Scott", 100)
dealer = Dealer()

currentWager = player.makeWager()
print(currentWager)

player.cards = [deck1.cards.pop(), deck1.cards.pop()]
dealer.cards = [deck1.cards.pop(), deck1.cards.pop()]

player.calculateScore()
dealer.calculateScore()

player.playHand()
