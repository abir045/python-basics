def hello():
    print("Hello wolrd!")


hello()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return
    return (num1 + num2)


total = sum(7, 2)

print(total)


def multiple_items(*args):

    print(args)
    print(type(args))


multiple_items("dave", "john", "sara")


def multi_named_items(**kwargs):

    print(kwargs)
    print(type(kwargs))


multi_named_items(first="Dave",  last="Sara")
