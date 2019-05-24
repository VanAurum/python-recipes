from difflib import get_close_matches

def close_matches(word, possibilities, n=3, cutoff=0.6):
    '''
    Returns a list of close matches to word from the list possibilities.  
    '''
    return get_close_matches(word, possibilities, n, cutoff) 