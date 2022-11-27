class Card:
    def __init__(self, _id, _value, _suit, _cardtype):
        self.id = _id
        self.value = _value
        self.suit = _suit
        self.cardtype = _cardtype

    def __repr__(self):
        '''print card details'''
        return f'Card(id={self.id} value={self.value} suit={self.suit} cardtype={self.cardtype})'
