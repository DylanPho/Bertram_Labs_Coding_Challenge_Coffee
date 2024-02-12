# *** Bertram Labs Coding Challenge ***
# Name: Dylan Phoutthavong
# Date: 02/07/2024

# Prompt:
    # Write a software program to help the coworkers decide who should pay for coffee.
    # Consider that not all drinks cost the same, so to be fair please take this into
    # account when crafting your solution.

import random

class CoffeeCoworker:
    def __init__(person, name, coffee_order):
        person.name = name
        person.coffee_order = coffee_order

price_of_coffee = {
    "Cappuccino": 3.50,
    "Black Coffee": 2.00,
    "Latte": 4.00,
    "Espresso": 3.00,
    "Mocha": 4.50,
    "Macchiato": 3.75,
    "Americano": 2.50,
    "Iced Coffee": 4.00
}

def input_ordered_coffees(coworkers):

    # Prompt the user to input the type of coffee each coworker ordered.

    # Args:
        # - coworkers: List of CoffeeCoworker objects

    # Returns: None  

    print("Here are the available coffee types and the prices: \n")
    for coffee, price in price_of_coffee.items():
        print(f"{coffee}: ${price}")
    print("\nPlease enter the type of coffee each person ordered:")
    for coworker in coworkers:
        coffee_order = input(f"{coworker.name}'s ordered coffee: ")
        coworker.coffee_order = coffee_order

def select_coffee_payer(coworkers):

    # Randomly select a coworker to pay for coffee based on the prices of their ordered coffees.

    # Args:
        # - coworkers: List of CoffeeCoworker objects

    # Returns:
        # CoffeeCoworker: The selected coworker to pay for coffee

    total_price = sum(price_of_coffee[coworker.coffee_order] for coworker in coworkers)
    rand_num = random.uniform(0, total_price)
    running_total = 0
    for coworker in coworkers:
        running_total += price_of_coffee[coworker.coffee_order]
        if rand_num <= running_total:
            return coworker

def main():
    while True:
        coworkers = [
            CoffeeCoworker("Bob", ""),
            CoffeeCoworker("Jeremy", ""),
            CoffeeCoworker("Dylan", ""),
            CoffeeCoworker("Lexie", ""),
            CoffeeCoworker("Ivy", ""),
            CoffeeCoworker("Cynthia", ""),
            CoffeeCoworker("Bertina", "")
        ]

        input_ordered_coffees(coworkers)
        payer = select_coffee_payer(coworkers)
        print(f"\nIt's {payer.name}'s turn to pay for coffee today.")

        again = input("\nWould you like to select another coffee payer? (yes/no): ")
        if again.lower() != "yes":
            print("Thanks! Enjoy your day :)")
            break
        else:
            print()

if __name__ == "__main__":
    main()
