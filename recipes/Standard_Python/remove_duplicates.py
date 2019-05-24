from collections import OrderedDict

def remove_duplicates(string):
    '''
    Removes contiguous and non-contiguous duplicates from a string
    '''
    return ''.join(list(OrderedDict.fromkeys(string)))    