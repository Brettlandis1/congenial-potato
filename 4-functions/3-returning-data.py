''' 
Sometimes functions dont return anything (examples 1 and 2 all we do is print the result)
Its best to return something, then output it elsewhere
'''

def greaterValue(input1, input2):
  output = 0

  print('Comparing', input1, "vs", input2)
  
  if(input1 > input2):
    output = input1

  elif(input1 < input2):
    output = input2

  else: 
    output = "They are equal"  

  return output


# since we dont print anything in the function, we must do it manually
print(greaterValue(10, 5))  

# we can also pass variables as parameters
value1 = 55
value2 = 100
print(greaterValue(value1, value2))

# and even store the result of the function in a variable (best way to do this)
resultOfFunction = greaterValue(500, 500)
print(resultOfFunction)
