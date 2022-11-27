# here is a Dawg class

class Dawg:
    def __init__(self, _name, _age, _weight):
        self.name = _name
        self.age = _age
        self.weight = _weight

    def sayHello(self):
        print("Hello", self.name, "age:", self.age, "weight:", self.weight)


# create a dawg named dexter, with age 8 and weighs 125LBS
dexter = Dawg("Dexter", 8, 125)
dash = Dawg("dash", 2, 65)
robert = Dawg('robert', 5, 63)
harold = Dawg('harold', 9, 25)
steven = Dawg('steven', 5, 165)
hubert = Dawg('hubert', 11, 95)
bill = Dawg('bill', 11, 95)

# why isnt this working grandpa????
Dawgies = [dexter, dash, robert, harold, steven, hubert, bill]

for item in Dawgies:
    item.sayHello()
