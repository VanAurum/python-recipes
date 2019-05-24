def flatten(matrix):
    '''
    Takes in an n-dimensional array and flattens it into a single list
    '''
    return [elem for sublist in matrix for elem in sublist]