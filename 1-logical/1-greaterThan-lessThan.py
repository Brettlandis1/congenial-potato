'''
a logic operator is a simple way to compare 2 variables
the result will always be TRUE or FALSE
'''

number1 = 5
number2 = 10

# this should be false since number 2 is greater
print('Is number one greater than number 2?')
print(number1 > number2)

# this should be true since number 2 is greater
print('Is number two greater than number one?')
print(number1 < number2)

# you can also store the result of a comparison in a variable.
# this is very helpful
isNumber1Greater = number1 > number2
print('here is the same thing stored in a variable')
print(isNumber1Greater)

'''
heres another example using greater than OR equal to
'''

number3 = 5
number4 = 5

# this should be false since number 3 is NOT less than
print('Is number three less than number4?')
print(number3 < number4)

# this should be TRUE since number 3 is less than OR EQUAL to number4
print('Is number three less than or equal to number4?')
print(number3 <= number4)
