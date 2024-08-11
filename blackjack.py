import random
from art import logo
from helper import validate_user_input, calculate_score, compare

cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
    print(logo)
    user_cards = random.choices(cards_deck, k=2)
    computer_cards = random.choices(cards_deck, k=2)
    computer_score = calculate_score(computer_cards)
    
    is_user_hit_over = False
    while not is_user_hit_over:
        user_score = calculate_score(user_cards)
        # if someone has blackjack, that is score = 0 (a possibility only during the first card dealing) 
        # or the user goes over 21 the game stops immediately
        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_game(user_cards, user_score, computer_cards, computer_score)
            return
        is_user_hit_over = user_hit(user_cards, user_score, computer_cards)

    while computer_score < 17:
        computer_cards.append(random.choice(cards_deck))
        computer_score = calculate_score(computer_cards)
        
    end_game(user_cards, user_score, computer_cards, computer_score)

def user_hit(u_cards, u_score, c_cards):
    """Returns true is the user hit is done, otherwise false.
    If the user scores 21 we stop the cards hit automatically (returns true), but the game goes on
    since there is always a possibility of a draw. A this point that we have more than 2 cards,
    so there is no blackjack scenario."""
    # the check for len(u_cards) > 2 is for keeping our code safe, but at the point this method is called
    # this check is always true
    if u_score == 21 and len(u_cards) > 2: return True
    print(f"Your cards: {u_cards}, current score: {u_score}")
    print(f"Computer's first card: {c_cards[0]}\n")
    get_another = validate_user_input(input("Do you want to get another card? Y/N\n"))
    if get_another == "n": return True
    u_cards.append(random.choice(cards_deck))
    return False

def end_game(u_cards, u_score, c_cards, c_score):
    """It prints the cards and scores of the user and the dealer (the computer), compares them
    and prints the outcome (win-lose-draw)"""
    print(f"Your final hand: {u_cards}, final score: {u_score if u_score !=0 else 21}")
    print(f"Computer's final hand: {c_cards}, computer final score: {c_score if c_score !=0 else 21}\n")
    print(compare(u_score, c_score))