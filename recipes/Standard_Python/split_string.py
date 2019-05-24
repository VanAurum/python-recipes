def split_string(string,k):
    '''
    splits a given string into k equal parts given that k is a factor of len(string)
    '''
    return [string[i:i+k] for i in range(0, len(string), k)]    