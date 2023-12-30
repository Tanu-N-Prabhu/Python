def check_distinct(data_list):
    # Check if the length of the list is equal to the length of the set
    # A set automatically removes duplicate elements, so if they are equal, all elements are distinct
    if len(data_list) == len(set(data_list)):
        # Return True if all elements are distinct
        return True
    else:
        # Return False if there are duplicates
        return False


print(check_distinct([1,2,3,4,5,6,7,8,9]))
