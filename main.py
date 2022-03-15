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

#guess_letter = input("Guess a letter: ")


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    this function checks if the letter guessed is valid
    for my game: the letter must be one letter
    in english only and the user didn't already guess it before.
    the old_letters_guessed list.
    :param: letter_guessed: the letter guested from the user
    :param: old_letters_guessed: a list of the letters
    already guested
    :type: string
    :type: list
    :return: returns if the letter is valid
    :rtype: bool
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() \
           and letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    the function checks if the letter guessed is valid
    :param: letter_guessed: the user input
    :param: old_letters_guessed: the user old letters input
    :type: string
    :type: list
    :return: if True - it adds it to the old letters list, return True
    if False - prints X and the list sorted by size and lowered case
    with a -> between each value in the list, returns False
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        sorted(old_letters_guessed)
        print(organize_list_as_string(old_letters_guessed))
        return False


def organize_list_as_string(old_letters_guessed):
    """
    organizes a list to a certain format: a sorted list
    and a -> between each value:
    a -> b -> c
    :param: old_letters_guessed: the old letters the user inputted
    :type: list
    :return: the new formatted string
    :rtype: string
    """
    new_string = " -> ".join(sorted(old_letters_guessed))
    return new_string


old_letters = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed('A', old_letters))
print(try_update_letter_guessed('s', old_letters))
print(try_update_letter_guessed('$', old_letters))
print(try_update_letter_guessed('d', old_letters))
