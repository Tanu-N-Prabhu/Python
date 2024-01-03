def hashmap(key, value):
    """
    Create a hashmap.

    Args:
        key: The key to store in the hashmap.
        value: The value to associate with the key.

    Returns:
        The hashmap.
    """
    hashmap = {}
    hashmap[key] = value
    return hashmap


def get(hashmap, key):
    """
    Get the value associated with a key in a hashmap.

    Args:
        hashmap: The hashmap.
        key: The key to get the value for.

    Returns:
        The value associated with the key, or None if the key is not in the hashmap.
    """
    if key in hashmap:
        return hashmap[key]
    else:
        return None


def put(hashmap, key, value):
    """
    Add a key-value pair to a hashmap.

    Args:
        hashmap: The hashmap.
        key: The key to add.
        value: The value to associate with the key.
    """
    hashmap[key] = value


def delete(hashmap, key):
    """
    Delete a key-value pair from a hashmap.

    Args:
        hashmap: The hashmap.
        key: The key to delete.
    """
    if key in hashmap:
        del hashmap[key]


hashmap = hashmap("key1", "value1")
print(hashmap)
# {'key1': 'value1'}

print(get(hashmap, "key1"))
# value1

put(hashmap, "key2", "value2")
print(hashmap)
# {'key1': 'value1', 'key2': 'value2'}

delete(hashmap, "key1")
print(hashmap)
# {'key2': 'value2'}
