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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 3. create a function to pirnt a
def resources_report():
    """Print a report of the coffe machine resources."""
    water = "water"
    milk = "milk"
    coffee = "coffee"
    return f"Water: {resources[water]}ml \n Milk: {resources[milk]}ml \n Coffe: {resources[coffee]}g \n Money: ${money}"


# TODO: 4 Check resources sufficient to make drinks order.
def is_resources_sufficient(ingredients_drink):
    """Takes an order ingredients and return if the there is sufficient resources to prepare the order"""
    for item in ingredients_drink:
        if ingredients_drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


#TODO: 5. Process the inserted coins and return the total amount
def process_coins():
    """Rertun the total amonunt of the proccesed coins"""
    print("Please insert coins.")
    total = 0
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many quarters?: ")) * 0.01
    return total


#TODO: 6. process the payment and validate if the transaccion is sucessful
def is_transaction_successful(processed_payment, drink_price):
    """Takes the inserted payment amount and the price of the desired drink and compare if the transaction is
    successful or not"""
    if processed_payment >= drink_price:
        global money
        money += drink_price
        change = round(processed_payment - drink_price, 2)
        print(f"here is {change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


#TODO: 7. Make coffe reducing the resources after order processes
def make_coffee(order_ingredients, drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO: 2. Check the coffe machine status (on/off)
is_on = True
while is_on:
    # TODO: 1. prompt user asking " What would you like?
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(resources_report())
    else:
        drink = MENU[user_choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink["ingredients"], user_choice)

