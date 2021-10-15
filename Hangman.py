import random

def welcome():
    "This functon welcomes the user and prompts him/her to enter his name  But makes sure he/she enters just letters and not numbers."
    while True:
        print("Welcome to Hangman Game!")
        print("Hi, please enter your name.")
        name = input(">>").capitalize()
        # Makes sure the user only enters letters
        if not name.isalpha():
            print("Numbers are not suppose to be in your name.")
            continue
        else:
            print(f"""Hi {name}. You will play against a computer.\nThe computer will randomly choose a word and you will have to try to guess the word.\nGood Luck!""" )
            break


def play_game():
    """This function asks the user if he/she wants to play the hangman game again"""

    print("Would like to play the game again? Enter 'Y' for Yes or 'N' for No.")
    response = input(">>").lower()

    if response == 'y':
        game_run()
    else:
        print("Thank you for playing the game!")

def get_word():
    """This function generates a random word from the list below"""

    words = ['car', 'phone', 'red', 'yellow', 'python', 'wheel']

    return random.choice(words).lower()