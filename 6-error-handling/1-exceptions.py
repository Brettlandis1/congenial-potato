'''
an exception in programming is a way to handle errors in your software.
The try block lets you test a block of code for errors.
The except block lets you handle the error.
'''

# this wont work since we never made a variable "xValue"
try:
  print(xValue)

# since there is an error, we can fix it in the except block
except:
  # explain the error
  print("An exception occurred! X is not defined. Assigning a default value")
  # fix the error
  xValue = 7
  print(xValue)

