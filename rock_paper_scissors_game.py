import random

print("Rock, Paper and Scissor Game")

print("What do you choose?")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

if user == 0:
    print("You Choose: ")
    print(rock)
    pc = random.randint(0,2)
    if pc == 0:
        print("Computer Choose: ")
        print(rock)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
    elif pc == 1:
        print("Computer Choose: ")
        print(paper)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
    else:
        print("Computer Choose: ")
        print(scissors)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
elif user == 1:
    print("You Choose: ")
    print(paper)
    pc = random.randint(0,2)
    if pc == 0:
        print("Computer Choose: ")
        print(rock)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
    elif pc == 1:
        print("Computer Choose: ")
        print(paper)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
    else:
        print("Computer Choose: ")
        print(scissors)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
elif user == 2:
    print("You Choose: ")
    print(scissors)
    pc = random.randint(0,2)
    if pc == 0:
        print("Computer Choose: ")
        print(rock)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
    elif pc == 1:
        print("Computer Choose: ")
        print(paper)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
    else:
        print("Computer Choose: ")
        print(scissors)
        if user == pc:
            print("It's a Tie!")
        elif user == 0 and pc == 1:
            print("You Loose!")
        elif user == 1 and pc == 0:
            print("You Win!")
        elif user == 1 and pc == 2:
            print("You Loose!")
        elif user == 2 and pc == 1:
            print("You Win!")
        elif user == 0 and pc == 2:
            print("You Win!")
        elif user == 2 and pc == 0:
            print("You Loose!")
else:
    print("Please Enter an Integer Between 0 - 2")
