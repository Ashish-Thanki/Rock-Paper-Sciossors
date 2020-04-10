import random
import sys
from time import sleep

win = 0
loss = 0
tie = 0
games = 0
weapons = {"P", "R", "S"}

while True and games < 3:
    user_input = input("You are playing Rock, Paper and Scissors, enter your weapon (R), (P) or (S) - (Quit): ")

    while True:
        if user_input in weapons:
            if user_input == "P":
                print("You picked Paper")
                break
            if user_input == "R":
                print("You picked Rock")
                break
            if user_input == "S":
                print("You picked Scissors")
                break
        if user_input == "Quit":
            sys.exit()
        else:
            user_input = input("No, Type either Quit, R, P or S: ")
    sleep(1.5)
    computer_chose = random.choice(["P", "R", "S"])
    if computer_chose == "R":
        print("Computer chose Rock")
    elif computer_chose == "P":
        print("Computer chose Paper")
    elif computer_chose == "S":
        print("Computer chose Scissors")
    sleep(1.5)
    if computer_chose == user_input:
        tie += 1
        print("That's a draw")
    elif computer_chose == "S" and user_input == "R":
        win +=1
        print("That's a win for you")
    elif computer_chose == "S" and user_input == "P":
        loss +=1
        print("Computer wins that one!")
    elif computer_chose == "R" and user_input == "S":
        loss +=1
        print("Computer wins that one!")
    elif computer_chose == "R" and user_input == "P":
        win += 1
        print("You win that one!")
    elif computer_chose == "P" and user_input == "R":
        loss +=1
        print("Computer wins that one!")
    elif computer_chose == "P" and user_input == "S":
        win +=1
        print("Computer wins that one!")

    sleep(1.5)
    games += 1
    if games < 3:
        print("You have played %s games so far." % games)
    sleep(1.5)
    if games == 3:
        if win > loss:
            print("WELL DONE, You WON the game!!!!")
        if loss > win:
            print("UNLUCKY, You LOSE the game!!!")
        if win == loss:
            print("It WAS A DRAW, PLAY THE GAME AGAIN")
        sleep(1.5)
        print("You won %s, lost %s and drew %s." % (win, loss, tie))