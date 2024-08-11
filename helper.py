def validate_user_input(user_input):
    while user_input not in ["y", "n"]:
        user_input = input("Wrong input. Try again.\n").lower()
    return user_input

def calculate_score(cards):
    """Returns the sum of the cards list values taken as parameter. If we have a blackjack it returns 0."""
    cards_score = sum(cards)
    if cards_score == 21 and len(cards) == 2:
        return 0
    if cards_score > 21 and 11 in cards:
        ace_index = cards.index(11)
        cards[ace_index] = 1
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

