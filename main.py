MAX_TRIES = 6
HANGMAN_ASCII_ART = """
Welcome to the game Hangman \n
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""
picture_1 = """
picture 1:
    x-------x
"""
picture_2 = """
picture 2:
    x-------x
    |
    |
    |
    |
    |
"""
picture_3 = """
picture 3:
    x-------x
    |       |
    |       0
    |
    |
    |
"""
picture_4 = """
picture 4:
    x-------x
    |       |
    |       0
    |       |
    |
    |
"""
picture_5 = """
picture 5:
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |
"""
picture_6 = """
picture 6:
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |
"""
picture_7 = """
picture 7:
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |
"""
#print(HANGMAN_ASCII_ART, MAX_TRIES)
#word = input("enter a word: ")
#print('_ '*len(word))

guess_letter = input("Guess a letter: ")


def is_valid_input(letter_guessed):
    """
    this function checks if the letter guessed is valid
    for my game: the letter must be one letter
    in english only.
    :param letter_guessed: the letter guested from the user
    :type: string
    :return: returns if the letter is valid (True or False).
    :rtype: bool
    """
    if len(letter_guessed) > 1 or not(letter_guessed.isalpha()):
        return False
    elif len(letter_guessed) == 1 and letter_guessed.isalpha():
        return True
