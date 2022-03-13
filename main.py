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
if len(guess_letter) > 1 and not guess_letter.isalpha():
    print("E3")
elif len(guess_letter) > 1:
    print("E1")
elif guess_letter.isalpha():
    print(guess_letter.lower())
elif not guess_letter.isalpha():
    print("E2")
