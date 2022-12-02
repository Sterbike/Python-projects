from Random_Deck import getcards
from Deck_Values import deck_value
from Percentage import randomPercentage
from Percentage import isDeckPulling

repeat = True
while repeat:
    dealer = (getcards(2))
    own = (getcards(2))
    pulling = True
    while pulling:
            if deck_value(own) > 21: 
                print(f"Dealer's Deck: {dealer}\nYour Deck: {own} ")
                print("You Lost!")
                pulling = False
                repeat = False
                restarting = True
                while restarting:
                    restart = input("Would you like to restart? y/n \n ")
                    if restart == "y":
                        repeat = True
                        restarting = False
                    elif restart == "n":
                        repeat = False
                        restarting = False
                    else:
                        restarting=True
                        
                
            else:
                print(f"Dealer's Deck: '🂠', {dealer[1]}")
                print(f"Your Deck: {own}")
                pull=input("Would you like to pull a card? y/n \n ")
                if pull == "y":
                    newcard = getcards(1)
                    own.append(newcard[0])
                    pulling = True
                    
                elif pull == "n":
                    pulling = False  
                    isDeckPulling(own,dealer)
                    
                    if deck_value(dealer) > 21:
                        print (f"Dealer's Deck: {dealer}\nYour Deck: {own} ")
                        print("You Won!\n")
                        restart = input("Would you like to play again? y/n \n ")
                        if restart == "y":
                            repeat = True
                        else:
                            repeat = False
                        
                    else:
                        if deck_value(dealer) < deck_value(own):
                            print (f"Dealer's Deck: {dealer}\nYour Deck: {own} ")
                            print("You Won!")
                            restart = input("Would you like to play again? y/n \n ")
                            if restart == "y":
                                repeat = True
                            else:
                                repeat = False
                            
                        elif deck_value(dealer) > deck_value(own):
                            print (f"Dealer's Deck: {dealer}\nYour Deck: {own} ")
                            print("You lost!")
                            restart = input("Would you like to play again? y/n \n ")
                            if restart == "y":
                                repeat = True
                            else:
                                repeat = False
                            
                        else:
                            print (f"Dealer's Deck: {dealer}\nYour Deck: {own} ")
                            print("You Draw!")
                            restart = input("Would you like to play again? y/n \n ")
                            if restart == "y":
                                repeat = True
                            else:
                                repeat = False
                else:
                    pulling =True
                    repeat = True


                


    






