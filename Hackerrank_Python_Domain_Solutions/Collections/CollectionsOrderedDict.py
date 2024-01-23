# Context:
# This script takes user input related to items and their prices, and then consolidates the total price for each unique item.

# Input:
# - n: An integer representing the number of items.
# - item_od: An ordered dictionary to store item names as keys and their cumulative prices as values.
# - Loop through each item:
#   - Parse the input to extract item name and price.
#   - Update the ordered dictionary with the cumulative price for each item.
import collections
import re

n = int(input())
item_od = collections.OrderedDict()
for _ in range(n):
    # Parse the input to extract item name and price.
    # - Split the input string on the last digit.
    # - The first part is the item name.
    # - The second part is the item price.
    record_list = re.split(r"(\d+)$", input().strip())
    item_name = record_list[0]
    item_price = int(record_list[1])
    if item_name not in item_od:
        item_od[item_name] = item_price
    else:
        item_od[item_name] = item_od[item_name] + item_price

# Output:
# - Print each item name along with its total price.
for i in item_od:
    print(f"{i}{item_od[i]}")
