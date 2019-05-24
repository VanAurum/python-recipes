from collections import OrderedDict

def remove_list_duplicates(lst):
    '''
    removes duplicates from list while preserving order of list.
    '''
    return list(OrderedDict.fromkeys(lst))