from coffee_machine import CoffeeMachine
from coffee_options import CoffeeOptions
from service import turn_off, service

coffee_machine = CoffeeMachine()
coffee_options = CoffeeOptions(coffee_machine)

# Service
service(coffee_machine)

# Make the chosen drink

message = coffee_options.make_latte()

# Print the updated report after making the latte
updated_report = coffee_machine.print_report()

print("Initial Report:")
print(initial_report)
print("\nUpdated Report:")
print(updated_report)
