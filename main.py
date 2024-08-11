from os import system
import signal
from helper import validate_user_input
from blackjack import play_game

def handler(signum, frame):
    system("cls")
    exit(1)

signal.signal(signal.SIGINT, handler)

############### Our Blackjack Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the deck have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def start_game():    
    if "n" == validate_user_input(input("Do you want to play a Blackjack game?Y/N\n").lower()): 
        return
    play = True
    while play:
        system("cls")
        play_game()
        play = ("y" == validate_user_input(input("Do you want to play another Blackjack game?Y/N\n").lower()))
    system("cls")            
start_game()
