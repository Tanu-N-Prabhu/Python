import numpy as np  # Import NumPy for efficient arrays (habit for numerical tasks)

def debug_script(filename):  # Reusable debugging function with clear naming
    """Starts the Python debugger for the given script."""
    import pdb  # Import pdb for debugging
    pdb.runfile(filename)  # Concise way to start debugging

def days_generator(start_index=0):  # Generator function for day names
    """Yields day names sequentially, starting from the given index."""
    days = ['S', 'M', 'T', 'W', 'Tr', 'F', 'St']
    for day in days[start_index:]:
        yield day

def list_to_string(data):  # Function to handle various data types
    """Converts a list, tuple, or set to a string with spaces between elements."""
    if isinstance(data, (list, tuple, set)):
        return ' '.join(data)
    raise TypeError("Input must be a list, tuple, or set")  # Handle invalid input

def count_occurrences(data, element):  # Function for counting occurrences
    """Counts the number of times 'element' appears in 'data' (list or tuple)."""
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    return data.count(element)

def create_numpy_array(data):  # Function for array creation (flexible for different data types)
    """Creates a NumPy array from a list, tuple, or even another NumPy array."""
    return np.array(data)

# Example usage (can be refactored into a more modular structure if needed)
day_gen = days_generator(2)  # Get day names starting from index 2 (Wednesday)
print(next(day_gen))  # Print the first day

weekdays = ['M', 'W', 'F']
print(list_to_string(weekdays))  # Print weekdays as a string

my_list = [1, 2, 2, 3, 4]
print(count_occurrences(my_list, 2))  # Count occurrences of 2

data = [5, 6, 7]
arr = create_numpy_array(data)
print(arr.dtype)  # Check the array's data type (habit for type awareness)
