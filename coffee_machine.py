total_resources={
'Water': 300 ,
'Milk': 200 ,
'Coffee': 100,
'Money': 0
}
espresso={
'Water': 50 ,
'Milk': 0 ,
'Coffee': 18,
'Money': 1.5
}
latte={
'Water': 200 ,
'Milk': 150 ,
'Coffee': 24,
'Money': 2.5
}
cappuccino={
'Water': 250 , 
'Milk': 100 ,
'Coffee': 24,
'Money': 3.5
}
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'report':
        print(f"Water: {total_resources['Water']}ml")
        print(f"Milk: {total_resources['Milk']}ml")
        print(f"Coffee: {total_resources['Coffee']}g")
        print(f"Money: ${total_resources['Money']}")
    elif choice == 'off':
        break
    elif choice in ['espresso', 'latte', 'cappuccino']:
        drink = locals()[choice]  
        sufficient = True
        for key in drink:
            if key != 'Money' and total_resources[key] < drink[key]:
                print(f"Sorry there is not enough {key}.")
                sufficient = False
                break
        if sufficient:
            print(f"It costs ${drink['Money']}. Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if total < drink['Money']:
                print(f"Sorry that's not enough money. Money refunded ${total}.")
            else:
                change = round(total - drink['Money'], 2)
                total_resources['Money'] += drink['Money']
                print(f"Here is ${change} dollars in change.")
                for key in drink:
                    if key != 'Money':
                        total_resources[key] -= drink[key]
                print(f"Here is your {choice}. Enjoy!")
    else:
        print("Invalid choice")
