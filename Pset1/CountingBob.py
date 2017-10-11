# This program counts the number of occurences of a word in a string.

def countWord(s, word, i = False):
    '''(str, str, [bool]) => int raises AssertionError
    Returns the number of occurences of word in s. Ignores case if i is True
    >>> countWord("azcbobobegghakl", "boB", True)
    2
    '''
    # Check parameter data types are correct
    assert type(s) == str, "parameter s must be str."
    assert type(word) == str, "parameter word must be str."
    assert type(i) == bool, "parameter i must be bool."

    # If word is an empty string just return 0 
    if len(word) == 0:
        return 0

    wordCount = 0
    
    # Convert s and word to lowercase versions if the i parameter is True
    if i:
        wordToFind = word.lower()
        strToSearch = s.lower()
    else:
        strToSearch = s
        wordToFind = word

    while strToSearch.find(wordToFind) != -1:
        wordCount += 1
        nextStartIndex = strToSearch.find(wordToFind)
        strToSearch = strToSearch[nextStartIndex + len(wordToFind) -1 :]

    return wordCount


def testCountWords():
    assert countWord("", "bob") == 0, "The word count should be 0."
    assert countWord("", "") == 0, "The word count should be 0."
    assert countWord("azcbobobegghakl", "") == 0, "The word count should be 0."
    # No occurences of word
    assert countWord("azcbobobegghakl", "ace") == 0, "The word count should be 0."
    # One occurence of word
    assert countWord("azcbobobegghakl", "beg") == 1, "The word count should be 1."
    # Two occurences of word
    assert countWord("azcbobobegghakl", "bob") == 2, "The word count should be 2."
    # Two occurences of word and ignore capitalisation
    assert countWord("azcbobobegghakl", "BoB", True) == 2, "The word count should be 2."
    # Two occurences of word and ignore capitalisation
    assert countWord("azcBobOBegghakl", "bob", True) == 2, "The word count should be 2."
    # Multiple occurences of word and ignore capitalisation
    assert countWord("BoBOboBoBOboBob", "bOb", True) == 7, "The word count should be 7."
    # Multiple occurences of word and ignore capitalisation and punctuation
    assert countWord("azcbobobegghakl bob b o bbob,!'b,o£b", "bOb", True) == 4, "The word count should be 4."
    print("countWord() - All tests pass!")


# Main program
s = "azcbobobegghakl"
w = "bob"
print("Number of times", w, "occurs is:", countWord(s, w))
testCountWords()

