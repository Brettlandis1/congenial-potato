'''In this program, I will create a black jack game'''

#Intro/Dealers hand
print('Hello, Welcome to Blackjack!')
print('(RULES)')
print('The object of this game is to beat the dealers hand, without going over 21')

    #list of suits
card_suits = ['spades', 'hearts', 'clubs', 'diamonds']
#list of the possible card value
card_values = ['1', '2', '3,' '4', '5', '6', '7', '8', '9', '10', '11']

#dealers cards
print('The dealers card is...')
import random
print(random.choice(card_suits))
print(random.choice(card_values))
#Your cards
print("Your cards are...")
print(random.choice(card_suits))
print(random.choice(card_values))
print(random.choice(card_suits))
print(random.choice(card_values))

#do you want to bust or stand

user_input = input('stand or bust?')

if user_input.lower() == 'stand':
  print('You picked stand!')
elif user_input.lower() == 'bust':
 print('You picked bust!')
else:
  print('Type stand or bust:')
  