import itertools as it

def generate_anagrams(string):
    '''Takes a string a returns all the anagrams of the string
    '''
    return  [''.join(w) for w in list(it.permutations(string))]

