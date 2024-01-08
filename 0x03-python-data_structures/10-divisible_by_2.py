#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lists= []
    if my_list:
        for num in my_list:
            new_lists.append(False if num % 2 else True)
        return new_lists
