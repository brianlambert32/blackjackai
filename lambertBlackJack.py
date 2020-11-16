import random
import numpy as np
#deck of cards

suits = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
ranks = ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace')
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
good_cards = ['10','Jack','Queen','King','Ace']
playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card



class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 1000
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet



def make_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much would you like to bet?  '))
        except ValueError:
            print("Must enter a number")
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed {} '.format(chips.total))
            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()




def hit_or_stand(deck,hand):
    global playing
    while True:
        answer = input("Tree Based AI or Baseline? T or B:")
        if answer == "T":
            if player_hand.value < 10:
                hit(deck,hand)  
        
            elif dealer_hand.value > player_hand.value:
                hit(deck,hand)
            elif dealer_hand.value == good_cards and player_hand.value < 17:
                    hit(deck,hand)
    
            else:
                print("Player stands. Dealer is playing.")
                playing = False
                break

        elif answer == "B":
            if player_hand.value < dealer_hand.value:
                hit(deck,hand)
            elif player_hand.value >= dealer_hand.value:
                print("Player stands. Dealer is playing.")
                playing = False
                break

def hit_or_standB(deck,hand):
    global playing
    while True:
        answer = input("Tree Based AI or Baseline? T or B:")
        if answer == "T":
            if player_hand.value <= 18:
                hit(deck,hand)
            
            elif dealer_hand.value > player_hand.value:
                hit(deck,hand)
            elif dealer_hand.value == good_cards and player_hand.value < 19:
                hit(deck,hand)
            
            else:
                print("Player stands. Dealer is playing.")
                playing = False
                break
    
        elif answer == "B":
            if player_hand.value < dealer_hand.value:
                hit(deck,hand)
            elif player_hand.value >= dealer_hand.value:
                print("Player stands. Dealer is playing.")
                playing = False
                break



def show_partial(player,dealer):
    print("\nDealer's Hand")
    print("<card unknown>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')

    input("Press <enter> to proceed")

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)




def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    # Start
    print("Welcome to Blackjack!")
    answer = input("Adjust Bust to 25? y or n:")
    if answer == "n":
    
        deck = Deck()
        deck.shuffle()
    
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
    
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    

        player_chips = Chips()
    
    
        make_bet(player_chips)
    
    
        show_partial(player_hand, dealer_hand)
    
        while playing:
        

            hit_or_stand(deck, player_hand)

            show_partial(player_hand,dealer_hand)
        
  
            if player_hand.value >21:
                player_busts(player_hand, dealer_hand, player_chips)
            
                break


        if player_hand.value <= 21:
    
            while dealer_hand.value <17:
                hit(deck, dealer_hand)
        

            show_all(player_hand,dealer_hand)
        
        #win or lose?
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
        
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
        
            else:
                push(player_hand,dealer_hand)
                    #bust = 25
    elif answer == "y":
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        
   
        player_chips = Chips()
        
   
        make_bet(player_chips)
        
    
        show_partial(player_hand, dealer_hand)
        
        while playing:
            

            hit_or_standB(deck, player_hand)
            
          
            show_partial(player_hand,dealer_hand)
            
       
            if player_hand.value >25:
                player_busts(player_hand, dealer_hand, player_chips)
                
                break


        if player_hand.value <= 25:
    
            while dealer_hand.value <17:
                hit(deck, dealer_hand)
            

            show_all(player_hand,dealer_hand)
            

            if dealer_hand.value > 25:
                dealer_busts(player_hand,dealer_hand,player_chips)
            
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            
            else:
                push(player_hand,dealer_hand)



    print("\nPlayers winnings stand at", player_chips.total)

    new_game = input("would you like to play again? Enter 'y' or 'n'")
    if new_game[0].lower() == 'y':
        playing = True
        player_chips.total
        continue
    else:
        print('Come back soon! ')
        
        break







