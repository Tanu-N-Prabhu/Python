# Context:
# This script takes user input related to shoe sizes, their availability, and purchase details.
# It calculates the total revenue from selling shoes based on the available sizes and prices.

# Input:
# - x: An integer representing the number of available shoe sizes.
# - shoe_size: A list containing the available shoe sizes as integers.
# - n: An integer representing the number of purchase transactions.
# - sell: A variable initialized to 0, which accumulates the total revenue.
# x = int(input())
# shoe_size = list(map(int, input().split()))
# n = int(input())
# sell = 0

# Test the function with sample input
x = 5
shoe_sizes = [10, 8, 7, 6, 9]
n = 3
sell = [(8, 50), (6, 30), (9, 40)]

# Loop through each purchase transaction:
for _ in range(n):
    # Read the size (s) and price (p) of the desired shoe.
    # s, p = map(int, input().split())
    s, p = map(int, sell.pop(0))
    
    # Check if the desired shoe size is available in the store.
    if s in shoe_sizes:
        # If available, add the price to the total revenue and remove the sold shoe size from the available sizes.
        sell = sell + [p]
        # sell = sell + p
        shoe_sizes.remove(s)

# Output:
# Print the total revenue generated from selling the available shoes.
print(sum(sell))
