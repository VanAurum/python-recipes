
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