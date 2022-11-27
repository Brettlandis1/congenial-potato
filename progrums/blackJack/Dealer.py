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
        super().__init__("dealer", True)

    def playHand(self):
        if(self.score > 21):
            return "bust"

        elif(self.score >= 17):
            return "stand"

        else:
            return "hit"
