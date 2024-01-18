class CoffeeOptions:
  def __init__(self, coffee_machine):
      self.coffee_machine = coffee_machine

  def make_espresso(self):
      result, ingredient = self.check_ingredients(250, 0, 16, 1)
      if result:
          self.coffee_machine.water -= 250
          self.coffee_machine.coffee_beans -= 16
          self.coffee_machine.cups -= 1
          self.coffee_machine.money += 4
          return "Espresso is ready!"
      else:
          return f"Sorry, not enough {ingredient} to make Espresso."

  def make_latte(self):
      result, ingredient = self.check_ingredients(350, 75, 20, 1)
      if result:
          self.coffee_machine.water -= 350
          self.coffee_machine.milk -= 75
          self.coffee_machine.coffee_beans -= 20
          self.coffee_machine.money += 7
          return "Latte is ready!"
      else:
          return f"Sorry, not enough {ingredient} to make Latte."

  def make_cappuccino(self):
      result, ingredient = self.check_ingredients(200, 100, 12, 1)
      if result:
          self.coffee_machine.water -= 200
          self.coffee_machine.milk -= 100
          self.coffee_machine.coffee_beans -= 12
          self.coffee_machine.cups -= 1
          self.coffee_machine.money += 6
          return "Cappuccino is ready!"
      else:
          return f"Sorry, not enough {ingredient} to make Cappuccino."

  def check_ingredients(self, required_water, required_milk, required_coffee_beans, required_cups):
      if self.coffee_machine.water < required_water:
          return False, "water"
      elif self.coffee_machine.milk < required_milk:
          return False, "milk"
      elif self.coffee_machine.coffee_beans < required_coffee_beans:
          return False, "coffee beans"
      elif self.coffee_machine.cups < required_cups:
          return False, "cups"
      else:
          return True, None
