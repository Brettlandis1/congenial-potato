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

#Dexter
print(dexter.name)
print(dexter.age)
print(dexter.weight)
print(dexter.fightingAbility)
#dash
print(dash.name)
print(dash.age)
print(dash.weight)
print(dash.fightingAbility)
#robert
print(robert.name)
print(robert.age)
print(robert.weight)
print(robert.fightingAbility)
#harold
print(harold.name)
print(harold.age)
print(harold.weight)
print(harold.fightingAbility)
#steven
print(steven.name)
print(steven.age)
print(steven.weight)
print(steven.fightingAbility)
#hubert
print(hubert.name)
print(hubert.age)
print(hubert.weight)
print(hubert.fightingAbility)
#bill
print(bill.name)
print(bill.age)
print(bill.weight)
print(bill.fightingAbility)

#round 1
#dexter vs dash
print('dexter vs dash')
print('the winner is....')
#what'd I do wrong on this?????
if Dawg(dexter > dash):
    print('dexter')
elif Dawg(dexter > dash):
    print('dash')