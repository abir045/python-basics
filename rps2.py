# value = input('please input a value:\n')

import sys
import random
from enum import Enum


class RPS(Enum):

    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playAgain = True

while playAgain:

    playerChoice = input(
        "\n Enter ... \n1 for Rock, \n2 for paper, \n3 for Scissors:n\n\ ")

    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("you must enter 1, 2 or 3")

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("\nYou choose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("python  choose " + str(RPS(computer)).replace("RPS.", "") + ".\n")
    print("")

    if player == 1 and computerChoice == 3:
        print("🎉 you win!")
    elif player == 2 and computerChoice == 1:
        print("🎉 you win!")
    elif player == 3 and computerChoice == 2:
        print("🎉 you win!")
    elif player == computer:
        print("😲 Tie game")
    else:
        print("🐍 pyhton wins")

    playAgain = input("\nPlay agian? \nY for yes or \nQ to quit \n\n")

    if playAgain.lower() == "y":
        continue
    else:
        print("🎉🎉🎉 ")
        print("Thank you for playing\n")
        playAgain = False
# break

sys.exit("Bye! 👋")
