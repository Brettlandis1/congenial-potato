from Card import *
from CardHand import *
from constants import *
from Dealer import *
from Deck import *
from main import *
from Player import *


class TestBlackJack:

    def __init__(self):
        self.testDeck = Deck()
        self.testPlayer = Player("test player", 100)

    def test_deck_len(self):
        assert len(self.testDeck) == 52

    def test_invalid_wager(self):
        assert type(self.testPlayer.makeWager()).__name__ == "int"
