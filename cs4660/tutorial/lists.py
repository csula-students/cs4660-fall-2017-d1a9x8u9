"""Lists defines simple list related operations"""
from __future__ import division

def get_first_item(li):
    """Return the first item from the list"""
    x = li[0]
    return x

def get_last_item(li):
    """Return the last item from the list"""
    x = li[-1]
    return x

def get_second_and_third_items(li):
    """Return second and third item from the list"""
    x = li[1:3]
    return x

def get_sum(li):
    """Return the sum of the list items"""
    x = sum(li)
    return x

def get_avg(li):
    """Returns the average of the list items"""
    x = sum(li)
    y = len(li)
    return x/y
    
