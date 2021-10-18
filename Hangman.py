import random

def welcome():
    "This functon welcomes the user and prompts him/her to enter his name  But makes sure he/she enters just letters and not numbers."
    while True:
        print("""=============================================================================\n88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
             
             
===================================================================================""")
        print("Welcome to Hangman Game!")
        print("Hi, please enter your name.")
        name = input(">> ").capitalize()
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

    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()

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
    print("Guess the animal ;)")
    print(len(word) * '_  ')
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
            print(hangman(tries))
            print(status)

            if status == word:
                print("Great Job! You guessed the word correctly!")
                guessed = True
            elif tries == 0:
                print("Sorryyy! You have run out of guesses :(")
    play_again()

def hangman(tries):
    stages = [""" ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\\\
| |       // |   |  \\\\
| |      //  | . |   \\\\
| |     ')   |   |    (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \              
| |         `-' `-' 
""", 
"""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\\\
| |       // |   |  \\\\
| |      //  | . |   \\\\
| |     ')   |   |    (`
| |          ||'
| |          ||
| |          ||
| |          ||
| |         / |
            `-'     
""",

"""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\\\
| |       // |   |  \\\\
| |      //  | . |   \\\\
| |     ')   |   |    (`
| |          
| |          
| |          
| |          
| |     
""",
"""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y
| |       // |   | 
| |      //  | . | 
| |     ')   |   |   
| |          
| |         
| |          
| |          
| | 
""",
"""

 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |         Y . . Y
| |          |   | 
| |          | . |  
| |          |   |   
| |          
| |          
| |          
| |          
| |  
""",
"""


 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |       
| |       
| |      
| |    
| |          
| |          
| |          
| |          
| |  
""",
"""

 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         || 
| |          ||  
| |          (\\
| |         
| |        
| |       
| |      
| |     
| |          
| |          
| |          
| |          
| |        
"""
]
    return stages[tries]
game_run()
