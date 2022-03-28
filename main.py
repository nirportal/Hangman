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


HANGMAN_PHOTOS = {"picture_1": """
    x-------x
    """, "picture_2": """
    x-------x
    |
    |
    |
    |
    |
    """, "picture_3": """
    x-------x
    |       |
    |       0
    |
    |
    |
    """, "picture_4": """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """, "picture_5": """
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |
    """, "picture_6": """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |
    """, "picture_7": """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |
    """}


def print_hangman(num_of_tries):
    global HANGMAN_PHOTOS
    if num_of_tries == 1:
        print(HANGMAN_PHOTOS["picture_1"])
    if num_of_tries == 2:
        print(HANGMAN_PHOTOS["picture_2"])
    if num_of_tries == 3:
        print(HANGMAN_PHOTOS["picture_3"])
    if num_of_tries == 4:
        print(HANGMAN_PHOTOS["picture_4"])
    if num_of_tries == 5:
        print(HANGMAN_PHOTOS["picture_5"])
    if num_of_tries == 6:
        print(HANGMAN_PHOTOS["picture_6"])
    if num_of_tries == 7:
        print(HANGMAN_PHOTOS["picture_7"])


num_of_tries = 6
print_hangman(num_of_tries)

'''8.32
from datetime import date


def age(birthdate):
    today = date.today()
    return today.year - int(birthdate[6:]) \
           - ((today.month, today.day) < (int(birthdate[3:5]), int(birthdate[:2])))


info_dict = {"first_name": "maria", "last_name": "Carey", "birth_date": "27.03.1970",
             "hobbies": ['Sing', 'Compose', 'Act']}
user_input = input("enter a number between 1 - 7: ")
if user_input == '1':
    print(info_dict["last_name"])
if user_input == '2':
    print(info_dict["birth_date"][3:5])
if user_input == '3':
    print(len(info_dict["hobbies"]))
if user_input == '4':
    print(info_dict["hobbies"][-1])
if user_input == '5':
    info_dict["hobbies"].append('Cooking')
if user_input == '6':
    info_dict["birth_date"] = ('27', '03', '1970')
    print(info_dict["birth_date"])
if user_input == '7':
    info_dict["age"] = age(info_dict["birth_date"])
    print(info_dict)

8.33    
def count_chars(my_str):
    new_dict = {}
    for char in my_str:
        if char != ' ':
            new_dict[char] = my_str.count(char)
    return new_dict


magic_str = "abra cadabra"
print(count_chars(magic_str))


8.34
def inverse_dict(my_dict):
    new_dict = {}
    for item in my_dict.keys():
        #print(new_dict)
        new_dict.setdefault(my_dict[item], [])
        new_dict[my_dict[item]].append(item)
    return new_dict


course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))
'''
