def start():

    # target to guess
    print('2 tries')
    answer = 'brett'
    guess = ''
    guessNum = 1

    while (answer != guess and guessNum <= 2):

        guess = input('Who has less receiving yards: ')

        if (answer == guess):
            print('correct :)')
            return True

        else:
            print('false')
            guessNum += 1

    return None


start()
