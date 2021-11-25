# Problem Set 2, hangman.py
# Name: Sdobnikov Valerii
# Time spent:

DEBUG = False

#region Helper Code

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words() -> list:
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



def choose_word(wordlist: list) -> str:
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

#endregion
wordlist = load_words()


def is_word_guessed(secret_word: str, letters_guessed: list) -> bool:
    #region
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    #endregion
    return set(letters_guessed) == set([*secret_word])



def get_guessed_word(secret_word: str, letters_guessed: list) -> str:
    #region
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    #endregion
    
    result = ''

    for i in secret_word:
        if i in letters_guessed:
            result += i
        else: result += '_ '
    return result



def get_available_letters(letters_guessed: list) -> str:
    #region
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    #endregion

    return ''.join([i for i in string.ascii_lowercase if i not in letters_guessed])
    
    

def hangman(secret_word: str):
    #region
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #endregion

    vowels = ['a','e','i','o','u']

    guesses = 6
    warnings = 3
    guessed_letters = []
    length = len(secret_word)

    if(DEBUG): print(f'secret word is: {secret_word}')

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {length} letters long.')   
    print(f'You have {warnings} warnings left.')

    # Main game cycle
    while not (guesses <= 0 or is_word_guessed(secret_word, guessed_letters)):

        print('-' * 11)
        print(f'You have {guesses} guesses left.')
        print(f'Available letters: {get_available_letters(guessed_letters)}')

        guess = input('Please guess a letter: ').replace(' ', '').lower()

        if len(guess) != 1 or (not guess.isalpha()) or (guess in guessed_letters):

            msg = 'You\'ve already guessed that letter.' if guess in guessed_letters else 'That is not a valid letter.'
            print(f'Oops! {msg} You have {warnings-1 if (warnings-1) > 0 else "no"} warnings left', end = '')

            if warnings > 0: warnings -= 1

            if warnings <= 0:
                print(f' So you lose one guess: {get_guessed_word(secret_word, guessed_letters)}')
                guesses -= 1
            else:
                print(f': {get_guessed_word(secret_word, guessed_letters)}')
            continue

            
        if guess in [*secret_word]:
            guessed_letters.append(guess)
            print(f'Good guess: {get_guessed_word(secret_word, guessed_letters)}')
        else:
            print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, guessed_letters)}')
            guesses -= 2 if guess in vowels else 1
        

    if is_word_guessed(secret_word, guessed_letters):
        score = len( set(secret_word) ) * guesses
        print(f'{"-" * 11}\nCongratulations, you won! Your total score for this game is: {score}')
    else:
        print(f'{"-" * 11}\nSorry, you ran out of guesses. The word was {secret_word}')



def match_with_gaps(my_word: str, other_word: str) -> bool:
    my_word = my_word.replace(' ', '')
    #region
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #endregion
    result = True
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] != '_': result = result and (my_word[i] == other_word[i])
    else:
        return False
    return result



def show_possible_matches(my_word: str) -> None:
    #region
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    #endregion
        
    possible_matches = [i for i in wordlist if match_with_gaps(my_word, i)]

    if(len(possible_matches) == 0):
        print("No matches found")
        return

    print('Possible word matches are: ')
    print(*possible_matches, sep=' ')



def hangman_with_hints(secret_word: str) -> None:
    #region
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #endregion

    vowels = ['a','e','i','o','u']

    guesses = 6
    warnings = 3
    guessed_letters = []
    length = len(secret_word)

    if(DEBUG): print(f'secret word is: {secret_word}')

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {length} letters long.')   
    print(f'You have {warnings} warnings left.')

    # Main game cycle
    while not (guesses <= 0 or is_word_guessed(secret_word, guessed_letters)):

        print('-' * 11)
        print(f'You have {guesses} guesses left.')
        print(f'Available letters: {get_available_letters(guessed_letters)}')

        guess = input('Please guess a letter: ').replace(' ', '').lower()
        
        if len(guess) != 1 or (not (guess == '*' or guess.isalpha())) or (guess in guessed_letters):

            msg = 'You\'ve already guessed that letter.' if guess in guessed_letters else 'That is not a valid letter.'
            print(f'Oops! {msg} You have {warnings-1 if (warnings-1) > 0 else "no"} warnings left', end = '')

            if warnings > 0: warnings -= 1

            if warnings <= 0:
                print(f' So you lose one guess: {get_guessed_word(secret_word, guessed_letters)}')
                guesses -= 1
            else:
                print(f': {get_guessed_word(secret_word, guessed_letters)}')
            continue
        
        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, guessed_letters))

        elif guess in [*secret_word]:
            guessed_letters.append(guess)
            print(f'Good guess: {get_guessed_word(secret_word, guessed_letters)}')
        else:
            print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, guessed_letters)}')
            guesses -= 2 if guess in vowels else 1
        

    if is_word_guessed(secret_word, guessed_letters):
        score = len( set(secret_word) ) * guesses
        print(f'{"-" * 11}\nCongratulations, you won! Your total score for this game is: {score}')
    else:
        print(f'{"-" * 11}\nSorry, you ran out of guesses. The word was {secret_word}')



if __name__ == "__main__":

    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)