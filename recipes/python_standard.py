#Standard python library imports
from difflib import SequenceMatcher, get_close_matches
from collections import OrderedDict, Counter
from operator import itemgetter
from datetime import datetime, timedelta
import math
import itertools as it



def get_combinations(iterable, n):
    '''Return all combinations from iterable of length n
    '''
    return list(it.combinations(iterable,n))


def generate_anagrams(string):
    '''Takes a string a returns all the anagrams of the string
    '''
    return  [''.join(w) for w in list(it.permutations(string))]


def get_similarity(a,b):
    '''
    returns the percentage of a that is the same as b
    '''
    return SequenceMatcher(a,b).ratio()    


def changes_to_same(s1, s2):
    '''
    Counts the number of changes required to make one string an anagram of another
    '''
    counter1=[0]*26  # Make array of 0's of length 26
    counter2=[0]*26

    for c in s1:
        counter1[ord(c)-ord('a')]+=1

    for c in s2:
        counter2[ord(c)-ord('a')]+=1

    ans=0    
    for i in range(26):
        ans+=abs(counter1[i]-counter2[i])

    return ans  


def flatten(matrix):
    '''
    Takes in an n-dimensional array and flattens it into a single list
    '''
    return [elem for sublist in matrix for elem in sublist]


def matrify(array):
    '''
    Accepts a flat array and converts to an n x n matrix if the length has a whole square root.
    '''
    n=int(math.sqrt((len(array))))
    return [[array.pop(0) for _ in range(n)] for _ in range(n)]


def split_string(string,k):
    '''
    splits a given string into k equal parts given that k is a factor of len(string)
    '''
    return [string[i:i+k] for i in range(0, len(string), k)]    


def remove_duplicates(string):
    '''
    Removes contiguous and non-contiguous duplicates from a string
    '''
    return ''.join(list(OrderedDict.fromkeys(string)))    


def remove_list_duplicates(lst):
    '''
    removes duplicates from list while preserving order of list.
    '''
    return list(OrderedDict.fromkeys(lst))


def get_n_most_common(iterable,n):
    '''
    Accepts an iterable and returns the n most common occurrences.
    '''
    return Counter(iterable).most_common(n)

def close_matches(word, possibilities, n=3, cutoff=0.6):
    '''
    Returns a list of close matches to word from the list possibilities.  
    '''
    return get_close_matches(word, possibilities, n, cutoff) 

def lowercase_list(string_list):
    '''
    Convert a list of strings to lower case
    '''
    return [x.lower() for x in string_list]


def uppercase_list(string_list):
    '''
    Convert a list of strings to upper case
    '''
    return [x.upper() for x in string_list]


def get_binary_elements(n):
    '''
    Get all binary values of length n.
    '''
    return [''.join(x) for x in list(it.product('01',repeat=n))]


def cartesian_product(somelists):
    '''
    Calculate the cartesian product of any number of lists. 
    'somelists' needs to be a list of lists
    '''
    return [element for element in it.product(*somelists)]


def strings_to_ints(string_list):
    '''
    Converts a list of strings to a list of integers:
    '''
    return list(map(int, string_list))


def all_elements_equal(my_list, check_val=None):
    '''
    Returns true of all elements in the list are equal to a provided value 
    or all the list elements are the same if no check value is provided.
    '''
    if check_val:
        return all(x==check_val for x in my_list)
    else:    
        return all(x==my_list[0] for x in my_list)


def any_elements_equal(my_list, check_val):
    '''
    Returns true if any value in the list equals the check value.
    '''
    return any(x==check_val for x in my_list)


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


if __name__=='__main__':
    
    print(get_similarity('abcde','abcd'))