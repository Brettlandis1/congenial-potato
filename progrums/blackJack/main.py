from Card import *
from Deck import *
from Player import *
from Dealer import *


def initialDeal():
    playerCard1 = deck1.dealCard()
    dealerCard1 = deck1.dealCard()
    playerCard2 = deck1.dealCard()
    dealerCard2 = deck1.dealCard()

    player.cards.append(playerCard1)
    player.cards.append(playerCard2)
    dealer.cards.append(dealerCard1)
    dealer.cards.append(dealerCard2)

    player.calculateScore()
    dealer.calculateScore()


def playerTurn():
    print("\nIt is your turn.")
    while(player.move != 'stay' and player.move != 'busted'):

        # check for blackJack
        if(player.score == 21):
            print('blackJack!')
            return True

        player.decideMove()

        if(player.move == 'hit'):
            nextCard = deck1.dealCard()
            player.hit(nextCard)

    player.calculateScore()
    return player.score


def dealerTurn():
    print("\nDealer turn")
    while(dealer.move != 'stay' and dealer.move != 'busted'):

        # check for blackJack
        if(dealer.score == 21):
            print('blackJack!')
            return True

        dealer.decideMove()

        if(dealer.move == 'hit'):
            nextCard = deck1.dealCard()
            dealer.hit(nextCard)

    return dealer.score


deck1 = Deck()
deck1.shuffle()

player = Player("Scott", 100.00)
dealer = Dealer()
playAgain = True

while(playAgain and player.money > 0):

    currentWager = player.makeWager()

    # give cards
    initialDeal()

    playerTurn()
    dealerTurn()

    if (player.score == dealer.score):
        print("Push.")

    elif (player.score > dealer.score):
        player.money += currentWager
        print("Player wins!")

    elif (player.score < dealer.score):
        player.money -= currentWager
        print("Dealer wins...")

    elif(player.score > 21 and dealer.score <= 21):
        player.money -= currentWager
        print("Dealer wins...")

    player.printMoney()

    playAgainInput = input("Play again? (y/n): ")

    if(playAgainInput.lower() == 'n'):
        print("Okay!")
        playAgain = False
    else:
        playAgain = True
