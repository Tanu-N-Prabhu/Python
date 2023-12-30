import json
import pickle
"""
There are two basic formats for JSON data. Either in a string or the object datastructure. 
The object datastructure, in Python, consists of lists and dictionaries which are mutable 
nested inside each other. The object datastructure allows one to use python methods 
(for lists and dictionaries) to add, list, search and remove elements from the 
datastructure. 
The String format is immutable and mainly used to pass the data into another program 
or load into a datastructure.
"""
# dumps take obj and return back string
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
# loads take string and return back obj
print(json.loads(json_string))

# pickling
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
# unpickling
print(pickle.loads(pickled_string))
