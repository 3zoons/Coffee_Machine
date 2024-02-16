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

is_on = True

def is_resources_sufficient(order_ingredients) :
    """ Return True if there are sufficient resources to make coffee, otherwise returns False. """
    for ingredient in order_ingredients : 
        if order_ingredients[ingredient] > resources[ingredient] :
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def process_coins() : 
    """ Returns the total money inserted into the coffee machine. """
    print("Please insert the coins")
    total = int(input("How many quaters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many penny?: ")) * 0.01
    return total

def is_transaction_successfull(money_received, drink_cost) :
    """ Returns True when the payment is accepted, or False if money is insuffecient. """
    if money_received >= drink_cost : 
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else : 
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients) :
    for ingredient in order_ingredients : 
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name}")

while is_on : 
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off" : 
        is_on = False
    elif choice == "report" :
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else : 
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]) : 
            money_inserted = process_coins()
            if is_transaction_successfull(money_inserted, drink["cost"]) :
                make_coffee(choice, drink["ingredients"])
                 