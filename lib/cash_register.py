#!/usr/bin/env python3

# lib/cash_register.py
class CashRegister:
    """A simple cash register for the lab tests."""

    def __init__(self, discount=0):
        """
        Initialize a CashRegister.
        :param discount: integer percentage (e.g. 20 for 20%).
        """
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        """
        Add an item (or multiple) to the register.
        - title: name of the item (string)
        - price: price per item (int or float)
        - quantity: number of items to add (default 1)
        This updates the total, appends the item name `quantity` times to items,
        and records the last transaction amount for possible voiding.
        """
        total_price = price * quantity
        self.total += total_price
        self.last_transaction = total_price

        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """
        Apply the register's discount to the total and print the result.
        """
        if not self.discount:
            print("There is no discount to apply.")
            return

        discounted = self.total * (100 - self.discount) / 100

        if isinstance(discounted, float) and discounted.is_integer():
            discounted = int(discounted)
        else:
            discounted = round(discounted, 2)
            if isinstance(discounted, float) and discounted.is_integer():
                discounted = int(discounted)

        self.total = discounted
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        """
        Remove the last transaction amount from the total.
        Resets last_transaction to 0 afterwards.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0

