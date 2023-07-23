# value = input('please input a value:\n')

import sys
import random
from enum import Enum


game_count = 0


def play_rps():

    class RPS(Enum):

        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input(
        "\n Enter ... \n1 for Rock, \n2 for paper, \n3 for Scissors:n\n\ ")

    if playerChoice not in ["1", "2", "3"]:
        print("you must enter 1,2 or 3")
        return play_rps()

    player = int(playerChoice)

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("\nYou choose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("python  choose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return ("🎉 You win!")
        elif player == 2 and computer == 1:
            return "🎉you win!"
        elif player == 3 and computer == 2:
            return ("🎉you win!")
        elif player == computer:
            return ("😲Tie game!")
        else:
            return "🐍 pyhton wins"

    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    game_count += 1

    print("\nGame Count: " + str(game_count))

    print("\nPlay agian?")
    while True:

        playAgain = input("\nY for yes or \nQ to quit \n\n")
        if playAgain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playAgain.lower() == "y":
        return play_rps()
    else:
        print("🎉🎉🎉 ")
        print("Thank you for playing\n")
        sys.exit("Bye! 👋")
# break


play_rps()
