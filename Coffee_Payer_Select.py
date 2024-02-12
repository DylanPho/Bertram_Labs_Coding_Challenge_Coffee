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
    print("\nPlease enter the type of coffee each person ordered:\n")
    for coworker in coworkers:
        coffee_order = input(f"{coworker.name}'s ordered coffee: ")
        coworker.coffee_order = coffee_order

def select_coffee_payer(coworkers):
    total_price = sum(price_of_coffee[coworker.coffee_order] for coworker in coworkers)
    rand_num = random.uniform(0, total_price)
    running_total = 0
    for coworker in coworkers:
        running_total += price_of_coffee[coworker.coffee_order]
        if rand_num <= running_total:
            return coworker

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

    # Select the payer for today
    payer_today = select_coffee_payer(coworkers)
    print(f"\nIt's {payer_today.name}'s turn to pay for coffee today.")

    # Select the payer for the next day
    coworkers.remove(payer_today)  # Remove today's payer from the list
    payer_next_day = select_coffee_payer(coworkers)
    print(f"{payer_next_day.name} will pay for coffee tomorrow.")

if __name__ == "__main__":
    main()
