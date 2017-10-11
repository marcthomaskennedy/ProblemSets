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

#------------------------------------------------------------------------------

def getAvailableLetters(lettersGuessed):
    characters = "abcdefghijklmnopqrstuvwxyz"
    availableLetters = ""
    for character in characters:
        if character in lettersGuessed:
            continue
        else:
            availableLetters += character
    return availableLetters


def testGetAvailableLetters():
    assert getAvailableLetters(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == "", "It should return an empty string"
    assert getAvailableLetters([]) == "abcdefghijklmnopqrstuvwxyz",\
            "It should return the string 'bcdefghijklmnopqrstuvwxyz'"
    assert getAvailableLetters(['a']) == "bcdefghijklmnopqrstuvwxyz",\
            "It should return the string 'bcdefghijklmnopqrstuvwxyz'"
    assert getAvailableLetters(['z']) == "abcdefghijklmnopqrstuvwxy",\
            "It should return the string 'abcdefghijklmnopqrstuvwxy'"
    assert getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']) == \
            "abcdfghjlmnoqtuvwxyz", "It should return the string 'abcdfghjlmnoqtuvwxyz'"
    print("getAvailableLetters() - All tests pass!")

#------------------------------------------------------------------------------

def getGuessedWord(secretWord, lettersGuessed):
    guessedLetters = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedLetters += letter
        else:
            guessedLetters += "_"

    return guessedLetters


def testGetGuessedWord():
    assert getGuessedWord("apple", ['f', 'i', 'k', 'j', 'r', 's']) == "_____",\
            "It should return the strinng '_____'"
    assert getGuessedWord("apple", ['a', 'i', 'k', 'j', 'r', 's']) == "a____",\
            "It should return the strinng 'a____'"
    assert getGuessedWord("apple", ['e', 'i', 'k', 'j', 'r', 's']) == "____e",\
            "It should return the strinng '____e'"
    assert getGuessedWord("apple", ['f', 'p', 'k', 'j', 'r', 's']) == "_pp__",\
            "It should return the strinng '_pp__'"
    assert getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's']) == "_pp_e",\
            "It should return the strinng '_pp_e'"
    assert getGuessedWord("apple", ['e', 'l', 'k', 'p', 'a', 's']) == "apple",\
            "It should return the strinng 'apple'"
    print("getGuessedWord() - All tests pass!")

#------------------------------------------------------------------------------

# Main program
#testIsWordGuessed()
#testGetAvailableLetters()
testGetGuessedWord()
#secretWord = "apple"
#lettersGuessed = ['p', 'e', 'i', 'a', 'k', 'r', 's', 'l']
#print(isWordGuessed(secretWord, lettersGuessed))
