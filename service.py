def turn_off():
  print("Turning off the machine...")
  print("Machine turned off. Type 'on' to turn it back on.")
coffee_options = CoffeeOptions(coffee_machine)

# Service
def service(coffee_machine):
  while True:
      choice = input("Hey, what would you like to have? (espresso/latte/cappuccino/off/report) ")

      actions = {
          "espresso": coffee_options.make_espresso,
          "latte": coffee_options.make_latte,
          "cappuccino": coffee_options.make_cappuccino,
          "off": turn_off,
          "report": coffee_machine.print_report,  
      }

      if choice in actions:
          if choice == "off":
              actions[choice]()
              break  
          else:
              result = actions[choice]()
              print(result)  
              global initial_report
              initial_report = coffee_machine.print_report()
              global updated_report
              updated_report = coffee_machine.print_report()
      else:
          print("Invalid choice. Please enter a valid option.")
