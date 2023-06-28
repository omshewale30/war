#Author: Om Shewale
#Description: This is a simple card game called war
import random

class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):

        return f"{self.rank} of {self.suit} \n"
class Deck():
    def __init__(self):
        self.deck=[]
        self.build()

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(1, 14):
                self.deck.append(Card(s, v))
        random.shuffle(self.deck)
    def show(self):
        for card in self.deck:
            print(card.__str__())
    def draw(self):
        return self.deck.pop(0)
    def add(self,cards):
        self.deck.extend(cards)

class Player():
    def __init__(self,name):
        self.name=name
        self.hand=[]

    def add_cards(self,cards):
        if isinstance(cards,list):
            self.hand.extend(cards)

        else:
            self.hand.append(cards)


    def remove_card(self,num):
        if num==1:
            return self.hand.pop(0)
        removed_cards=[]
        for i in range(num):
            removed_cards.append(self.hand.pop(0))

        return removed_cards

    def __str__(self):
        return f"{self.name} has {len(self.hand)} cards \n"
    def print_deck(self):
        for card in self.hand:
            print(card)




#TODO: GAME LOGIC
# Make 2 players,
# make one deck
# split the 52 Cards between the players


def game_logic():
    loser=""
    winner=""
    game_on=True
    p1=Player("Player 1")
    p2 = Player("Player 2")
    deck = Deck()
    print(len(deck.deck))
    i = 0
    prev = True
    # false -> p1
    # true->p2
    print("Shuffling the deck")
    while i < 52:  # splitting the cards
        if prev:
            p2.add_cards(deck.deck[i])
            prev = False
            i += 1
        else:
            p1.add_cards(deck.deck[i])
            prev = True
            i += 1
    print("Done shuffling the deck")
    round_num=0

    while game_on: #keeping the game on unless someone runs out of cards
        round_num+=1
        print(f"Round {round_num}")
        if len(p1.hand)==0: #if p1 runs out of cards
            loser=p1.name
            winner=p2.name
            game_on=False
            break
        if len(p2.hand)==0:   #if p2 runs out of cards
            loser=p2.name
            winner=p1.name
            game_on=False
            break

        p1_card=[] #current p1 cards
        p1_card.append(p1.remove_card(1))
        p2_card=[] #current p2 cards
        p2_card.append(p2.remove_card(1))

        at_war=True
        while at_war:
            if p1_card[-1].rank>p2_card[-1].rank:
                p1.add_cards(p1_card)
                p1.add_cards(p2_card)
                at_war=False

            elif p1_card[-1].rank<p2_card[-1].rank:
                p2.add_cards(p1_card)
                p2.add_cards(p2_card)
                at_war=False
            else:
                print("War")
                if len(p1.hand)<8:
                    print("Player 1 does not have enough cards")
                    loser=p1.name
                    winner=p2.name
                    game_on=False
                    break
                elif len(p2.hand)<8:
                    print("Player 2 does not have enough cards")
                    loser=p2.name
                    winner=p1.name
                    game_on=False
                    break
                else:
                    p1_card.extend(p1.remove_card(7))
                    p2_card.extend(p2.remove_card(7))
    print(f"Game over and {winner} won and {loser} lost")

game_logic()









