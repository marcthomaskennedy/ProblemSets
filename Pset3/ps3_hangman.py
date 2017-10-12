# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    isGuessed = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            isGuessed += letter

    if secretWord == isGuessed:
        return True
    return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedLetters = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedLetters += letter
        else:
            guessedLetters += "_ "

    return guessedLetters



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    characters = "abcdefghijklmnopqrstuvwxyz"
    availableLetters = ""
    for character in characters:
        if character in lettersGuessed:
            continue
        else:
            availableLetters += character
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    # Helper functions
    def printDivider():
        '''() => None
        Prints some characters to seperate the programs output.
        >>> printDivider()

        -------------

        '''
        print("-------------")

    def printGreeting(secretWord):
        '''(str) => None
        Prints the welcome text of the game
        >>> printGreeting("tact")
        Welcome to the game, Hangman!
        I am thinking of a word that is 4 letters long.
        '''
        print("Welcome to the game, Hangman!")
        print("I am thinking of a word that is", len(secretWord), "letters long.")


    def getGuess():
        '''() => str
        Returns the character that the user has entered. Ignores case.
        >>> getGuess()
        Please guess a letter: a
        a
        '''
        guess = input("Please guess a letter: ")
        return guess.lower()


    # Main routine
    guessesRemaining = 8
    lettersGuessed = []
    guessedLetter = ""

    printGreeting(secretWord)
    printDivider()
    while guessesRemaining != 0:
        print("You have", guessesRemaining, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))

        guessedLetter = getGuess()

        if guessedLetter not in lettersGuessed and guessedLetter in secretWord:
            lettersGuessed.append(guessedLetter)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed):
                printDivider()
                break
            printDivider()
        elif guessedLetter not in secretWord:
            lettersGuessed.append(guessedLetter)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            printDivider()
            guessesRemaining -= 1
            continue
        elif guessedLetter in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            printDivider()
            continue

    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord + ".")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = "tact"
hangman(secretWord)
