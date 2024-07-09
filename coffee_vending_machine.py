MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0
should_continue = True
while should_continue:
    input1 = input("what would you like? (espresso/latte/cappuccino): ")
    if input1 == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: ${money}")
    elif input1 == "latte":
        if resources['water'] >= MENU['latte']['ingredients']['water'] and resources['milk'] >= MENU['latte']['ingredients']['milk'] and resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
            print("please insert coins")
            quarters = float(input("how many quarters: $"))
            dimes = float(input("how many dimes: $"))
            nickles = float(input("how many nickles: $"))
            pennies = float(input("how many pennies: $"))
            money1 = 0
            money1 = quarters + dimes + nickles + pennies
            if money1 == MENU['latte']['cost']:
                money = money + money1
                resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
                print("enjoy! heres your latte: ☕")
                should_continue = False
            elif money1 > MENU['latte']['cost']:
                money = money + money1
                change = money1 - 2.5
                resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
                print("enjoy! heres your latte: ☕")
                print(f"heres your change: ${change}")
                should_continue = False
            else:
                refund = money1
                print(f"sorry, money not enough. here is your refund: ${refund}")
                should_continue = False
        elif resources['water'] < MENU['latte']['ingredients']['water'] and resources['milk'] >= MENU['latte']['ingredients']['milk'] and resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
            print("sorry, we dont have enough water")
            should_continue = False
        elif resources['water'] >= MENU['latte']['ingredients']['water'] and resources['milk'] < MENU['latte']['ingredients']['milk'] and resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
            print("sorry, not enough milk")
            should_continue = False
        elif resources['water'] >= MENU['latte']['ingredients']['water'] and resources['milk'] >= MENU['latte']['ingredients']['milk'] and resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("sorry, not enough coffee")
            should_continue = False
    elif input1 == "espresso":
        if resources['water'] >= MENU['espresso']['ingredients']['water'] and resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
            print("please insert coins")
            quarters = float(input("how many quarters: $"))
            dimes = float(input("how many dimes: $"))
            nickles = float(input("how many nickles: $"))
            pennies = float(input("how many pennies: $"))
            money1 = 0
            money1 = quarters + dimes + nickles + pennies
            if money1 == MENU['espresso']['cost']:
                money = money + money1
                resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
                print("enjoy! heres your espresso: ☕")
                should_continue = False
            elif money1 >= MENU['espresso']['cost']:
                money = money + money1
                change = money1 - 1.5
                resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
                print("enjoy! heres your espresso: ☕")
                print(f"heres your change: ${change}")
                should_continue = False
            else:
                refund = money1
                print(f"sorry, money not enough. here is your refund: ${refund}")
                should_continue = False
        elif resources['water'] < MENU['espresso']['ingredients']['water'] and resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
            print("sorry, we dont have enough water")
            should_continue = False
        elif resources['water'] >= MENU['espresso']['ingredients']['water'] and resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("sorry, not enough coffee")
            should_continue = False
    elif input1 == "cappuccino":
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
            print("please insert coins")
            quarters = float(input("how many quarters: $"))
            dimes = float(input("how many dimes: $"))
            nickles = float(input("how many nickles: $"))
            pennies = float(input("how many pennies: $"))
            money1 = 0
            money1 = quarters + dimes + nickles + pennies
            if money1 == MENU['cappuccino']['cost']:
                money = money + money1
                resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
                print("enjoy! heres your cappuccino: ☕")
                should_continue = False
            elif money1 > MENU['cappuccino']['cost']:
                money = money + money1
                change = money1 - 2.5
                resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
                print("enjoy! heres your cappuccino: ☕")
                print(f"heres your change: ${change}")
                should_continue = False
            else:
                refund = money1
                print(f"sorry, money not enough. here is your refund: ${refund}")
                should_continue = False
        elif resources['water'] < MENU['cappuccino']['ingredients']['water'] and resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
            print("sorry, we dont have enough water")
            should_continue = False
        elif resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['milk'] < MENU['cappuccino']['ingredients']['milk'] and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
            print("sorry, not enough milk")
            should_continue = False
        elif resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] and resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("sorry, not enough coffee")
            should_continue = False
    elif input1 == "resources":
        print(f"water: {resources['water']}")
        print(f"water: {resources['milk']}")
        print(f"water: {resources['coffee']}")
    else:
        print("invalid input")
