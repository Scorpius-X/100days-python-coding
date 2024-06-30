from Coffee_data import resources, MENU
#prompt should come up again after the whole process has ended


#check if the resources are sufficient?
def check_resources(coffee, resource):
    required_ingredients = MENU[coffee_choice]['ingredients']
    for ingredient, required_amount in required_ingredients.items():
        if resource.get(ingredient, 0) < required_amount:
            print(f"Sorry theres insufficient ingredients to make {coffee}")
            return False
    print(f"All resources are available to make {coffee}")
    return True

#process successful transaction
def check_cost(coffee):
    required_money = MENU[coffee_choice]["cost"]
    if money >= required_money:
        change = money - required_money
        formatted_change = "{:.2f}".format(change)
        print(f"Your change is : ${formatted_change}")
        print(f"Here is your {coffee_choice} ☕ Enjoy!")
        return True
    else:
        print("Sorry your money is not enough")
        print(f"Your {coffee_choice} cost ${required_money}")
        return False

#update resources
def update_resources(coffee, resource, profits):
    resources['money'] = profits
    required_ingredients = MENU[coffee]['ingredients']
    for ingredient, required_amount in required_ingredients.items():
        resource[ingredient] -= required_amount

#displays report
def display_report():
    for key, value in resources.items():
            print(f"{key}:{value}")

profit = 0
while True:
    #prompts to ask for coffee choice
    coffee_choice = input("What would you like?. (Espresso/Latte/Cappuccino): ").lower()
    #turnoff the coffee machine by entering 'off'
    if coffee_choice == "off":
        print("Thanks and Goodbye")
        break
    #prints report on resources
    elif coffee_choice == "report":
         display_report()

    elif coffee_choice  in MENU:
            if check_resources(coffee_choice, resources):
                print(f"Yes you can make {coffee_choice}")
                print("Please insert coins")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                money = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
                formatted_money = "{:.2f}".format(money)
                print(f"You inserted : ${formatted_money}")
                if check_cost(coffee_choice):
                    cost_of_coffee = MENU[coffee_choice]['cost']
                    profit += cost_of_coffee
                    update_resources(coffee_choice, resources, profit)
            else:
                print(f"You cannot make {coffee_choice} due to insufficient resources")



















