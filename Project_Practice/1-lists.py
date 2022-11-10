'''
given a list of names, create a function that
searches through the list of names and:
  print true if the name occurs in the list
  print false if the name does not occur in the list
'''

playerNames = ["Scott", "Brett", "Matt", "Will", "Lambo", "Trevor"]

# research how to access a list element 
print("The first name in this list is: " + playerNames[0])

def findPlayer(name):
  print("Searching for name: " + name)
  # loop through the list 
  # if the element is found in the list, print true


# example output:
findPlayer("Scott") # true
findPlayer("Petro") # false