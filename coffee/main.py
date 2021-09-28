from typing import ChainMap, Counter


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

profit=0
coffee_on=True

def is_res_suf(order_ing):
    for item in order_ing:
        if order_ing[item]>=resources[item]:
            print(f"Sorry there is not enoug {item}.")
            return False
    return True

def coins():
    """Returns total value from coins inserted."""
    print("Please Insert Coins.")
    total= int(input("How many quarters?:")) *0.25
    total+= int(input("How many dimes?:")) *0.1
    total+= int(input("How many nickles?:")) *0.05
    total+= int(input("How many pennies?:")) *0.01
    return total

def tran_suc(money_rec,drink_cost):
    if money_rec>=drink_cost:
        change=round(money_rec-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough. Money refunded.")
        return False    

def make_coffee(drink_name,order_ing):
    for item in order_ing:
        resources[item]-=order_ing[item]
    print(f"Here is your {drink_name}")

while coffee_on:
    choice=input("What would you like?(espresso/latte/cappuccino): ")
    if choice =="off":
        coffee_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_res_suf(drink['ingredients']):
            payment= coins()
            if tran_suc(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

