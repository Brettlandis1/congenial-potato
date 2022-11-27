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

    def __repr__(self):
        return f'Player(name={self.name} money={self.money} move={self.move})'

    def makeWager(self):
        print("You have", self.money, "$")
        wagerAmount = float(input("What is your wager? "))

        # make sure they have enough money
        if(wagerAmount > self.money):
            print("You do not have enough money to make that wager!")
            # run it again
            self.makeWager()

        # once the amount is legal return it
        print("You wagered $", wagerAmount)
        return wagerAmount

    def decideMove(self):

        self.calculateScore()

        if(self.score > 21):
            self.move = "busted"
            print("BUST")
            return self.move

        moveInput = input("What is your move? ").lower()

        if(moveInput == 'h'):
            self.move = "hit"
            return self.move

        elif(moveInput == 's'):
            self.move = "stay"
            return self.move

        else:
            print("Invalid move. Please select from", VALID_MOVES)
            # recursion! We can run this funtion again from inside of itself.
            # way cleaner than a loop
            self.move = 'INVALID'
            self.playHand()

        '''note: future feature
        # elif(move == 'sp'):
            self.move = "split"
        '''

    def printMoney(self):
        print("Current money: " + str(self.money))
