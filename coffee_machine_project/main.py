import time

MENU: dict = {

    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },

        "cost": 1.50,

    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },

        "cost": 2.50,

    },

    "cappuccino": {
        "ingredients": {
            "water":250,
            "milk":100,
            "coffee":24,
        },

        "cost": 3.00,

    }

}

resources: dict = {

    "water": 1000,
    "milk": 1000,
    "coffee": 500

}

order_is_not_over: bool = True

def resources_are_sufficient(coffee):
    """Output function returning a boolean value in response to resources available and the what is needed to make the coffee """

    if coffee == 'espresso':

        water_needed: int = MENU[coffee]['ingredients']['water']
        coffee_needed: int = MENU[coffee]['ingredients']['coffee']

        water_left: int = resources['water']
        coffee_left: int = resources['coffee']

        if water_needed <= water_left and coffee_needed <= coffee_left: return True

        else: return False

    else:

        water_needed: int  = MENU[coffee]['ingredients']['water']
        milk_needed: int = MENU[coffee]['ingredients']['milk']
        coffee_needed: int = MENU[coffee]['ingredients']['water']

        water_left: int = resources['water']
        milk_left: int = resources['milk']
        coffee_left: int = resources['coffee']

        if water_needed <= water_left and milk_needed <= milk_left and coffee_needed <= coffee_left: return True

        else: return False

def transaction_was_succesfull():
    """Output fucntion returning a boolean value based on amount of money given """

    cost: float = MENU[customer_response]['cost']

    customer_payment: float = 0.0

    customer_payment = float(input(f'Your total is ${cost}, insert payment amount in dollars and cents please: '))

    if customer_payment == cost: 
        
        print('Thank you! We are making your order right now...')

        return True

    elif customer_payment > cost: 
            
        change: float = 0

        change = customer_payment - cost

        print(f'Thank you! Your change is ${change}. We are making your order right now...')

        return True

    else: 
        
        print('Insufficient funds.')

        return False

def update_resources(response):
    """Input function changing the values assigned in the resources dictionary based on a customers order """

    if response == 'espresso':

        water_left: int = resources['water']
        coffee_left: int = resources['coffee']

        water_needed: int  = MENU[response]['ingredients']['water']
        coffee_needed: int = MENU[response]['ingredients']['water']

        water_left = water_left - water_needed
        coffee_left = coffee_left - coffee_needed

        resources['water'] = water_left
        resources['coffee'] = coffee_left

    elif response == 'latte' or response == 'cappuccino': 

        water_left: int = resources['water']
        milk_left: int = resources['milk']
        coffee_left: int = resources['coffee']        

        water_needed: int  = MENU[response]['ingredients']['water']
        milk_needed: int = MENU[response]['ingredients']['milk']
        coffee_needed: int = MENU[response]['ingredients']['water']

        water_left = water_left - water_needed
        milk_left = milk_left - milk_needed
        coffee_left = coffee_left - coffee_needed

        resources['water'] = water_left
        resources['milk'] = milk_left
        resources['coffee'] = coffee_left

    else:

        water_left: int = resources['water']
        milk_left: int = resources['milk']
        coffee_left: int = resources['coffee']

        water_left = water_left + 500
        milk_left = milk_left + 500
        coffee_left = coffee_left + 500

        resources['water'] = water_left
        resources['milk'] = milk_left
        resources['coffee'] = coffee_left

def customer_response_evaluation(response):
    """This is an output function running the logic behind the customers response returning a value' """

    if response == 'espresso' or response == 'latte' or response == 'cappuccino': 

        if resources_are_sufficient(response): return 'good to go'

        else: return 'not enugh resources'

    elif response == 'off': return response

    elif response == 'report': return response

    elif response == 'restock': return response

def make_coffee(coffee):
    """This is an input fucntion printing the customers order and updating the stores resources """
    update_resources(coffee)

    print('making the coffee..\n')
    time.sleep(1)
    print('pouring the milk..\n')
    time.sleep(1)
    print('preparing your beverage..\n')
    time.sleep(1)

    print(f'Here is your {coffee}! Enjoy!')



while order_is_not_over:

    print('\n')

    customer_response: str = input('What would you like? (espresso/latte/cappuccino): ')

    if customer_response_evaluation(customer_response) == 'good to go':

        if transaction_was_succesfull(): make_coffee(customer_response)

        else: order_is_not_over = False

    elif customer_response_evaluation(customer_response) == 'not enugh resources': 
        
        print('Were out of stock sorry :/')

        order_is_not_over = False

    elif customer_response_evaluation(customer_response) == 'off': 
        
        order_is_not_over = False

    elif customer_response_evaluation(customer_response) == 'report':

        print(resources)

    elif customer_response_evaluation(customer_response) == 'restock':

        update_resources(customer_response)

    direction: str = input('Would you like anything else? : ')

    if direction == 'Yes' or direction == 'yes': order_is_not_over = True

    else: order_is_not_over = False






