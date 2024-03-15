#Deck class
import random
#Global values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank +" of "+self.suit

class Deck():
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                Created_Card=card(suit,rank)
                self.all_cards.append(Created_Card)

    

    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()
    
class Player:
    def __init__(self,name):
        self.name=name
        self.all_card=[]

    def remove_one(self):
        return self.all_card.pop(0)

    def add_cards(self,new_card):
        if type(new_card)==type([]):
            self.all_card.extend(new_card)
        else:
            self.all_card.append(new_card)
        
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_card)} cards.'

if __name__=='__main__':
    #Creating Player
    Player_1=Player("one")
    Player_2=Player("Two")

    new_deck=Deck()
    new_deck.shuffle()

    for x in range(26):
        Player_1.add_cards(new_deck.deal_one())
        Player_2.add_cards(new_deck.deal_one())
    
    game_on=True

    #While Game on loop
    round_num=0
    while game_on:
        round_num+=1
        print(f"Round {round_num}\n")
        if(len(Player_1.all_card)==0):
            print('Player one is out of card\n Player two wins')
            game_on=False
        if(len(Player_2.all_card)==0):
            print('Player 2 wins ')
            game_on=False
        
        #start new round
        player_1_current_card=[]
        player_1_current_card.append(Player_1.remove_one())

        player_2_current_card=[]
        player_2_current_card.append(Player_2.remove_one())
        
        at_war=True

        while at_war:
            if((player_1_current_card[-1].value) > (player_2_current_card[-1].value)):
                Player_1.add_cards(player_1_current_card)
                Player_1.add_cards(player_2_current_card)
                
                at_war=False

            elif((player_2_current_card[-1].value)> (player_1_current_card[-1].value)):
                Player_2.add_cards(player_2_current_card)
                Player_2.add_cards(player_1_current_card)
                at_war=False

            else:
                print("\n****WAR****")
                if((len(Player_2.all_card))<5):
                    print("Player 1 unable to play \nPlayer 2 wins! in WAR ")
                    game_on=False
                    break

                elif(len(Player_1.all_card)<5):
                    print("Player 2 unable to play \nPlayer 1 wins! in WAR")
                    game_on=False
                    break
                
                else:
                    for num in range(5):
                        player_1_current_card.append(Player_1.remove_one())
                        player_2_current_card.append(Player_2.remove_one())
                    




