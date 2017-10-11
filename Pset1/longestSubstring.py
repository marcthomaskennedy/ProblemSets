# This program finds the longest alphbetical substring.

def longestAlphaSubStr(s):
    '''(str) => str raisesAssertionError
    Returns the longest alphabetical substring in s
    >>> longestAlphaSubStr("azcbobobegghakl")
    'beggh'
    '''
    # Helper functions
    def isLongestStr(currentStr, longestStr):
        '''(str, str) => bool
        Returns True if currentStr >= longestStr and currentStr length > 1.
        False otherwise.
        '''
        if len(currentStr) >= len(longestStr) and len(currentStr) != 1:
            return True
        return False

    def isAlphabetical(previousStr, nextStr):
        '''(str, str) => bool
        Returns True if previousStr and nextStr are in alphabetical order.
        False otherwise.
        '''
        if nextStr >= previousStr:
            return True
        return False

    # Check that the parameter is the correct data type.
    assert type(s) == str, "Parameter s must be a string."

    # If s is the empty string or a single character return s as we are done.
    if len(s) == 0 or len(s) == 1:
        return s

    currentStr = "" # Current alphabetical string
    longestStr = s[0] # Longest alphabetical string so far

    for i in range(1, len(s)):
        if isAlphabetical(s[i - 1], s[i]):
            if i == 1:
                # Add this character to the first character of s
                currentStr = longestStr + s[i]
            else:
                currentStr += s[i]
        else:
            if isLongestStr(currentStr, longestStr):
                longestStr = currentStr
            # Set to the current character of s and start again
            currentStr = s[i]

    # Last check to make sure that currentStr is not >= longestStr
    if isLongestStr(currentStr, longestStr):
        longestStr = currentStr

    return longestStr


def testLongestAlphaSubStr():
    assert longestAlphaSubStr("") == "", "It should return the empty string"
    assert longestAlphaSubStr("g") == "g", "It should return 'g'"
    assert longestAlphaSubStr("ab") == "ab", "It should return 'ab'"
    assert longestAlphaSubStr("ba") == "b", "It should return 'b'"
    assert longestAlphaSubStr("abcbcd") == "bcd", "It should return 'bcd'"
    assert longestAlphaSubStr("cdeabar") == "cde", "It should return 'cde'"
    assert longestAlphaSubStr("cdeabxr") == "abx", "It should return 'abx'"
    assert longestAlphaSubStr("cdeabxrstu") == "rstu", "It should return 'rstu'"
    assert longestAlphaSubStr("abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz", "It should return 'abcdefghijklmnopqrstuvwxyz'"
    assert longestAlphaSubStr("zyxwvutsrqponmlkjihgfedcba") == "z", "It should return 'zyxwvutsrqponmlkjihgfedcba'"
    print("longestAlphaSubStr() - All tests pass!")

# Main program
testLongestAlphaSubStr()
s = "azcbobobegghakl"
print("Longest substring in alphabetical order is:", longestAlphaSubStr(s))
