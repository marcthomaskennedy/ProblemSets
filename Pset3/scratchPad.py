def isWordGuessed(secretWord, lettersGuessed):
    lettersGuessedCopy = lettersGuessed[:]
    isGuessed = ""
    print(lettersGuessedCopy)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            isGuessed += lettersGuessedCopy.pop(i)
            print(lettersGuessedCopy)
    print("WORD:", secretWord)
    print("GUESS:", isGuessed)

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
    print("isWordGuessed() - All tests pass!")

# Main program
#testIsWordGuessed()
secretWord = "apple"
lettersGuessed = ['p', 'e', 'i', 'a', 'k', 'r', 's', 'l']
print(isWordGuessed(secretWord, lettersGuessed))
