MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3
    }
}

TOTAL_CAPACITY = {"milk": 300,
                  "coffee": 100,
                  "water": 500}


cups_sold = 0

def is_capable_to_make_coffee():
    for coffee, details in MENU.items():
        for item, required in details["ingredients"].items():
            if TOTAL_CAPACITY[item] < required:
                print(f"Not capable to make your {coffee} because {item} is insufficient.")
                return False
    return True


def is_ingredients_sufficient(coffe_choice):
    for item, required in MENU[coffe_choice]["ingredients"].items():
        if TOTAL_CAPACITY[item] < required:
            print(f"Not enough {item}")
            return False
    return True

def make_coffee(coffee_choice):
    global cups_sold
    for item, required in MENU[coffee_choice]["ingredients"].items():
        TOTAL_CAPACITY[item] -= required
    cups_sold += 1
    print(f"Your coffee {coffee_choice}")

def generate_report():
    for item, amount in TOTAL_CAPACITY.items():
        print(f"{item}: {amount}" if item != "coffee" else f"{item}: {amount}")

    print(f"Cups sold: {cups_sold}")


def coffee_machine():
    while True:
        choice = input("What would you like?\n")

        if not is_capable_to_make_coffee():
            break

        elif choice == "exit":
            break
        elif choice == "report":
            generate_report()
        elif choice in MENU:
            if is_ingredients_sufficient(choice):
                make_coffee(choice)

        else:
            pass


coffee_machine()



















