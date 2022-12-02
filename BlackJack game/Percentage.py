import random
from Deck_Values import deck_value
from Random_Deck import getcards


def randomPercentage(percent): 
    perc = float(percent)
    num = float(random.randint(0, 100))
    if num <= perc:
        return True
    return False

 
def isDeckPulling(own,person=list):
    repeat = True
    Decks = print(f"Dealer's Deck: {person}\nYour Deck: {own}\n")
    while repeat:
        if deck_value(person) <= 5:
            if randomPercentage(95) == True:
                card1 = getcards(1)
                print(f"Dealer pulled : {card1[0]}")
                person.append(card1[0])
                repeat = True
            else:
                print("Dealer'S Standing")
                Decks
                repeat = False
            
        elif deck_value(person) <= 10:
            if randomPercentage(90) == True:
                card1 = getcards(1)
                print(f"Dealer pulled : {card1[0]}")
                person.append(card1[0])
                repeat = True
            else:
                print("Dealer'S Standing")
                Decks
                repeat = False
            
            
        elif deck_value(person) <= 13:
            if randomPercentage(85) == True:
                card1 = getcards(1)
                print(f"Dealer pulled : {card1[0]}")
                person.append(card1[0])
                repeat = True
            else:
                print("Dealer'S Standing")
                Decks
                repeat = False
            
        elif deck_value(person) <= 15:
            if randomPercentage(50) == True:
                card1 = getcards(1)
                print(f"Dealer pulled : {card1[0]}")
                person.append(card1[0])
                repeat = True
            else:
                print("Dealer'S Standing")
                Decks
                repeat = False
                            
        elif deck_value(person) <= 18:
            if randomPercentage(7) == True:
                card1 = getcards(1)
                print(f"Dealer pulled : {card1[0]}")
                person.append(card1[0])
                repeat = True
            else:
                print("Dealer'S Standing")
                repeat = False
            
            
                
        elif deck_value(person) <= 20:
            if randomPercentage(3) == True:
                card1 = getcards(1)
                print(f"Dealer pulled : {card1[0]}")
                person.append(card1[0])
                repeat = True
            else:
                print("Dealer'S Standing")
                Decks
                repeat = False
            
        elif deck_value(person) > 21:
            repeat = False 
        else :
            Decks
            print("Dealer has BlackJack!\n")
            repeat = False
        

            
    

