import itertools as it

def get_combinations(iterable, n):
    '''Return all combinations from iterable of length n
    '''
    return list(it.combinations(iterable,n))