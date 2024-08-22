# HOMEWORK 2 DICT

# dict instead of match case:

# START

# Original match-case function:
def perform_action(action):
    match action:
        case 'add':
            return 'Adding item'
        case 'delete':
            return 'Deleting item'
        case 'update':
            return 'Updating item'
        case _:
            return 'Unknown action'

result = perform_action('add')
print(result)  # Output: Adding item

# Rewriting the function using a dictionary:
def perform_action(action):
    actions_dict = {
        'add': 'Adding item',
        'delete': 'Deleting item',
        'update': 'Updating item'
    }
    return actions_dict.get(action, 'Unknown action')

result = perform_action('add')
print(result)  # Output: Adding item




# END