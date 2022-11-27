'''
given a list of names, create a function that
searches through the list of names and:
  print true if the name occurs in the list
  print false if the name does not occur in the list
'''

playerNames = ["Scott", "Brett", "Matt", "Will", "Lambo", "Trevor"]
  
def findPlayer(name):
  
  foundName = False                    # return value
  playerNamesLength = len(playerNames) # length of array
  
  print("Searching for name: " + name)
  
  # loop thru array 
  for i in range(playerNamesLength):
    # if this element matches the input, update the return value
    if(name == playerNames[i]):
      foundName = True
    
  # remeber, we declared this variable as false, so it wont change unless its found!  
  # if the name is not found, no changes needs to be done
  return foundName   
  
# ========= example output ========= #
test1 = findPlayer("Scott") # true
print(test1)

test2 = findPlayer("Petro") # false
print(test2)

  