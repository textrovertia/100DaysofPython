MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,

        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0

}


order = str(input("What would you like? (espresso/latte/cappuccino): "))

if order == "report":

    print(
        "Water:", resources["water"], "\n"
        "Milk:", resources["milk"], "\n"
        "Coffee:", resources["coffee"], "\n"
        "Money:", resources["money"]
    )

elif order == "latte" or "espresso" or "cappuccino":

    if MENU[order]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")

    elif MENU[order]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk")

    elif MENU[order]["ingredients"]["coffee"] > resources["coffee"]:
        print('Sorry there is not enough coffee')
        suf = "no"
    else:
        print("Please insert coins")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickels?"))
        pennies = int(input("How many pennies?"))

        total = 0.25*quarters+0.1*dimes+0.05*nickels + 0.01*pennies
        if total < MENU[order]["cost"]:
            "Sorry that is not enough money. Money refunded. "
        else:
            resources["money"] += MENU[order]["cost"]
            print(resources["money"])
            if total > MENU[order]["cost"]:
                print("Here is $", round(total-MENU[order]["cost"], 2), " in change")
            resources["water"] -= MENU[order]["ingredients"]["water"]
            resources["milk"] -= MENU[order]["ingredients"]["milk"]
            resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
            print("Here is your " + order + "! Enjoy!")
            print(resources["money"])
            print(resources["water"])
            print(resources["milk"])
            print(resources["milk"])
