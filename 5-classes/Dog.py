'''
Dog.py
This is a basic dog class

A class is how you create more OBJECTS from that class
Example: 
  Pitbull is an object of the dog class
  The pitbull TRAITS will be the class MEMBERS
'''


class Dog:
    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight


# now cook up some functions and progrums to read the members of the class.
# remeber to use the dot "." to access class members

dash = Dog("DASHIE", 3, 65)

# this is how you acess the members to READ Them
print(dash._name)
print(dash._age)
print(dash._weight)

# you can even change them (Write them)
dash._name = 'DASHER DASHER'
print(dash._name)
