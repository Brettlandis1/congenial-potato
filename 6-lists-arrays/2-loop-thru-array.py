'''
one of the most useful thing a loop can do is go through an array
'''

# this will print every element in list
playerNames = ['Scott', 'Brandon', 'Brett', 'Matt', 'Andrew', 'Will']

# use the len function to get the length of an object
lengthOfArray = len(playerNames)

# this will loop 6 times, since the length of the array is 6
for i in range(lengthOfArray):
  print('Element ' + str(i) + ' in list: ' + playerNames[i])