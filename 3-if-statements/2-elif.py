'''
if-else statements
elif means if the if-block above it ends up being false, the next one will run if its true 
'''

apples = 10
oranges = 4

print("Are there more apples or oranges?")

# this block will be FALSE. Therefore it will go to the next block we provided
if(oranges > apples):
  print("Oranges")

# this block will be TRUE and run. 
elif(apples > oranges):
  print("Apples")


''' You can add as many elif blocks as you wish '''
boys = 7
girls = 14

print("Are there more boys or girls?")

# this block will be FALSE. Therefore it will go to the next block we provided
if(boys > girls):
  print("boys")

# this block will be TRUE and run. 
elif(girls > boys):
  print("girls")

# this block will be TRUE HOWEVER it will not run because the one above it will execute, and end the if-else process. 
elif(boys >= 0):
  print("boys greater than zero")
  print("I will not run!")
