import math

def matrify(array):
    '''
    Accepts a flat array and converts to an n x n matrix if the length has a whole square root.
    '''
    n=int(math.sqrt((len(array))))
    return [[array.pop(0) for _ in range(n)] for _ in range(n)]