''' 
Parameters are how we provide input to a function. 
Watch how we can use the same function multiple times with different inputs!
'''

def sayHello(input):
  print("Hello", input, "!")

name1 = 'Jon'
name2 = 'David'
name3 = 'Alex'

sayHello(name1)  
sayHello(name2) 
sayHello(name3)
sayHello("Thomas") # this works too! but best to keep your data in variables