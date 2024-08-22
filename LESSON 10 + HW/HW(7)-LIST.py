# HOMEWORK 7 LIST

# LIST
# 1. Filter the list for countries with more than 30 million people using filter.
# 2. Filter the list for countries established after 1800 using filter.
# 3. Create a list of just the country names using map.
# 4. Create a list of just the birth years of the countries using map.
# 5. Sort the list of countries by their birth year using sort.
# 6. Sort the list of countries by their population using sort.

# START

# LIST:

countries = [
    {'name': 'Israel', 'population': 9.3, 'birth': 1948},
    {'name': 'United States', 'population': 331.9, 'birth': 1776},
    {'name': 'Japan', 'population': 125.8, 'birth': 660},
    {'name': 'Australia', 'population': 25.7, 'birth': 1901},
    {'name': 'Canada', 'population': 38.0, 'birth': 1867}
]

# 1. Filter the list for countries with more than 30 million people using filter:
large_population_countries = list(filter(lambda c: c['population'] > 30, countries))
print("Countries with more than 30 million people:", large_population_countries)

# 2. Filter the list for countries established after 1800 using filter:
modern_countries = list(filter(lambda c: c['birth'] > 1800, countries))
print("Countries established after 1800:", modern_countries)

# 3. Create a list of just the country names using map:
country_names = list(map(lambda c: c['name'], countries))
print("List of country names:", country_names)

# 4. Create a list of just the birth years of the countries using map:
birth_years = list(map(lambda c: c['birth'], countries))
print("List of country birth years:", birth_years)

# 5. Sort the list of countries by their birth year using sort:
countries_sorted_by_birth = sorted(countries, key=lambda c: c['birth'])
print("Countries sorted by birth year:", countries_sorted_by_birth)

# 6. Sort the list of countries by their population using sort:
countries_sorted_by_population = sorted(countries, key=lambda c: c['population'])
print("Countries sorted by population:", countries_sorted_by_population)

# END