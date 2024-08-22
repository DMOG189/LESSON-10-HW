# HOMEWORK 5 CODE EXAMPLE

# START

# CODE GIVEN:
def remove_key_from_dict(dictionary: dict):
dictionary.popitem()
def clear_all(dictionary: dict):
dictionary = { }
a = {'x': 1, 'y': 2}
remove_key_from_dict(a)
print(a)
clear_all(a)
print(a)


# 1. Does the dictionary sent to the function remove_key_from_dict change?
# Yes, the dictionary will change.
# When you pass a dictionary to a function and modify it (e.g., removing an item using popitem()),
# the original dictionary is directly affected because dictionaries are mutable objects in Python.
# The changes made inside the function will reflect outside the function as well.

# EXAMPLE:
a = {'x': 1, 'y': 2}
remove_key_from_dict(a)
print(a)
# Output: {'x': 1} or {'y': 2}


# 2. Does the dictionary sent to the function clear_all change?
# No, the dictionary will not change.
# In the clear_all function, the reassignment dictionary = {} creates a new local dictionary within the function’s scope.
# This does not affect the original dictionary outside the function.
# The original reference to the dictionary remains unchanged.

# EXAMPLE:
a = {'x': 1, 'y': 2}
clear_all(a)
print(a)
# Output: {'x': 1, 'y': 2}

# 3. How to clear the dictionary inside a function so that it affects the dictionary outside?
# To clear the dictionary so that the change is reflected outside the function,
# you should modify the dictionary in-place using the clear() method, which empties the dictionary:

# EXAMPLE:
def clear_all(dictionary: dict):
    dictionary.clear()

a = {'x': 1, 'y': 2}
clear_all(a)
print(a)
# Output: {}

# END