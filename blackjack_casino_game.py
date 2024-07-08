import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

user_cards = []
computer_cards = []

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def adding_user_card(user_cards):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    ra = random.choice(cards)
    user_cards.append(ra)

def adding_computer_card(computer_cards):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    ra = random.choice(cards)
    computer_cards.append(ra)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over 21, You Lose!"
    elif computer_score > 21:
        return "Opponent went over 21, You Win!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"

input1 = input("do you wanna play blackjack casino game? type 'y' or 'n': ").lower()
if input1 == "y":
    print(logo)
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    adding_user_card(user_cards)
    adding_user_card(user_cards)
    print(f"cards selected for user: {user_cards} and current score is: {calculate_score(user_cards)}")
    adding_computer_card(computer_cards)
    adding_computer_card(computer_cards)
    print(f"first computer card is: {computer_cards[0]}")

    should_continue = True
    while should_continue:
        input2 = input("type 'y' to get another card, type 'n' to pass: ").lower()
        if input2 == "y":
            adding_user_card(user_cards)
            print(f"cards selected for user: {user_cards} and current score is: {calculate_score(user_cards)}")
            adding_computer_card(computer_cards)
            print(f"first computer card is: {computer_cards[0]}")
        elif input2 == "n":
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            result1 = compare(user_score, computer_score)
            print(f"your final hand is: {user_cards} and final score is: {calculate_score(user_cards)}")
            print(f"computer's final hand is: {computer_cards} and final score is: {calculate_score(computer_cards)}")
            print(result1)
            should_continue = False

elif input1 == "n":
    print("maybe next time")
