# "QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card. test = {
#     'input': { 
#         'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
#         'query': 7
#     },
#     'output': 3
# }"


def binary_search(lo, hi, condition):
    """TODO - add docs"""
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