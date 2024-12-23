Menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee":24,
        },
        "cost": 3.0,
    }
}


Resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
turn_on_machine = True


def is_resources_sufficient(order_ingredients):
    """a function to check if resources is sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= Resources[item]:
            print(f"sorry there is enough {item}")
            return False
    return True


def process_coins():
    """a function to process coins"""
    print("Please insert coins")
    total = int(input("please insert quarters : ")) * 0.25
    total += int(input("please insert dimes : ")) * 0.10
    total += int(input("please insert nickels : ")) * 0.05
    total += int(input("please insert pennies : ")) * 0.01
    return total


def is_transaction_successful(order_cost,payment):
    if payment >= order_cost:
        change = payment - order_cost
        print(f"Here is ${change:.2f} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money, money refunded.")
        return False


def make_coffee(order_ingredient, drink):
    for item in order_ingredient:
        Resources[item] -= order_ingredient[item]
    print(f"Here is your {drink}, enjoy!")



while turn_on_machine:
    """Prompt user by asking """
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        turn_on_machine = False

    elif choice == "report":
        print(f"water: {Resources['water']}ml")
        print(f"milk: {Resources['milk']}ml")
        print(f"coffee: {Resources["coffee"]}g")
        print(f"profit : $ {profit}")
    else:
        drink = Menu.get(choice)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(drink["cost"],payment):
                profit += drink["cost"]
                make_coffee(drink["ingredients"], choice)


