# closure is a function of having access to the scope of its parents

# function after the parent function has returned


def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if (coins > 1):
            print("\n" + person + " has " + str(coins) + " coins left ")

        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins ")

        else:
            print("\n" + person + " has " + str(coins) + " coins ")

    return play_game


tommy = parent_function("Tommy", 3)
jimmy = parent_function("jimmy", 5)

tommy()
tommy()
jimmy()
