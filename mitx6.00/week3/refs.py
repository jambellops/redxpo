def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    temp = 0
    key = ''
    for i in aDict:
        if (len(aDict[i]) > temp):
            key = i
            temp = len(aDict[i])
    return key
    
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    valList = []
    for i in aDict:
        valList += aDict[i]
    return len(valList)
