class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if ingredients[ingredient] > self.machine_resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient in order_ingredients:
            self.machine_resources[ingredient] -= order_ingredients[ingredient]
        print(f"{sandwich_size} sandwich is ready. Bon appetit")

    def report(self):
        """prints remaining resources"""
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} pound(s)")