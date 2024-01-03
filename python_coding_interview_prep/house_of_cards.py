"""
You want to build a standard house of cards, but you don't know how many cards you will need.
Write a program which will count the minimal number of cards according to the number of floors
you want to have. For example, if you want a one floor house, you will need 7 of them
(two pairs of two cards on the base floor, one horizontal card and one pair to get the first floor).
Here you can see which kind of house of cards I mean:
/\/\
- -

S=2+(2+3)+(2+3+3)+...+(2+3+..+3)=2(n+1)+3(1+2+3+...+n)=2(n+1)+3(n(n+1)/2)
"""
import unittest


def house_of_cards(floors):
    if floors < 1:
        raise ValueError("floors must be greater than or equal to 1")

    # Calculate the number of cards for the base floor
    # Certainly! Let's break down the expression `base_floor_cards = 2 * (2 * floors + 1)`:
    # 1. `2 * floors`: This part calculates twice the number of floors.
    # Each floor requires two pairs of cards, one for each side, so doubling the number of
    # floors accounts for the pairs.
    #
    # 2. `2 * floors + 1`: Adding 1 to the doubled number of floors. The additional 1
    # represents the horizontal card that connects the pairs on the base floor.
    #
    # 3. ` (2 * floors + 1)`: adding 1 to the doubled number of floors. The additional 1
    #
    # So, the entire expression calculates the total number of cards needed for the base
    # floor of the house of cards, considering the pairs and the horizontal card connecting them.
    base_floor_cards = (2 * floors + 1) + 1

    # Calculate the number of cards for the additional floors
    # range(2, floors + 1): This creates a range of numbers from 2 to floors (inclusive).
    # This represents the number of additional floors beyond the base floor.
    #
    # sum(range(2, floors + 1)): This calculates the sum of the numbers in the range,
    # representing the total number of pairs needed for the additional floors.
    #
    # sum(range(2, floors + 1)) * 3: Multiplying the sum by 3. Each additional floor requires
    # three pairs of cards – one for each side and one for the horizontal card connecting them.
    additional_floor_cards = sum(range(1, floors + 1)) * 3
    print(additional_floor_cards)

    # Total number of cards needed
    total_cards = base_floor_cards + additional_floor_cards

    return total_cards


class TestDecodeMorse(unittest.TestCase):
    def test_decode_morse(self):
        self.assertEqual(house_of_cards(1), 7)
        self.assertEqual(house_of_cards(2), 15)
        self.assertEqual(house_of_cards(3), 26)
        self.assertEqual(house_of_cards(6), 77)
        self.assertEqual(house_of_cards(15), 392)
        self.assertEqual(house_of_cards(0), ValueError("floors must be greater than or equal to 1"))


if __name__ == '__main__':
    test_decode_morse = TestDecodeMorse()
    TestDecodeMorse.test_decode_morse(self=test_decode_morse)
