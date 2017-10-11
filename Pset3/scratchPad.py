def isWordGuessed(secretWord, lettersGuessed):
    isGuessed = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            isGuessed += letter

    if secretWord == isGuessed:
        return True
    return False

def testIsWordGuessed():
    assert isWordGuessed("apple", ['a', 'p', 'p', 'l', 'e']) == True,\
            "isWordGuessed should have returned True"
    assert isWordGuessed("apple", ['e', 'l', 'p', 'p', 'a']) == True,\
            "isWordGuessed should have returned True"
    assert isWordGuessed("apple", ['a', 'p', 'p', 'l', 'e', 'a']) == True,\
            "isWordGuessed should have returned True"
    assert isWordGuessed("apple", ['a', 'p', 'l', 'e']) == True,\
            "isWordGuessed should have returned True"
    assert isWordGuessed("apple", ['a', 'p', 'p', 'l', 'e', 'a', 'p', 'p', 'l']) == True,\
            "isWordGuessed should have returned True"
    assert isWordGuessed("apple", ['a', 'p', 'p', 'l', 'a']) == False,\
            "isWordGuessed should have returned False"
    assert isWordGuessed("apple", ['a', 'p', 'p', 'p', 'a']) == False,\
            "isWordGuessed should have returned False"
    assert isWordGuessed("apple", ['b', 'c', 'd', 'f', 'g']) == False,\
            "isWordGuessed should have returned False"
    assert isWordGuessed("apple", ['a', 'p', 'l', 'e', 'g']) == True,\
            "isWordGuessed should have returned True"
    print("isWordGuessed() - All tests pass!")

# Main program
testIsWordGuessed()
#secretWord = "apple"
#lettersGuessed = ['p', 'e', 'i', 'a', 'k', 'r', 's', 'l']
#print(isWordGuessed(secretWord, lettersGuessed))
