class Card:
    def __init__(self, _id, _value, _suit, _cardtype):
        self.id = _id
        self.value = _value
        self.suit = _suit
        self.cardtype = _cardtype

    def peek(self):
        '''print card details'''
        print(self.id, self.value, self.suit, self.cardtype)
