class TicTacToeBoard:

    pos1 = "  "
    pos2 = "  "
    pos3 = "  "
    pos4 = "  "
    pos5 = "  "
    pos6 = "  "
    pos7 = "  "
    pos8 = "  "
    pos9 = "  "

    movesPlayed = 0
    playerXTurn = True

    def __init__(self):
        self.displayBoard()

    def displayBoard(self):
        print(self.pos1 + "|" + self.pos2 + "|" + self.pos3)
        print("--------")
        print(self.pos4 + "|" + self.pos5 + "|" + self.pos6)
        print("--------")
        print(self.pos7 + "|" + self.pos8 + "|" + self.pos9)

    def makeMove(self, position, character):
        if position == 1:
            self.pos1 = character
        elif position == 2:
            self.pos2 = character
        elif position == 3:
            self.pos3 = character
        elif position == 4:
            self.pos4 = character
        elif position == 5:
            self.pos5 = character
        elif position == 6:
            self.pos6 = character
        elif position == 7:
            self.pos7 = character
        elif position == 8:
            self.pos8 = character
        elif position == 9:
            self.pos9 = character


board = TicTacToeBoard()

while (board.movesPlayed < 10):
    board.displayBoard()

    if board.playerXTurn == True:
        marker = 'X '
        movePosition = int(input("Player X, where would you like to move"))

    else:
        marker = 'O '
        movePosition = int(input("Player O, where would you like to move"))

    board.movesPlayed += 1
    board.makeMove(movePosition, marker)
    # toggle a true false variable
    board.playerXTurn = not board.playerXTurn
