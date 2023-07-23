users = ['Dave', 'John' , 'Sara']

data = ['Dave', 42 , True]

emptyList = []


print("Dave" in emptyList)

print(users[0])
# last value in the last
print(users[-1])

print(users.index('Sara'))

print(users[0:2])
print(users[-3: -1])

print( "length: ", len(data))


users.append("Elsa")
print(users)

users += ['Jason']

print(users)

users.extend(['Robert', 'Jim'])

print(users)


users.insert(0 , 'Bob')

print(users)



users[2:2] = ['Eddie', 'Alex']

print(users)

#  replaced list items

users[1:3] = ['robert' , 'JPJ']

print(users)



users.remove('Bob')

print(users)

print(users.pop()) 

print(users)

# delete users
del users[0]

print(users)


#del data

# clear data
data.clear()

print(data)

users[1:2] = ['dave']

users.sort()
print(users)

users.sort(key=str.lower)
print(users)


nums = [4,42,78, 1, 5]

nums.reverse()

print(nums)

# dscending order sort
# nums.sort(reverse=True)

# print(nums)

# sorting without modifying the list using global sorted function

print(sorted(nums, reverse=True ))
print(nums)

# copying methods

numscopy = nums.copy()

mynums = list(nums)

mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Salekin" , True])

print(mylist)


# Tuples

myTuple = tuple(('Dave', 42, True))

anotherTuple = (1,4,2,8)

print(myTuple)
print(type(myTuple))
print(type(anotherTuple))


newList = list(myTuple)

newList.append('Neil')

newTuple = tuple(newList)

print(newTuple)


(one , *two, hey ) = anotherTuple

print(one)
print(two)
print(hey)


print(anotherTuple.count(4))
