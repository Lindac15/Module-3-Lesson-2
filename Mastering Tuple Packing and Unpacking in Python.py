# Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Input: orders = [("Alice", "Apple", 5), ("Bob", "Banana", 3), ("Charlie", "Cherry", 7)]
# Sample Output: Alice ordered 5 Apples Bob ordered 3 Bananas Charlie ordered 7 Cherries
# - Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display


def print_orders(orders):
    for order in orders:
        name, product, quantity = order
        print(f"{name} ordered {quantity} {product}s")


orders = [("Alice", "Apple", 5), ("Bob", "Banana", 3), ("Charlie", "Cherry", 7)]
print_orders(orders)








