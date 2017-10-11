# This program counts the number of vowels in a string and displays the results
#to the user

def numberOfVowels(s):
    ''' (str) => int raises AssertionError
    Assumes that s is a str
    Returns the number of vowels in s ignoring capitalisation.
    >>> numberOfVowels("azcbObobegghAkl")
    5
    '''
    # Check parameter data type is correct
    assert type(s) == str, "s is not a string"

    # Helper functions
    def isVowel(l):
        vowels = ('a', 'e', 'i', 'o', 'u')
        if l in vowels:
            return True
        return False

    def countVowels(s):
        totalVowels = 0
        for letter in s.lower():
            if isVowel(letter):
                totalVowels += 1
        return totalVowels

    return countVowels(s)


def testCountVowels():
    # Empty str
    assert numberOfVowels("") == 0, "The number of vowels should be 0."
    # One character non-vowel
    assert numberOfVowels("b") == 0, "The number of vowels should be 0."
    # One character vowel
    assert numberOfVowels("a") == 1, "The number of vowels should be 1."
    # Multiple characters no vowels
    assert numberOfVowels("zcbbbgghkl") == 0, "The number of vowels should be 0."
    # Multiple characters all vowels
    assert numberOfVowels("aooea") == 5, "The number of vowels should be 5."
    # Multiple characters one vowel
    assert numberOfVowels("azcbbbgghkl") == 1, "The number of vowels should be 1."
    # Multiple characters multiple vowels
    assert numberOfVowels("azcbobobegghakl") == 5, "The number of vowels should be 5."
    # Multiple characters capital case Vowels
    assert numberOfVowels("azcbObobegghAkl") == 5, "The number of vowels should be 5."
    # Multiple characters capital case non-vowel
    assert numberOfVowels("aZcboBobeggHakl") == 5, "The number of vowels should be 5."
    # Multiple mixed case characters symbols and spaces
    assert numberOfVowels("The quicK BrOwn Fox jUmpEd Over The LAzY DOg!!! 12345") == 12, "The number of vowels should be 12."
    print("numberOfVowels() - All tests pass!")


# Main program
s = "azcbobobegghakl"
testCountVowels()
print("Number of vowels:", numberOfVowels(s))

try :
    print("Number of vowels:", numberOfVowels(1234))
except AssertionError:
    print("Oops! The argument passed to countVowels() is not a string.")
