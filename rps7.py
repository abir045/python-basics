# value = input('please input a value:\n')

import sys
import random
from enum import Enum


def rps():

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
            elif player == 2 and computer == 1:
                player_wins += 1
            elif player == 3 and computer == 2:
                player_wins += 1
            elif player == computer:
                return ("😲Tie game!")
            else:
                python_wins += 1

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame Count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

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

    return play_rps
    # break


rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()
