#!/usr/bin/python3

# Define a function named best_score
def best_score(my_dict):
    # Check if the dictionary is not empty
    if my_dict:
        # Find the key with the maximum value using max() and return it
        return max(my_dict, key=my_dict.get)
    else:
        # If the dictionary is empty, return None
        return None
