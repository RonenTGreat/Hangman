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


def play_again():
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

def game_run():

    """This function starts the game play"""
    welcome()

    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    word = get_word()
    guessedLetters = []
    tries = 7;
    guessed = False
    print()
    print("The word is a ", len(word), "letter word.")
    print(len(word) * '_')
    while guessed == False and tries > 0:
        print("You have ", tries, "tries.")
        guess = input("Guess a letter in the word or enter the full word: \n").lower()

        if len(guess) == 1:
            if guess not in alphabet:
                print("You are yet to enter a letter. Check your entry, make sure you enter an alphabet not a number or a symbol.")
            elif guess in guessedLetters:
                print("You have already guessed that letter before. Try again!")
            elif guess not in word:
                print("Sorry, that letter is not part of the word.")
                guessedLetters.append(guess)
                tries -= 1
            elif guess in word:
                print("Nice, that letter exists in the word")
                guessedLetters.append(guess)
            else:
                print("Check your entry! You might made a mistake.")
                
        elif len(guess) == len(word):
            if guess == word:
                print("Wow! You guessed the word correctly.")
                guessed = True
            else:
                print("Sorry, that was not the word we were looking for.")
                tries -= 1
        else:
            print("The length of your guess is not the same as the length of the correct word.")
            tries -= 1
            
        status = ''
        if guessed == False:
            for letter in word:
                if letter in guessedLetters:
                    status += letter
                else:
                    status += '_'
            print(status)

            if status == word:
                print("Great Job! You guessed the word correctly!")
                guessed = True
            elif tries == 0:
                print("Sorryyy! You have run out of guesses :(")
    play_again()

game_run()
