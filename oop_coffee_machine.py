class Drink:
    def __init__(self, name, water, milk, coffee, price):
        self.name = name
        self.ingredients = {
            'Water': water,
            'Milk': milk,
            'Coffee': coffee
        }
        self.price = price
class CoffeeMachine:
    def __init__(self):
        self.resources = {
            'Water': 300,
            'Milk': 200,
            'Coffee': 100,
            'Money': 0
        }
        self.menu = {
            'espresso': Drink('espresso', 50, 0, 18, 1.5),
            'latte': Drink('latte', 200, 150, 24, 2.5),
            'cappuccino': Drink('cappuccino', 250, 100, 24, 3.5)
        }
    def report(self):
        print(f"Water: {self.resources['Water']}ml")
        print(f"Milk: {self.resources['Milk']}ml")
        print(f"Coffee: {self.resources['Coffee']}g")
        print(f"Money: ${self.resources['Money']}")
    def has_resources(self, drink):
        for item, amount in drink.ingredients.items():
            if self.resources[item] < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
    def process_payment(self, price):
        print(f"It costs ${price}. Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

        if total < price:
            print(f"Sorry that's not enough money. Money refunded ${total}.")
            return False
        else:
            change = round(total - price, 2)
            print(f"Here is ${change} dollars in change.")
            self.resources['Money'] += price
            return True
    def make_coffee(self, drink):
        for item, amount in drink.ingredients.items():
            self.resources[item] -= amount
        print(f"Here is your {drink.name}. Enjoy!")
    def run(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

            if choice == 'report':
                self.report()

            elif choice == 'off':
                break

            elif choice in self.menu:
                drink = self.menu[choice]

                if self.has_resources(drink) and self.process_payment(drink.price):
                    self.make_coffee(drink)

            else:
                print("Invalid choice")
machine = CoffeeMachine()
machine.run()
