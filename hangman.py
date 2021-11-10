# Problem Set 2, hangman.py
# Name: Sdobnikov Valerii
# Time spent: idk yet

DEBUG = True

#region Helper Code

import random
import string

WORDLIST_FILENAME = "words.txt"

ART = r''' _   _   ___   _   _ _____ ___  ___  ___   _   _ 
| | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
| |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
|  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
| | | || | | || |\  | |_\ \| |  | || | | || |\  |
\_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
                                                 
                                                 '''

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
        else: result += '_'
    return result




def get_available_letters(letters_guessed: list) -> str:
    #region
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    #endregion

    return ''.join([chr(i) for i in range(97,123) if chr(i) not in letters_guessed])
    
    

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
    print('\n\n' + ART + '\n\n')

    if(DEBUG): print(f'secret word is: {secret_word}')

    length = len(secret_word)
    print(f'Secret word is {length} letters long.')

    guesses = 6
    warnings = 3
    guessed_letters = []
    while guesses != 0:
        print('*' * 30)
        print(f'You have {guesses} guesses left and {3-warnings}/3 warnings.')
        print(f'Available letters: ', end = '')
        print(*list(get_available_letters(guessed_letters)), sep=',')
        guess = ''
        while True:
            guess = input('Please guess a letter: ').replace(' ', '').lower()
            if len(guess) != 1 or (not guess.isalpha()):
                warnings -= 1
                print(f'Entered data is not a letter! You now have {3-warnings}/3 warnings.')
                continue
            else:
                break

        if guess in [*secret_word]:
            guessed_letters.append(guess)
            print(f'Good guess: {get_guessed_word(secret_word, guessed_letters)}')
        else:
            print(f'Oops, you didn\'t guess: {get_guessed_word(secret_word, guessed_letters)}')
        if is_word_guessed(secret_word, guessed_letters): break
        guesses -= 1

    if is_word_guessed(secret_word, guessed_letters):
        print(f'{"*" * 30}\nCongratulations! You won!')
    else:
        print(f'{"*" * 30}\nMy condolences. You lost.')

def match_with_gaps(my_word: str, other_word: str) -> bool:
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
    pass



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
    pass



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
    pass


if __name__ == "__main__":

    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)