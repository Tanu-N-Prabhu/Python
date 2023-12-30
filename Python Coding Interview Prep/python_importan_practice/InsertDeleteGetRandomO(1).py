"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.



Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

To implement the RandomizedSet class, you can use a Python dictionary (a hashmap) to store the values and their corresponding indices in an array. This allows you to achieve constant time complexity for insertion and removal. Additionally, you can use a list to store the values for constant time complexity when getting a random element.
"""
import random


class RandomizedSet:

    def __init__(self):
        # Initialize the data structures
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        # If the value is already in the set, return False
        if val in self.val_to_index:
            return False

        # Add the value to the end of the list and store its index
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        # If the value is not in the set, return False
        if val not in self.val_to_index:
            return False

        # Swap the value with the last element in the list
        last_val = self.values[-1]
        index = self.val_to_index[val]
        self.values[index] = last_val
        self.val_to_index[last_val] = index

        # Remove the last element and the value's index
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # Get a random element from the list
        return random.choice(self.values)


# Example usage
if __name__ == "__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1))  # Expected output: True
    print(randomizedSet.remove(2))  # Expected output: False
    print(randomizedSet.insert(2))  # Expected output: True
    print(randomizedSet.getRandom())  # Expected output: Randomly 1 or 2
    print(randomizedSet.remove(1))  # Expected output: True
    print(randomizedSet.insert(2))  # Expected output: False
    print(randomizedSet.getRandom())  # Expected output: 2
