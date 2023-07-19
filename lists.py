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




