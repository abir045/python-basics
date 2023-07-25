from functools import reduce
def sqaured(num): return num * num

# lambda num : num * num


print(sqaured(2))


def addTwo(num): return num + 2
# lambda num : num + 2


print(addTwo(12))


def sum_Total(a, b): return a + b
# lambda a, b : a + b


print(sum_Total(10, 8))


#######################


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)

addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


###################

# higher order functions
# map

numbers = [1, 45, 6, 78, 3]


sqaured_nums = map(lambda num: num * num, numbers)


print(list(sqaured_nums))


#################
# filter

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))


################
# reduce

numbers_reduce = [1, 2, 3, 4, 5, 1]


total = reduce(lambda acc, curr: acc + curr, numbers_reduce, 10)

print(total)

print(sum(numbers_reduce, 10))

lambda acc, curr: acc + len(curr)


names = ["salekin", "Imran", "Paban", "Rubab"]


char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)


print("char count", char_count)
