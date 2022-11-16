# here is a Dawg class

class Dawg:
    def __init__(self, _name, _age, _weight, _fightingAbility):
        self.name = _name
        self.age = _age
        self.weight = _weight
        self.fightingAbility = _fightingAbility

    def sayHello(self):
        print("Hello", self.name, "age:", self.age, "weight:", self.weight)

# create a dawg named dexter, with age 8 and weighs 125LBS
dexter = Dawg("Dexter", 8, 125, 81)
dash = Dawg("dash", 2, 65, 91)
robert = Dawg('robert', 5, 63, 94)
harold = Dawg('harold', 9, 25, 35)
steven = Dawg('steven', 5, 165, 57)
hubert = Dawg('hubert', 11, 95, 15)
bill = Dawg('bill', 11, 95, 82)
#why isnt this working grandpa????
Dawgies = [dexter, dash, robert, harold, steven, hubert, bill]
print(Dawgies)


#round 1
#dexter vs dash
print('dexter vs dash', 'The winner is.....')
