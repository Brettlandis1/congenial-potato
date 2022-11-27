'''In this prgrum, I will have some math equations to solve'''
# welcome page
print('I have some questions for you to solve Scott:')

# Here is the list of questions, the answer, guess, and guess number
print('What is 4x10')
answer = 40
guess = 0
guessnum = 1
# While loop
while (answer != guess and guessnum <= 3):
    guess = int(input('What is the Answer?'))
    guessnum += 1

# see result
if (answer == guess):
    print('That is correct brother!')

else:
    print('Incorrect.')
