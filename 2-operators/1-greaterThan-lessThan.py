'''
a logic operator is a simple way to compare 2 variables
the result will always be TRUE or FALSE
'''

number1 = 5
number2 = 10

# this should be false since 10 is greater
print('Is 5 greater than 10?')
print(number1 > number2)

# this should be true since 10 is greater
print('Is 10 greater than 5?')
print(number1 < number2)

'''
heres another example using greater than OR equal to
'''

number3 = 5
number4 = 5

# this should be TRUE since number3 is less than OR EQUAL to number4
print('Is 5 less than or equal to 5?')
print(number3 <= number4)

# this should be false since number3 is NOT less than
print('Is 5 less than 5?')
print(number3 < number4)

# you can also store the result of a comparison in a variable.
# this is very helpful
isNumber1Greater = number1 > number2
print('Is 5 greater than 10? (Stored in a variable)')
print(isNumber1Greater)