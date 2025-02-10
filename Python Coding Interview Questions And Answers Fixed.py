def debug_script(filename):  # Reusable debugging function with clear naming
    """Starts the Python debugger for the given script."""
    import pdb  # Import pdb for debugging
    with open(filename) as f:
        code = compile(f.read(), filename, 'exec')
        pdb.run(code)  # Standard way to debug code

def days_generator(start_index=0):
    """Yields day names sequentially, starting from the given index.
    
    Args:
        start_index (int): Starting index in the days list (0=Sunday)
        
    Returns:
        generator: Yields day names as strings
        
    Example:
        >>> gen = days_generator(2)  # Start from Tuesday
        >>> next(gen)
        'Tue'
    """
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for day in days[start_index:]:
        yield day

def list_to_string(data):
    """Converts a list, tuple, or set to a string with spaces between elements.
    
    Args:
        data: Input collection (list, tuple, or set) to be converted
        
    Returns:
        str: Space-separated string of elements
        
    Raises:
        TypeError: If input is not a list, tuple, or set
    """
    if isinstance(data, (list, tuple, set)):
        return ' '.join(str(x) for x in data)
    raise TypeError(f"Expected list, tuple, or set, but got {type(data).__name__}")

def count_occurrences(data, element):
    """Counts the number of times an element appears in a sequence.
    
    Args:
        data: Input sequence (list or tuple) to search in
        element: The element to count occurrences of
        
    Returns:
        int: Number of occurrences of element in data
        
    Raises:
        TypeError: If data is not a list or tuple
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError(f"Expected list or tuple, but got {type(data).__name__}")
    return data.count(element)

def create_numpy_array(data):  # Function for array creation (flexible for different data types)
    """Creates a NumPy array from a list, tuple, or even another NumPy array.
    
    Args:
        data: Input data that can be converted to a numpy array
        
    Returns:
        numpy.ndarray: A numpy array containing the input data
        
    Raises:
        ImportError: If numpy is not installed
    """
    try:
        import numpy as np
        return np.array(data)
    except ImportError:
        raise ImportError("NumPy is required for this function. Install it using 'pip install numpy'")

# Example usage
day_gen = days_generator(2)  # Get day names starting from index 2 (Tuesday)
print(next(day_gen))  # Print the first day

weekdays = ['Mon', 'Wed', 'Fri']
print(list_to_string(weekdays))  # Print weekdays as a string

my_list = [1, 2, 2, 3, 4]
print(count_occurrences(my_list, 2))  # Count occurrences of 2

data = [5, 6, 7]
arr = create_numpy_array(data)
print(arr.dtype)  # Check the array's data type (habit for type awareness)
