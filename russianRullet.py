import random as ran
from time import sleep

# main game
# for print blank.
def blank():
    print("#"*25)

# continue? yes or no.
def confirm():
    for i in range(0, 10):
        confirm = input("계속 하겠는가? [Y/N] : ").upper()
        if confirm == "Y":
            break
        if confirm == "N":
            print("출구는 없습니다..")
            if i > 4:
                print("씨발 좀")
        else:
            print("Y 또는 N을 입력.")

    print("게임을 계속 진행합니다.")

# guess the number.
def guess(diffculty):
    while True:
        print("1 부터 "+str(diffculty)+" 사이의 정수를 입력하라.")
        userGuess = input("입력: ")
        try:
            userGuess = int(userGuess)
            if userGuess in range (1, diffculty+1):
                return userGuess
            else:
                print("다시 입력하라.")
        except ValueError:
            print("다시 입력하라.")

# number == userGuess True or False.
def game(userGuess, number):
    if userGuess == int(number):
        print("player의 승리.")
    else:
        print("CPU의 승리.")
        print("후, 이번만입니다...")

# main game.
def mainGame():
    blank()
    print("게임을 시작하지")
    blank()
    sleep(2.5)

    print("난이도를 선택하라.")

    # Set diffculty.
    # I wanted to make this roop a function.. But I can't.
    while True:
        print("2 부터 10 사이의 정수를 선택하라.")
        diffculty = input("입력: ")
        try:
            diffculty = int(diffculty)
            # U can choose diffculty between 2 and 10.
            if diffculty in range (2, 11):
                break
            else:
                print("다시 입력하라.")
        except ValueError:
            print("다시 입력하라.")

    diffculty = int(diffculty)
    number = ran.randrange(1,diffculty)

    # Debuger
    # print(number)

    blank()
    print("Russian Rullet")
    print("숫자를 틀리면 시스템이 초기화됩니다.")
    blank()
    sleep(2.5)

    userGuess = guess(diffculty)
    sleep(2.5)

    confirm()
    sleep(2.5)

    game(userGuess, number)
    sleep(2.5)

# start game. (Old version.)
# while True:
#     print("게임을 시작하려면 Y를, 아니면 아무 키를 입력하시오.")
#     accept = input("입력: ").upper()
#     if accept == "Y":
#         mainGame()
#     else:
#         break