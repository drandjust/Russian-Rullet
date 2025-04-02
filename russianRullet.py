import random
from time import sleep

# Print blank.
def blank():
    print("#"*25)

# Continue? Yes or no.
def confirm():
    for i in range(0, 10):
        confirm = input("Continue? [Y/N] : ")
        if confirm.upper() == "Y":
            break
        # When player enter 'N' over 4 times, print nahh man.
        if confirm.upper() == "N":
            if i < 4:
                print("You must play the game.")
            else:
                print("nahh man")
        # Please enter 'Y' or 'N'.
        else:
            if i < 4:
                print("Please try again.")
            else:
                print("Are you stupid?")

    # When player doesn't enter 'Y' over 10 times, just continue the game.
    print("Continue the game.")

# Guess the number.
def guess(diffculty):
    while True:
        print("Enter the number between 1 and "+str(diffculty)+".")
        userGuess = input("Enter: ")
        # Try transfer type.
        try:
            userGuess = int(userGuess)
            # Check range.
            if userGuess in range (1, diffculty+1):
                return userGuess
            else:
                print("Try again.")
        except ValueError:
            print("Try again.")

# number == userGuess, True or False.
def game(userGuess, number):
    if userGuess == int(number):
        print("player win.")
    else:
        print("CPU win.")
        sleep(1.5)
        print("os.rmdir")

# Main game.
def mainGame():
    # intro.
    blank()
    print("Let's play a game.")
    blank()
    sleep(1.5)
    print("Set diffculty.")

    # Set diffculty.
    # I wanted to make this roop a function.. But I can't.
    while True:
        print("Enter the number between 2 and 10.")
        diffculty = input("Enter: ")
        try:
            diffculty = int(diffculty)
            # Choose diffculty between 2 and 10.
            if diffculty in range (2, 11):
                break
            else:
                print("Try again.")
        except ValueError:
            print("Try again.")

    diffculty = int(diffculty)
    number = random.randrange(1,diffculty)

    # Debuger
    # print(number)

    userGuess = guess(diffculty)
    sleep(1.5)

    confirm()
    sleep(1.5)

    game(userGuess, number)
    sleep(1.5)
    blank()

# Start game.
while True:
    print("Enter Y to start.")
    print("Enter any key except Y to exit.")
    accept = input("Enter: ")

    if accept.upper() == "Y":
        mainGame()
    else:
        print("Exit the game . . .")
        sleep(2.5)
        break