# HOMEWORK 1 DICT

# DICT:
# 1. Create the dictionary:
# 1. Find and print the capital city:
# 2. Print all the keys:
# 3. Create a list containing only the keys in uppercase:
# 4. Print all the values:
# 5. Create a list containing only the lengths of the values:
# 6. Print all key-value pairs:
# 7. Copy the dictionary to a new dictionary:
# 8. Clear the new dictionary of its values:
# 9. Create a new dictionary with the same keys but all values as None:
# 10. Delete the currency key (and its value):
# 11. Pop the area_Kilometer key (and its value):
# 12. Update the dictionary in one operation:
# a. Add a new key-value pair 'Soccer': 'sport_national'.
# b. Update the population_millions key to 9.4.



# START

# 1. Create the dictionary:
israel = {
    'name': 'Israel',
    'birth': 1948,
    'population_millions': 9.3,
    'capital': 'Jerusalem',
    'language': 'Hebrew',
    'cities': ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
    'currency': 'ILS',
    'area_Kilometer': 22145,
    'gdp_billion': 450
}

# 1. Find and print the capital city:
capital_city = israel.get('capital')
print("Capital city:", capital_city)

# 2. Print all the keys:
keys = israel.keys()
print("Keys:", keys)

# 3. Create a list containing only the keys in uppercase:
uppercase_keys = [key.upper() for key in israel.keys()]
print("Uppercase keys:", uppercase_keys)

# 4. Print all the values:
values = israel.values()
print("Values:", values)

# 5. Create a list containing only the lengths of the values:
values_lengths = [len(str(value)) for value in israel.values()]
print("Lengths of values:", values_lengths)

# 6. Print all key-value pairs:
items = israel.items()
print("Key-value pairs:", items)

# 7. Copy the dictionary to a new dictionary:
israel_copy = israel.copy()
print("Copied dictionary:", israel_copy)

# 8. Clear the new dictionary of its values:
israel_copy.clear()
print("Cleared dictionary:", israel_copy)

# 9. Create a new dictionary with the same keys but all values as None:
none_values_dict = dict.fromkeys(israel.keys(), None)
print("Dictionary with None values:", none_values_dict)

# 10. Delete the currency key (and its value):
del israel['currency']
print("Dictionary after deleting 'currency':", israel)

# 11. Pop the area_Kilometer key (and its value):
area_kilometer_value = israel.pop('area_Kilometer')
print("Popped 'area_Kilometer':", area_kilometer_value)
print("Dictionary after popping 'area_Kilometer':", israel)

# 12. Update the dictionary in one operation:
# a. Add a new key-value pair 'Soccer': 'sport_national'.
# b. Update the population_millions key to 9.4.
israel.update({'Soccer': 'sport_national', 'population_millions': 9.4})
print("Updated dictionary:", israel)

# END