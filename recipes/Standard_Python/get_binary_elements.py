import itertools as it

def get_binary_elements(n):
    '''
    Get all binary values of length n.
    '''
    return [''.join(x) for x in list(it.product('01',repeat=n))]