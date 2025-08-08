from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

#create the objects
menu = Menu()
moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
items = menu.get_items()
# drink = menu.find_drink()

is_on = True

while is_on:
#prompt what the user would like
    choice = input(f"What would you like? {items} : ").lower()
    if choice == "off":
        break
    #prompt report
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        #check if resources is sufficient
        if coffeemaker.is_resource_sufficient(drink):
            #process coins
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)















#check if transaction is successful
