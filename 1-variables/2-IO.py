''' 
in software, IO means input and output
Python has built in specific functions for inputing and outputing data 
which allows you to enter data in the terminal while the program is running, and see results of data
To input data: we will use the input() function
To output data: we will use the print() function
'''

apples = input("How many apples do you have?: ")
oranges = input("How many oranges do you have?: ")
print('Apples: ', apples)
print('Oranges: ', oranges)

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

# in python we can print multiple things by using a comma
# also, it doesnt matter if you use ' ' or " " but they must both match!
print('Full Name:', firstName, lastName)