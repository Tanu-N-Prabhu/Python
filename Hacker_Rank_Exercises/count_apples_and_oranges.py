"""
https://www.hackerrank.com/challenges/apple-and-orange/problem

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
  """
  This function counts the number of apples and oranges that land on Sam's house.

  Args:
      s: Starting point of Sam's house location.
      t: Ending location of Sam's house location.
      a: Location of the Apple tree.
      b: Location of the Orange tree.
      apples: Array containing distances at which each apple falls from the tree.
      oranges: Array containing distances at which each orange falls from the tree.
  """
  apple_count = 0
  orange_count = 0

  # Loop through each apple distance
  for apple_distance in apples:
    # where apple landed
    landing_position = a + apple_distance
    # if apple landed between starting and ending position of Sams house
    if s <= landing_position <= t:
      apple_count += 1

  # Loop through each orange distance 
  for orange_distance in oranges:
    # where orange landed
    landing_position = b + orange_distance
    # if orange landed between starting and ending position of Sams house
    if s <= landing_position <= t:
      orange_count += 1

  # Print the number of apples and oranges
  print(apple_count)
  print(orange_count)


if __name__ == '__main__':
    # No code here
    # Example usage (replace with your actual input values)
    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-2, 2, 1]
    oranges = [5, -6]
    countApplesAndOranges(s, t, a, b, apples, oranges)
