MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

money_register = 0

def report_resource(water, milk, coffee, money):
    return f"Água: {water}ml\nLeite: {milk}ml\nCafé: {coffee}g\nDinheiro: ${money}"

def check_resource(water, milk, coffee):
    if MENU[order]["ingredients"]["water"] <= water and MENU[order]["ingredients"]["milk"] <= milk and MENU[order]["ingredients"]["coffee"] <= coffee:
        return True
    else:
        if MENU[order]["ingredients"]["water"] > water:
            print(f"Desculpe, hão há água suficiente.")
        elif MENU[order]["ingredients"]["milk"] > milk:
            print(f"Desculpe, hão há leite suficiente.")
        elif MENU[order]["ingredients"]["coffee"] > coffee:
            print(f"Desculpe, hão há café suficiente.")

def subtract_resource(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

on = True
while on:
    order = input(" Do que você gostaria? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(report_resource(resources["water"], resources["milk"], resources["coffee"], money_register))
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if check_resource(resources["water"], resources["milk"], resources["coffee"]):
            print("Por favor insira as moedas.")
            quarter = int(input("quantas moedas de $0.25?: "))
            dime = int(input("quantas moedas de $0.10?: "))
            nickel = int(input("quantas moedas de $0.05?: "))
            penny = int(input("quantas moedas de $0.01?: "))
            money = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
            if money < MENU[order]["cost"]:
                print("Desculpe, o dinheiro não é suficiente. Dinheiro reembolsado.")
            else:
                change = money - MENU[order]["cost"]
                print(f"Aqui está ${change:.2f} em troco.")
                print(f"Aqui está o seu {order} ☕ Aproveite!")
                money_register += MENU[order]["cost"]
                subtract_resource(MENU[order]["ingredients"]["water"], MENU[order]["ingredients"]["milk"], MENU[order]["ingredients"]["coffee"])

    elif order == "off":
        on = False


