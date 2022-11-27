from CardHand import *


class Dealer(CardHand):
    ''' 
    this right here is a superclass. 
    A superclass is gud here because the dealer and CardHand share some attributes
    So its better to just modify them slightly instead of copy and paste.
    '''

    def __init__(self):
        # heres a cool python trick. Use underscores where commas would be (100,00,000 = 100_000_000)
        self.money = 100_000_000
        self.move = None
        super().__init__("dealer", True)

    def decideMove(self):

        self.calculateScore()

        if(self.score > 21):
            self.move = "busted"

        elif(self.score >= 17):
            self.move = "stay"

        else:
            self.move = "hit"

        print('Dealer move:', self.move)
        return self.move
