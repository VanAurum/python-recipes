from collections import Counter

def get_n_most_common(iterable,n):
    '''
    Accepts an iterable and returns the n most common occurrences.
    '''
    return Counter(iterable).most_common(n)