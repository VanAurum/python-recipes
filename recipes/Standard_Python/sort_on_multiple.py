from operator import itemgetter

def sort_on_multiple(my_list, instructions):
    '''
    Sorts a list of tuples or list of lists according to multiple instructions.  

    Args:
        my_list (list of lists of list of tuples)
        instryctions (List of tuples) : e.g [(0, 'asc'), (1, 'desc'), (2', 'desc')]
    '''    
    for inst in instructions:
        if inst[1]=='desc':
            reverse=True
        else:
            reverse=False    

        my_list.sort(key = itemgetter(inst[0]), reverse=reverse)
    return my_list    