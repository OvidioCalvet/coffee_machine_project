MENU: dict = {

    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },

        "Cost": 1.5,

    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },

        "Cost": 2.5,

    },

    "cappuccino": {
        "ingredients": {
            "water":250,
            "milk":100,
            "coffee":24,
        },

        "cost": 3.0,

    }

}

resources: dict = {

    "water": 300,
    "milk": 200,
    "coffee": 100

}

order_is_not_over: bool = True

def are_resources_sufficient():
    return

def was_transaction_succesfull():
    return

def update_resources():
    return

def customer_response_evaluation():
    return

def make_coffee():
    return



while order_is_not_over:

    customer_response: str = input('What would you like? (espresso/latte/cappuccino):')



