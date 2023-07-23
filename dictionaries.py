# Dicktionaries

band = {
    "vocals": "Plant",
    "guitar": "page",

}


band2 = dict(vocals="Plant", guitar="Page")


print(band)
print(band2)
print(type(band))
print(len(band))

# access items
print(band["vocals"])
print(band.get("guitar"))


# list all keys

print(band.keys())


# list all values

print(band.values())

# list of key value pairs as tuples

print(band.items())


# verify a key exists


print("guitar" in band)
print("triangle" in band)


# change values
band["vocals"] = "Coverdale"

band.update({"bass": "JPG"})

print(band)

# remove items

print(band.pop("bass"))

print(band)


band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple

print(band)


# delete and clear


band["drums"] = "Bonham"

del band["drums"]

print(band)

band2.clear()

print(band2)

del band2


# copy dictionaries


band2 = band  # creates a reference

# print("Bad copy")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()

band2["drums"] = "dave"

print("good copy")
print(band)
print(band2)


# or use the dictionary constructor function

band3 = dict(band)

print("good copy")
print(band3)


# Nested dictionaries

memeber1 = {
    "name": "plant",
    "instrument": "vocals"
}
memeber2 = {
    "name": "page",
    "instrument": "guitar"
}

band = {
    "member1": memeber1,
    "member2": memeber2
}

print(band)
print(band["member1"]["name"])


# Sets


nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))


print(nums)
print(nums2)
print(type(nums))
print(len(nums))


# no duplicates allowed in sets

nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero

nums = {1, True, 2, False, 3, 4, 0}
print(nums)


# check if a value is in a set

print(2 in nums)


# but you can not refer to an element in the set with an index position or key

# add a new element to a set


nums.add(8)

print(nums)

# add elements from one set to another

moreNums = {5, 6, 7}
nums.update(moreNums)


print(nums)

# you can use update with list, tuples  and dictionaries


# Merge two sets to create  a New set

one = {1, 2, 3}
two = {5, 6, 7}

myNewSet = one.union(two)

print(myNewSet)


# Keep only the duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)

print(one)


# Keep everything except the duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)

print(one)
