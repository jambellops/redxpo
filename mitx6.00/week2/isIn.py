def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    mid = int((len(aStr))/2)
    if aStr == char:
#        print('aStr is char')
        return True
    elif aStr == '':
#        print('aStr is empty')
        return False
    elif len(aStr) == 1:
#        print('aStr is one letter and not char')
        return False
    elif aStr[mid] == char:
#        print('aStr mid is char')
#        print aStr[mid]
        return True
    else:
        if char < aStr[mid-1]:
#            print aStr[mid]
#            print char
            return isIn(char, aStr[0:mid-1])
        else:
#            print aStr[mid]
#            print char
            return isIn(char, aStr[mid:])
