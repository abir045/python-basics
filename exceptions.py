class JustNotCoolError(Exception):
    pass


x = 2

try:
    # print(x / 1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
    # raise Exception("I'm a custom exception!")
    raise JustNotCoolError("This just isn't cool man")

except NameError:
    print("NameError means something is probabely undefined")

except ZeroDivisionError:
    print('Please do not divide by zero')

except Exception as error:
    print(error)
else:
    print('No errors!')

finally:
    print("I'm going to print with or without an error")
