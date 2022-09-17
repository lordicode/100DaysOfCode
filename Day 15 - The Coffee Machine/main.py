import time
from tqdm import tqdm

coffee_machine_ascii = """        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~"""

espresso_ascii = """  .-=-.
 ,|`~'|
 `|   |  
   `~'"""


latte_ascii = """  .=%%=.
,|`=%%='|
||      |
`|      |  
  `-__-'"""

capuchinno_ascii = """     )))
    (((
  +-----+
  |     |]
  `-----' """

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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0,
}

def get_change(how_much_inserted, cost_of_drink):
    if how_much_inserted == cost_of_drink:
        change_a = 0
        return change_a
    else:
        change_a = float(how_much_inserted) - float(cost_of_drink)
        quarters, change_a = divmod(change_a, 0.25)
        dimes, change_a = divmod(change_a, 0.10)
        nickels, change_a = divmod(change_a, 0.05)
        pennies = round(change_a / 0.01, 0)
        coins_to_dispense = list(map(int, [quarters, dimes, nickels, pennies]))
        line_show_change = "{} quarters, {} dimes, {} nickels, {} pennies".format(
            quarters, dimes, nickels, pennies)
        return change_a, line_show_change

def pay_coins(usd_for_drink):
    global change_p
    global summ_of_coins
    summ_of_coins = 0
    print("You have quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent)\nWhich coins and how much would you like to enter into the machine?")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    while summ_of_coins < usd_for_drink:
        summ_of_coins = 0
        summ_of_coins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        print(f"You inserted {summ_of_coins}$ into the machine.")
        change_p, show_change = get_change(summ_of_coins, usd_for_drink)
        if summ_of_coins < usd_for_drink:
            print("This is not enough for the drink. Please collect the coins from the dispenser at the bottom.")
            again = input("Do you want to get more coins and try again? Y/N")
            if again.strip().lower() == "y":
                pay_coins(usd_for_drink)
            else:
                return

    return 1, change_p, show_change

def bar():
    for i in tqdm(range(100), desc="Preparing..."):
        time.sleep(0.05)
        pass

def espresso():
    inner_dict = MENU["espresso"]
    cost = inner_dict["cost"]
    print(f"Espresso costs {cost}$")
    state, change, change_coins = pay_coins(cost)
    if state == 1:
        print("Your espresso is being prepared!")
        bar()
        print(espresso_ascii)
        print("Your espresso is ready!")
        resources["water"] -= 50
        resources["coffee"] -= 25
        resources["money"] += cost
        print(f"Your change is {change_coins}")


def latte():
    inner_dict = MENU["latte"]
    cost = inner_dict["cost"]
    print(f"Latte costs {cost}$")
    state, change, change_coins = pay_coins(cost)
    if state == 1:
        print("Your latte is being prepared!")
        bar()
        print(latte_ascii)
        print("Your latte is ready!")
        resources["water"] -= 150
        resources["coffee"] -= 50
        resources["milk"] -= 150
        resources["money"] += cost
        print(f"Your change is {change_coins}")


def cappuccino():
    inner_dict = MENU["cappuccino"]
    cost = inner_dict["cost"]
    print(f"Cappuccino costs {cost}$")
    state, change, change_coins = pay_coins(cost)
    if state == 1:
        print("Your cappuccino is being prepared!")
        bar()
        print(capuchinno_ascii)
        print("Your cappuccino is ready!")
        resources["water"] -= 200
        resources["coffee"] -= 50
        resources["milk"] -= 100
        resources["money"] += cost
        print(f"Your change is {change_coins}")


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money_usd = resources["money"]
    print(f"\nThis machine currently has {water} ml of water in stock, {milk} ml of milk, and {coffee} grams of coffee\nIt holds {money_usd}$")
    print(coffee_machine_ascii)

cancel = False
print("Hello! You are standing in front of a coffee machine. It has 3 buttons for drinks. 1 button to display how much coffee, milk, and water it has in stock.\nWhat do you want to press?")
while cancel is False:
    button_pressed = int(input("0 for espresso, 1 for latte, 2 for cappuccino. Press 3 if you want to check how much in stock the machine has. 9 to cancel."))

    if button_pressed == 0:
        if resources["water"] < 50:
            print("You cannot order this drink. Not enough water.")
        else:
            espresso()
    elif button_pressed == 1:
        if resources["water"] < 150 or resources["milk"] < 150:
            print("You cannot order this drink. Not enough water or milk.")
        else:
            latte()
    elif button_pressed == 2:
        if resources["water"] < 200 or resources["milk"] < 100:
            print("You cannot order this drink. Not enough water.")
        else:
            cappuccino()
    elif button_pressed == 3:
        report()
    elif button_pressed == 9:
        cancel = True
    else:
        print("Oops, missed that button over there!")

report()
