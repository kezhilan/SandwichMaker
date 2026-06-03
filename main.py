### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if ingredients[ingredient] > self.machine_resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}" )
                return False
        return True
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("please insert coins")
        dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        total = (dollars * 1.00) + (half_dollars * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return total
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry there is not enough money. Money Refunded")
            return False
        change =  coins - cost
        print(f"here is ${change:.2f} in change")
        return True
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient in order_ingredients:
            self.machine_resources[ingredient] -= order_ingredients[ingredient]
        print(f"{sandwich_size} sandwich is ready. Bon appetit")
    def report(self):
        """prints remaining resources"""
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} pound(s)")
### Make an instance of SandwichMachine class and write the rest of the codes ###
mac = SandwichMachine(resources)
display = True
while display:
    order = input("What would you like? (small/medium/large/off/report): ")
    order.lower()
    if order == "off":
        display = False
    elif order == "report":
        mac.report()
    elif order == "small":
        ingredients = recipes[order]["ingredients"]
        price = recipes[order]["cost"]
        if mac.check_resources(ingredients):
            payment = mac.process_coins()
            if mac.transaction_result(payment, price):
                mac.make_sandwich(order, ingredients)
    elif order == "medium":
        ingredients = recipes[order]["ingredients"]
        price = recipes[order]["cost"]
        if mac.check_resources(ingredients):
            payment = mac.process_coins()
            if mac.transaction_result(payment, price):
                mac.make_sandwich(order, ingredients)
    elif order == "large":
        ingredients = recipes[order]["ingredients"]
        price = recipes[order]["cost"]
        if mac.check_resources(ingredients):
            payment = mac.process_coins()
            if mac.transaction_result(payment, price):
                mac.make_sandwich(order, ingredients)
    else:
        print("Invalid selection")