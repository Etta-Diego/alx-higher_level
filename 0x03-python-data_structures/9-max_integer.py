#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = my_list[0]
    if my_list is None:
        return None
    for num in my_list:
        if num > maxi:
            maxi = num
    return maxi
