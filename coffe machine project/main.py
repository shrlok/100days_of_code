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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# emoji: ☕


def check_resources(drink):
    for ing in drink:
        if drink[ing] > resources[ing]:
            print(f"Sorry there is not enough {ing}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total_sum = 0
    total_sum += int(input("how many quarters?: ")) * 0.25
    total_sum += int(input("how many dimes?: ")) * 0.1
    total_sum += int(input("how many nickles?: ")) * 0.05
    total_sum += int(input("how many pennies?: ")) * 0.01
    return total_sum


def check_transaction(total_sum, drink_cost):
    if total_sum >= drink_cost:
        change = total_sum - drink_cost
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ing):
    for item in drink_ing:
        resources[item] -= drink_ing[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

turn_on = True

while turn_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        turn_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink_ing = MENU[choice]['ingredients']
        drink_cost = MENU[choice]['cost']
        if check_resources(drink_ing):
            pay = process_coins()
            if check_transaction(pay, drink_cost):
                make_coffee(choice, drink_ing)

