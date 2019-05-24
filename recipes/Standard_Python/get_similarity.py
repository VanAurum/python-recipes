from difflib import SequenceMatcher

def get_similarity(a,b):
    '''
    returns the percentage of a that is the same as b
    '''
    return SequenceMatcher(a,b).ratio()    