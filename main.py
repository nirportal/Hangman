from os.path import exists as file_exists


num_of_tries = 6


def start_screen():
    """
    this func prints the start screen:
    the hangman bug assci and the amount of tries the player has.
    :return: none
    """
    HANGMAN_ASCCI_ART = r"""
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
    print(HANGMAN_ASCCI_ART, num_of_tries)


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
        print("incorrect input or you already guessed that letter" + "\n"
              "please try to enter a new letter!")
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
    return "the letters you already guessed: " +\
           " -> ".join(sorted(old_letters_guessed))


def show_hidden_word(secret_word, old_letters_guessed):
    """
    the function shows how much progress the user did so far
    :param secret_word: the word the user needs to guess
    :param old_letters_guessed: a list of user input of letters
    :type: str
    :type: list
    :return: the string format for showing how much the user progressed
    :rtype: prints str
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
    return " ".join(secret_word) == \
           show_hidden_word(secret_word, old_letters_guessed)


def print_hangman(current_tries):
    """
    this function prints the current state of
    the hangman.
    :param: current_tries: the number of liives the use has
    :type: int
    :return: none
    """
    HANGMAN_PHOTOS = {1: """
    x-------x
    """, 2: """
    x-------x
    |
    |
    |
    |
    |
    """, 3: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """, 4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """, 5: r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
    """, 6: r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
    """, 7: r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
    """}
    print(HANGMAN_PHOTOS[current_tries])


def choose_word(file_path, index):
    """
    the func chooses the secret word from the words file
    :param file_path: the word's file
    :param index: the index of the secret word from the file
    :type: str
    :type: int
    :return: returns the secret word
    :rtype str
    """
    file = open(file_path, "r").read()
    file_list = file.split()
    while index > len(file_list):
        index = index - len(file_list)
    secret_word = file_list[index - 1]
    return secret_word


def print_joke(hangman_photo_num):
    JOKES = {1: "now we have a nice hanging pillar :)",
             2: "hey look now theres a head!",
             3: "wowow where are my limbs???",
             4: "hoo, theres my hands :o",
             5: "I have one leg! better get the next one right!",
             6: "GG you really bad, im now ded :x"}
    print(JOKES[hangman_photo_num])


def check_if_right(secret_word, player_letter):
    """
    this func checks if the letter guessed is in the secret word
    if True: does nothing
    if False: prints amessege and the hangman with one more step
    :param secret_word: the secret word
    :param player_letter: the player input letter
    :type: str
    :type: str
    :return: none
    """
    global num_of_tries
    if not (player_letter in secret_word):
        print("letter not in the word\ntry again!")
        print_joke(7 - num_of_tries)
        num_of_tries = num_of_tries - 1
        print_hangman(7 - num_of_tries)


def check_user_input(input):
    """
    this func checks if the input of the index the user logged
    into the interperter is an int!
    :param: input: the player input
    :type: str
    :return: returns True if it's int, else returns False
    :rtype: bool
    """
    try:
        int(input)  # checks if int
        return True
    except ValueError:
        try:
            float(input)  # checks if float
            return False
        except ValueError:
            return False  # it's a string


def main():
    start_screen()
    file_path = input("enter a file path: ")
    while not file_exists(file_path):
        # C:\Users\nirpo\OneDrive\Documents\words.txt
        file_path = input("file not exists! enter a new file path: ")
    index = input("enter an index: ")
    while not check_user_input(index):
        index = input("you didn't enter a number, please enter an index: ")
    secret_word = choose_word(file_path, int(index))
    old_letters_guessed = []
    print_hangman(7 - num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries > 0:
        player_input = input("guess a letter: ")
        if try_update_letter_guessed(player_input, old_letters_guessed):
            check_if_right(secret_word, player_input)
            print(show_hidden_word(secret_word, old_letters_guessed))
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            break
    if not check_win(secret_word, old_letters_guessed):
        print("LOSE")


if __name__ == "__main__":
    main()
