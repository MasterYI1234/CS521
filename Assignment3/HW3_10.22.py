# -*- coding: utf-8 -*-
"""
CS521
10.22
"""
import random

# Make the deck

deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

cards = []

cards_suits = []

#Make the choose of the card

n = 0
m = 0

while n<4:
    card_deck = random.choice(deck)
    card_suit = random.choice(suit)
    if card_suit in cards_suits:
        m +=1
        n = len(cards_suits)
    else:
        cards.append(card_deck+" of "+card_suit)
        cards_suits.append(card_suit)
        n +=1
        m +=1
# Print the output
for x in cards:
    print(x)
print("Number of picks:",m)