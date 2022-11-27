from CardHand import *
from constants import *


class Player(CardHand):
    ''' 
    this right here is a superclass. 
    A superclass is gud here because the player and CardHand share some attributes
    So its better to just modify them slightly instead of copy and paste.
    '''

    def __init__(self, _name, _money):
        self.name = _name
        self.money = _money
        self.move = None
        super().__init__(_name, False)

    def makeWager(self):
        print("You have", self.money, "$")
        wagerAmount = int(input("What is your wager?"))

        # make sure they have enough money
        if(wagerAmount <= self.money):
            return wagerAmount

        else:
            print("You do not have enough money to make that wager!")
            # run it again
            self.makeWager()

    def playHand(self):
        move = input("What is your move? ").lower()

        if(move == 'h'):
            self.move = "hit"

        elif(move == 's'):
            self.move = "stay"

        else:
            print("Invalid move. Please select from", VALID_MOVES)
            # recursion! We can run this funtion again from inside of itself.
            # way cleaner than a loop
            self.playHand()

        '''note: future feature
        # elif(move == 'sp'):
            self.move = "split"
        '''
