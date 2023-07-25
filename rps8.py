# value = input('please input a value:\n')

import sys
import random
from enum import Enum


def rps(name='playerOne'):

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):

            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerChoice = input(
            f"\n{name} Enter ... \n1 for Rock, \n2 for paper, \n3 for Scissors:n\n\ ")

        if playerChoice not in ["1", "2", "3"]:
            print(f"{name} you must enter 1,2 or 3")
            return play_rps()

        player = int(playerChoice)

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print(
            f"\n {name} You choose  {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"python  choose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉{name}, you win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉{name}, you win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉{name}, you win"
            elif player == computer:
                return ("😲Tie game!")
            else:
                python_wins += 1
                return f" 🐍 Python wins!, \nSorry {name}...😢"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count:  {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay agian, {name}?")

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
            sys.exit(f"Bye {name}! 👋")

    return play_rps
    # break


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience "
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to playing the game"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
