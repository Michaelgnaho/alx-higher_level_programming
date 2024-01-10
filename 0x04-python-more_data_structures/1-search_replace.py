#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for n in my_list:
        if n == search:
            result.append(replace)
        else:
            result.append(n)
    return result
