# *** Bertram Labs Coding Challenge ***
# Name: Dylan Phoutthavong
# Date: 02/07/2024

# Prompt:
    # Write a software program to help the coworkers decide who should pay for coffee.
    # Consider that not all drinks cost the same, so to be fair please take this into
    # account when crafting your solution.

import random

class CoffeeCoworker:
    def __init__(self, name, coffee_order):
        self.name = name
        self.coffee_order = coffee_order

price_of_coffee = {
    "Cappuccino": 3.50,
    "Black Coffee": 2.00,
    "Latte": 4.00,
    "Espresso": 3.00,
    "Mocha": 4.50,
    "Macchiato": 3.75,
    "Americano": 2.50,
    "Iced Coffee": 3.50
}

def input_ordered_coffees(coworkers):
    print("Here are the available coffee types and the prices:\n")
    for coffee, price in price_of_coffee.items():
        print(f"{coffee}: ${price}")
    print("\nPlease enter the type of coffee each person ordered:")
    for coworker in coworkers:
        coffee_order = input(f"{coworker.name}'s ordered coffee: ")
        coworker.coffee_order = coffee_order

def select_coffee_payers(coworkers, first_payer_index):
    payers = []
    next_index = (first_payer_index + 1) % len(coworkers)
    while len(payers) < len(coworkers) - 1:
        payers.append(coworkers[next_index])
        next_index = (next_index + 1) % len(coworkers)
    return payers

def main():
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

    # Select the first person randomly
    first_payer_index = random.randint(0, len(coworkers) - 1)
    first_payer = coworkers[first_payer_index]
    print(f"\nIt's {first_payer.name}'s turn to pay for coffee today.\n")

    # List the next coffee payers in rotational order, excluding the first payer
    print("The next payer will be in the following order:")
    next_payers = select_coffee_payers(coworkers, first_payer_index)
    for payer in next_payers:
        print(f"{payer.name}")

if __name__ == "__main__":
    main()
