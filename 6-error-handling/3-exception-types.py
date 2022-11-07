'''
we can specify the type of exception we want to look out for, and how to handle it 
'''

# name error means the variable is not defined
try:
  print(xValue)
except NameError:
  print("Variable xValue is not defined")
  xValue = 10
except:
  print("Something else went wrong")
  xValue = 200
finally:
  print(xValue)


myInteger = 1
myString = "Hello World"

try:
  print(myInteger + myString)
except TypeError:
  print("Int cannot be added to string! Handling")
  # Handle it! convert int to string 
  myInteger = str(myInteger)
finally:
  print("Finally result:")
  print(myInteger + myString)


