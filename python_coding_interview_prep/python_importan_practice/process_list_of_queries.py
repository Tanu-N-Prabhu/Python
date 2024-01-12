"""
This script defines a function 'solution' to process a list of queries related to manipulating a temporary list.

Functions:
- 'solution': Processes a list of queries and performs actions like adding, checking existence, finding the next bigger element,
              and removing elements from a temporary list.

Parameters:
- queries (list): A list of queries, where each query is represented as a sublist with a key and a value.

Returns:
- result (list): A list containing the results of each query.
"""

def solution(queries):
    # Temporary list to store values
    temp = []
    # Result list to store outcomes of queries
    result = []

    # Check if queries list is not empty
    if queries:
        # Iterate through each sublist in queries
        for key, value in queries:
            # Add operation: Add value to the temporary list if conditions are met
            if key.lower() == "add" and -100 <= int(value) <= 100:
                temp.append(int(value))
                temp.sort()  # Sort the temporary list
                result.append("")  # Append an empty string to the result list

            # Exists operation: Check if the value exists in the temporary list
            elif key.lower() == "exists":
                result.append("true" if int(value) in temp else "false")

            # Get_next operation: Find the next bigger element in the temporary list
            elif key.lower() == "get_next":
                find_bigger = lambda x: next((element for element in temp if element > x), None)
                result.append(str(find_bigger(int(value))) if find_bigger(int(value)) is not None else "")

            # Remove operation: Remove the value from the temporary list if it exists
            elif key.lower() == "remove":
                # after successfully removed the value it must return None
                result.append("true" if int(value) in temp and temp.remove(int(value)) is None else "false")

    # Return the result list
    return result
