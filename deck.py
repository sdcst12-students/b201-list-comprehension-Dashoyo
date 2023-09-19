#!python3
import random
ask = int(input("How many cards do you want?"))
ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['C','D','H','S']

deck = [f"{i}{j}"for i in ranks for j in suits]

for i in deck:

    def shuffle():
        random.shuffle(deck)
        return shuffle
    def draws():
        ask = int(input("How many cards do you want?"))
        draw = []
        for i in range(ask):
            draw.append(deck[i])
            deck.pop(i)
            
        return draw

