def any_elements_equal(my_list, check_val):
    '''
    Returns true if any value in the list equals the check value.
    '''
    return any(x==check_val for x in my_list)