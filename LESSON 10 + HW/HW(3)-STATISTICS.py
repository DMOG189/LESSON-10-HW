# HOMEWORK 3 STATISTICS

# STATISTICS:
# write a python function
# receiving a list of numbers
# and returning statistics about:
# average, max, min, sum, count

# START

def get_statistics(numbers: list[int]) -> dict:
    if not numbers:
        return {
            'average': None,
            'max': None,
            'min': None,
            'count': 0,
            'sum': 0
        }

    statistics = {
        'average': sum(numbers) / len(numbers),
        'max': max(numbers),
        'min': min(numbers),
        'count': len(numbers),
        'sum': sum(numbers)
    }

    return statistics

numbers = [10, 20, 30, 40, 50]
stats = get_statistics(numbers)
print(stats)

# END