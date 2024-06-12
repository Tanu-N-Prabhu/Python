# "QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card. test = {
#     'input': { 
#         'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
#         'query': 7
#     },
#     'output': 3
# }"


def binary_search(lo, hi, condition):
    """
    Performs binary search to find the index of an element that meets a specified condition.

    Parameters:
    lo (int): The lower bound index of the search range.
    hi (int): The upper bound index of the search range.
    condition (function): A function that takes the index as input and returns 'found', 'left', or 'right' based on the search condition.

    Returns:
    int: The index of the element that meets the condition, or -1 if not found.
    """
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# decorator
def locate_card(cards, query):
    """
    Locates the position of a query element within a sorted list using binary search.

    Parameters:
    cards (List[int]): A sorted list of integers representing cards.
    query (int): The integer to search for within the list.

    Returns:
    int: The index of the query element in the list, or -1 if not found.
    """
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(cards) - 1, condition)

# test cases
test = {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
       },
       'output': 3
    }
print(locate_card(**test['input']) == test['output'])
