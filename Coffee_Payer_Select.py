# *** Bertram Labs Coding Challenge ***
# Name: Dylan Phoutthavong
# Date: 02/07/2024

# Prompt:
# Write a software program to help the coworkers decide who should pay for coffee.
# Consider that not all drinks cost the same, so to be fair please take this into
# account when crafting your solution.

import random  # Importing random library to randomly select the first coffee payer.

# Define a class to represent a coworker and their coffee order.
class CoffeeCoworker:
    def __init__(self, name, coffee_order):
        self.name = name  # Store the coworker's name.
        self.coffee_order = coffee_order  # Store the type of coffee they ordered.

# Dictionary that holds the price of each type of coffee.
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

# Function to input coffee orders for each coworker.
def input_ordered_coffees(coworkers):
    # Display the available coffee types and their prices.
    print("Here are the available coffee types and the prices:\n")
    for coffee, price in price_of_coffee.items():
        print(f"{coffee}: ${price}")
    print("\nPlease enter the type of coffee each person ordered:")

    # Prompt the user to input the coffee order for each coworker.
    for coworker in coworkers:
        coffee_order = input(f"{coworker.name}'s ordered coffee: ")
        coworker.coffee_order = coffee_order  # Store the input coffee order.

# Function to select the next payers in a rotational order.
# Takes the list of coworkers and the index of the first payer.
def select_coffee_payers(coworkers, first_payer_index):
    payers = []  # List to hold the order of the next payers.
    next_index = (first_payer_index + 1) % len(coworkers)  # Start from the next coworker.

    # Add coworkers to the payer list until everyone, except the first payer, is included.
    while len(payers) < len(coworkers) - 1:
        payers.append(coworkers[next_index])  # Append the next payer to the list.
        next_index = (next_index + 1) % len(coworkers)  # Move to the next index.
    
    return payers  # Return the list of next payers.

# Main function that initializes the program and controls the flow.
def main():
    # List of coworkers with empty coffee orders initially.
    coworkers = [
        CoffeeCoworker("Bob", ""),
        CoffeeCoworker("Jeremy", ""),
        CoffeeCoworker("Dylan", ""),
        CoffeeCoworker("Lexie", ""),
        CoffeeCoworker("Ivy", ""),
        CoffeeCoworker("Cynthia", ""),
        CoffeeCoworker("Bertina", "")
    ]

    # Get the coffee order from each coworker.
    input_ordered_coffees(coworkers)

    # Randomly select the first person to pay for coffee.
    first_payer_index = random.randint(0, len(coworkers) - 1)  # Random index.
    first_payer = coworkers[first_payer_index]  # Get the coworker at that index.
    print(f"\nIt's {first_payer.name}'s turn to pay for coffee today.\n")  # Announce the first payer.

    # Determine the order of the next payers, excluding the first payer.
    print("The next payer will be in the following order:")
    next_payers = select_coffee_payers(coworkers, first_payer_index)
    
    # Display the names of the next payers in order.
    for payer in next_payers:
        print(f"{payer.name}")

# Entry point of the program.
if __name__ == "__main__":
    main()  # Run the main function.
