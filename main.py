import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def order_calc(order):
    """Makes sandwich maker and cashier based on user input"""
    ingredients = recipes[order]["ingredients"]
    price = recipes[order]["cost"]
    if sandwich_maker_instance.check_resources(ingredients):
        payment = cashier_instance.process_coins()
        if cashier_instance.transaction_result(payment, price):
            sandwich_maker_instance.make_sandwich(order, ingredients)


def main():
    display = True
    while display:
        order = input("What would you like? (small/ medium/ large/ off/ report): ")
        order.lower()
        if order == "off":
            display = False
        elif order == "report":
            sandwich_maker_instance.report()
        elif order == "small":
            order_calc(order)
        elif order == "medium":
            order_calc(order)
        elif order == "large":
            order_calc(order)
        else:
            print("Invalid selection")

if __name__=="__main__":
    main()
