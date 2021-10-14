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

#


welcome()