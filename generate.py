# import random #gives you access all functions in that library
#must use random.choice if we use import random
from random import choice, randint, shuffle # to import the specific choice function you need

cards = ['jack', 'queen', 'king', 'joker']
shuffle(cards)
for card in cards:
    print(card, end=" ")

'''
coin = choice(['heads', 'tails'])
integer = randint(1, 1000)
print(coin, integer)
'''