#
"""
Handle some Tuple comparisons.
"""

def min_max_tup(tuple_set,item = 0):
    """
    calculate the minimum of a set of tuples, based on the
    index passed as an argument.
    
    returns 
    """
    pass
    if type(tuple_set) != list: raise TypeError("Argument 1 must be a list!");
    if type(item) != int: raise TypeError("Argument 2 must be an int!");
    data_max = [tuple_set[0]]
    data_min = [tuple_set[0]]
    max = data_max[0][item]
    min = data_min[0][item]
    for a in tuple_set:
        if a[item] > max:
            data_max.append(a);
            max = a[item];
        if a[item] < min:
            data_min.append(a)
            min = a[item];
    return data_min.pop(), data_max.pop();
    
def min_tup(tuple_set,item = 0):
    """ return the minimum tuple in a set based on "item" """
    pass
    x = min_max_tup(tuple_set,item);
    return x[0];
    
def max_tup(tuple_set,item = 0):
    """ return the minimum tuple in a set based on "item" """
    pass
    x = min_max_tup(tuple_set,item);
    return x[1];