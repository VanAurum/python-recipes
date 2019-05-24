import itertools as it

def cartesian_product(somelists):
    '''
    Calculate the cartesian product of any number of lists. 
    'somelists' needs to be a list of lists
    '''
    return [element for element in it.product(*somelists)]