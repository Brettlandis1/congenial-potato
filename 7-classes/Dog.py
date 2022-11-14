'''
Dog.py
This is a basic dog class

A class is how you create more OBJECTS from that class
Example: 
  Pitbull is an object of the dog class
  The pitbull TRAITS will be the class MEMBERS
'''


class Dog:
    def __init__(self, _name, _age, _weight):
        self.name = _name
        self.age = _age
        self.weight = _weight


# now cook up some functions and progrums to read the members of the class.
# remeber to use the dot "." to access class members

dash = Dog("DASHIE", 3, 65)

# this is how you acess the members to READ Them
print(dash.name)
print(dash.age)
print(dash.weight)

# you can even change them (Write them)
dash.name = 'DASHER DASHER'
print(dash.name)
