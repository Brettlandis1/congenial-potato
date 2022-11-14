'''
use an if block to determine which number is larger. 
Use al else block if they are both equal
'''


def getGreaterInt(input1, input2):

    print("Comparing", input1, "vs", input2)

    # if():
    if input1 > input2:
        print('input1 is greater')

    # elif():
    elif input1 < input2:
        print('input1 is less')

    # else:
    else:
        print('theyre equal')


getGreaterInt(1, 2)
getGreaterInt(2, 1)
getGreaterInt(2, 2)
