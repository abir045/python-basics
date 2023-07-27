
import os
# r = read
# a = append
# w = write
# x = create

# read - error if iit does not exist"


f = open("names.txt")

# print(f.read())
# print(f.read(4))
# print(f.read())

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = f.open("name_list.txt")
    print(f.read())

except:
    print("the file you want to read that doesn't exist")

finally:
    f.close()

# Append - create the file if it doesn't exist


f = open("names.txt", "a")
f.write('Neil\n')
f.close

f = open("names.txt")
print(f.read())
f.close()


# write (over write)

f = open("context.txt", "w")
f.write(" I deleted all the context")
f.close()


f = open("context.txt")
print(f.read())
f.close()


# two ways to create a new file

# opens a file for writing, creates the file if that does not exist


f = open("name_list.txt", "w")
f.close()

# create the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()


# delete a file


# avoid an error if it doesn't exist

if os.path.exists("dave.txt"):

    os.remove("dave.txt")
else:
    print("the file you wish to delete does not exist")


with open("moreNames.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
