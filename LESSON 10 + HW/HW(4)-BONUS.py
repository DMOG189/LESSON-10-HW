# HOMEWORK 4 BONUS

# input from user int + operation
# Create a dictionary of string operations
# Get the word and the operation from the user
# Find the operation in the dictionary and apply it

# START

def main():
    oper_dict = {
        "lower": lambda w: w.lower(),
        "upper": lambda w: w.upper(),
        "len": lambda w: len(w),
        "reverse": lambda w: w[::-1]
    }

    word = input("Enter word: ")
    operation = input("Enter operation name (lower, upper, len, reverse): ")

    result = oper_dict.get(operation, lambda w: "Unknown operation")(word)

    print(result)

main()

# END