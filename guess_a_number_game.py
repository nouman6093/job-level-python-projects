import random
import os

logo =  """
  _   _                 _                  _____                     _             
 | \ | |               | |                / ____|                   (_)            
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |
                                                                              __/ |
                                                                             |___/ 
"""

def compare(guess,attempts):
    if guess > 100:
        print("wrong! make a guess between 100 and 1")
        return attempts - 1
    elif guess < 1:
        print("wrong! make a guess between 100 and 1")
        return attempts - 1
    elif guess < ra:
        print("too low!")
        return attempts - 1
    elif guess > ra:
        print("too high!")
        return attempts - 1
    else:
        print(f"good guess! i was thinking of same {guess} number")

should_continue4 = True
while should_continue4:
    should_continue2 = input("do you want to play 'guess a number' game? type 'y' or 'n': ")
    if should_continue2 == "y":
        os.system('cls' if os.name == 'nt' else 'clear')    #this line clears the console screen
        print(logo)
        should_continue3 = True
        while should_continue3:
            print("Welcome to the number guessing game: ")
            ra = random.randint(1,101)
            print("im thinking of a number between 1 and 100")
            difficulty = input("choose a difficulty. type 'easy' or 'hard': ")
            if difficulty == "hard":
                attempts = 5
                should_continue = True
                while should_continue and attempts >= 1:
                    print(f"you have {attempts} attempts remaining to guess the number")
                    guess = int(input("make a guess: "))
                    attempts = compare(guess, attempts)
                    if attempts <= 0:
                        should_continue = False
                        should_continue3 = False
            elif difficulty == "easy":
                attempts = 10
                should_continue = True
                while should_continue and attempts >= 1:
                    print(f"you have {attempts} attempts remaining to guess the number")
                    guess = int(input("make a guess: "))
                    attempts = compare(guess, attempts)
                    if attempts <= 0:
                        should_continue = False
                        should_continue3 = False
    elif should_continue2 == "n":
        print("thanks for your interest hope to see you soon")
        should_continue4 = False
