'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

# this wont work since we never made a variable "xValue"
try:
  print('try xValue:', xValue)

# since there is an error, we can fix it in the except block
except:
  # explain the error
  print("An exception occurred! X is not defined. Assigning a default value")
  # fix the error
  xValue = 7

# this will run no matter what!
finally:
  print('finally xValue:', xValue)