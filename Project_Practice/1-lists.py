'''
given a list of names, create a function that
searches through the list of names and:
  print true if the name occurs in the list
  print false if the name does not occur in the list
'''


def findPlayer(name):
  
  print("Searching for name: " + name)
  
  playerNames = ["Scott", "Brett", "Matt", "Will", "Lambo", "Trevor"]
  
  for i in range(len(playerNames)):
    if(name == playerNames[i]):
      print('true')
      return
  print('false')
   
  
# example output:
findPlayer("Scott") # true
findPlayer("Petro") # false


  