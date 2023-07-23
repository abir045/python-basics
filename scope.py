name = "Dave"
count = 1

# local scope


def greeting(name):
    color = "blue"
    print(color)
    print(name)
    # print(firstName)


# greeting("John")

# modifying the global variable with the global keyword


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("Dave")


another()
