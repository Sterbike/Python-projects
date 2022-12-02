import random
from Values import card_values

times=0
def getcards(times):
    cards = []
    num=0
    while num < times:
        randomvalue = random.choice(list(card_values))
        cards.append(randomvalue)
        num += 1
    return cards



