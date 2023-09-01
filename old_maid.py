# A card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     while len(deck)>1:
         other.append(deck.pop())
         dealer.append(deck.pop())

     if len(dealer)>=len(other) and len(deck)==1:
         other.append(deck.pop())
     elif len(dealer)<len(other) and len(deck)==1:
         dealer.append(deck.pop())

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    
    no_suits=[]

    for i in range(len(l)):
        num = l[i][:-1]
        no_suits.append(num)

    for j in range(len(no_suits)):
        if no_suits.count(no_suits[j])%2==1 and j==no_suits.index(no_suits[j]):
            no_pairs.append(l[j])
    
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    print()
    for card in deck:
        print(card, end=' ')
    print("\n")

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     print(f"I have {n} cards. If 1 stands for my first card and")
     print(f"{n} for my last card, which of my cards would you like?")
     user_input=int(input(f"Give me an integer between 1 and {n}: "))
     while user_input>n or user_input<1:
         user_input=int(input(f"Invalid number. Please enter integer between 1 and {n}: "))
     return user_input


def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)
     next_turn = 'player'

     while (len(human)>0 and len(dealer)>0):
         if next_turn=='player':
             print()
             print('Your turn.')
             print()
             print('Your current deck of cards is: ')
             print_deck(human)
             card_choice = get_valid_input(len(dealer))
             card = dealer[card_choice-1]
             dealer.remove(card)

             print(f'You asked for my {card_choice} card.')
             print(f'Here it is. It is {card}.')
             human.append(card)
             print()
             print(f'With {card} added, your current deck of cards is: ')
             print_deck(human)
             human = remove_pairs(human)
             print('And after discarding pairs and shuffling, your deck is: ')
             print_deck(human)
             next_turn = 'robot'
             wait_for_player()

         else:
             print()
             print('My turn.')
             print()
             card_choice = random.randrange(0,len(human))
             card = human[card_choice]
             human.remove(card)
             dealer.append(card)
             dealer = remove_pairs(dealer)
             print(f'I took your {card_choice+1} card.')
             next_turn = 'player'
             wait_for_player()
             
     if len(human)==0:
         print()
         print("You don't have any more cards.")
         print('Congratulations! You win!')
     elif len(dealer)==0:
         print()
         print("I don't have any more cards.")
         print('You lost! I win!')
	 

# main
play_game()
