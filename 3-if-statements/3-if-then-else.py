'''
if-then-else statements
Add an else block that will run if none of the conditions are true!
'''

boys = 7
girls = 7

print("Are there more boys or girls?")

# this block will be FALSE. Therefore it will go to the next block we provided
if(boys > girls):
  print("boys")

# this block will be FALSE. Therefore it will go to the next block we provided
elif(girls > boys):
  print("girls")

# no condition required. Just the word else
else:
  print("There are an equal number of boys and girls")
