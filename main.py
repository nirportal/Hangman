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


def show_hidden_word(secret_word, old_letters_guessed):
    """
    the function shows how much progress the user did so far
    :param secret_word: the word the user needs to guess
    :param old_letters_guessed: a list of user input of letters
    :type: str
    :type: list
    :return: the string format for showing how much the user progressed
    :rtype: str
    """
    b_string = ''
    for item in secret_word:
        if item in old_letters_guessed:
            b_string += item + " "
        else:
            b_string += "_ "
    return b_string[:-1]


def check_win(secret_word, old_letters_guessed):
    """
    checks if the user have won or not
    :param secret_word: the word the user needs to guess
    :param old_letters_guessed: the user letters guessed
    :type: str
    :type: list
    :return: True if the player won
    False if the player lost
    :rtype: bool
    """
    return " ".join(secret_word) == show_hidden_word(secret_word, old_letters_guessed)


secret_word = "friends"
old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
print(check_win(secret_word, old_letters_guessed))
secret_word = "yes"
old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
print(check_win(secret_word, old_letters_guessed))

#data = ("self", "py", 1.543)
#format_string = "Hello %s.%s learner, you have only %.1f units left before" \
#                " you master the course!"
#print(format_string % data)

