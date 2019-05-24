def all_elements_equal(my_list, check_val=None):
    '''
    Returns true of all elements in the list are equal to a provided value 
    or all the list elements are the same if no check value is provided.
    '''
    if check_val:
        return all(x==check_val for x in my_list)
    else:    
        return all(x==my_list[0] for x in my_list)