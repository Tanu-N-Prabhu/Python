def solution(queries):
    """
    Perform operations on an in-memory database based on the given queries.

    Parameters:
    - queries (list): List of queries, where each query is represented as a sublist.

    Returns:
    - list: List of results corresponding to each query.

    Constraints:
    - The length of the queries list should be between 1 and 500 (inclusive).
    """

    # Initialize an empty dictionary to store key-value pairs.
    temp = {}

    # Initialize an empty list to store the results of each query.
    result = []

    # Check if the queries list is not empty and within the allowed length.
    if queries and 1 <= len(queries) <= 500:
        for sublist in queries:
            # Extract command, key, and field from the current sublist.
            command, key, field = sublist[0], sublist[1], sublist[2]

            # Process "set_or_inc" command.
            if command.lower() == "set_or_inc":
                # Extract the value from the sublist.
                value = sublist[3]

                # Update the in-memory database with the key-value pair.
                # is using a tuple (key, field) pair as a key in a dictionary
                temp[(key, field)] = str(value)

                # Append the value to the result list.
                result.append(str(value))

            # Process "get" command.
            elif command.lower() == "get":
                # Retrieve the value for the specified key and field from the database.
                # if not found matched key then send empty string
                result.append(temp.get((key, field), ""))

            # Process "delete" command.
            elif command.lower() == "delete":
                # Check if the key and field exist in the database and delete if present.
                if (key, field) in temp:
                    del temp[(key, field)]
                    result.append("true")
                else:
                    result.append("false")

    # Return the final result list.
    return result



import pytest

# Test Case 1: Set or Increment
def test_SET_OR_INC():
    queries = [["SET_OR_INC", "EMPLOYEE_1", "NAME", "Guddu"]]
    assert solution(queries) == ["Guddu"]

# Test Case 2: GET
def test_GET():
    queries = [["SET_OR_INC", "EMPLOYEE_1", "NAME", "Guddu"], ["GET", "EMPLOYEE_1", "NAME"]]
    assert solution(queries) == ["Guddu", "Guddu"]

# Test Case 3: DELETE
def test_DELETE():
    queries = [["SET_OR_INC", "EMPLOYEE_2", "NAME", "Guddu"], ["DELETE", "EMPLOYEE_2", "NAME"]]
    assert solution(queries) == ["Guddu", "true"]

# Test Case 4: Non-existent Key/Field in GET
def test_GET_non_existent():
    queries = [["SET_OR_INC", "EMPLOYEE_3", "NAME", "Guddu"], ["GET", "AGE", "NAME"]]
    assert solution(queries) == ["Guddu", ""]

# Test Case 5: Non-existent Key/Field in DELETE
def test_DELETE_non_existent():
    queries = [["SET_OR_INC", "EMPLOYEE_1", "NAME", "Guddu"], ["SET_OR_INC", "EMPLOYEE_2", "AGE", "30"], ["DELETE", "AGE", "NAME"]]
    assert solution(queries) == ["Guddu", "30", "false"]

# Add more test cases as needed...

if __name__ == "__main__":
    pytest.main()
