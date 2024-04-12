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

profit = 0
machine_on = True


def process_coin():
    """Returns total calculated from coins inserted.."""
    print("Please Insert coins🪙....")
    total = int(input("How many quarter:")) * 0.25
    total += int(input("How many dime:")) * 0.10
    total += int(input("How many nickle:")) * 0.05
    total += int(input("How many pennies:")) * 0.01
    return total


def check_resource(other_ingredient):
    """return True or false based on the resources sufficiency"""
    for key in other_ingredient:
        if other_ingredient[key] >= resources[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money.Money refunded.")


def display_resource():
    for key in resources:
        print(f"{key} : {resources[key]}")


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources."""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
        print(f"Here is your {drink_name}☕")


while machine_on:
    user_choice = input("What would you like? (expresso/latte/cappuccino):").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        display_resource()
        print(f"Money : ${profit}")
    else:
        u_define = MENU[user_choice]
        if check_resource(u_define["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, u_define["cost"]):
                make_coffee(user_choice, u_define["ingredients"])
