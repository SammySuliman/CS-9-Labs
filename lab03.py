def multiply(x,y):
    if y <= 0:
        return 0
    else:
        return multiply(x, y-1) + x

def reverseString(s):
    s2 = s
    if len(s) <= 1:
        return s
    else:
        return reverseString(s[1:]) + s[0]

def collectOddValues(listOfInt):
    if len(listOfInt) == 0:
        return []
    if len(listOfInt) == 1:
        if listOfInt[0] % 2 != 0:
            return listOfInt
        else:
            return []
    else:
        if listOfInt[0] % 2 != 0:
            return listOfInt[0:1] + collectOddValues(listOfInt[1:])
        else:
            return collectOddValues(listOfInt[1:])

def countInts(listOfInt, num):
    if len(listOfInt) == 0:
        return 0
    if len(listOfInt) == 1:
        if listOfInt[0] == num:
            return 1 
        else:
            return 0
    else:
        if listOfInt[0] == num:
            return countInts(listOfInt[1:], num) + 1 
        else:
            return countInts(listOfInt[1:], num) 

def removeSubString(s, sub):
    if len(s) == 0:
        return ''
    else:
        if sub[0] == s[0]:
            if s.find(sub) == 0:
                return removeSubString(s[len(sub):], sub)
            else:
                return s[0] + removeSubString(s[1:], sub)
        else:
            return s[0] + removeSubString(s[1:], sub)
