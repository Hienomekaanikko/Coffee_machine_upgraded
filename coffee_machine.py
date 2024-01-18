class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def print_report(self):
        return f"Water: {self.water}ml, Milk: {self.milk}ml, Coffee Beans: {self.coffee_beans}g, Cups: {self.cups}, Money: ${self.money}"
