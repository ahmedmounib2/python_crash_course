# Storing data
# json to store data
# Using json.dump() and json.load()

# Let’s write a short program that stores a set of numbers and another
# program that reads these numbers back into memory. The first program will
# use json.dump() to store the set of numbers, and the second program will use
# json.load().

# The json.dump() function takes two arguments: a piece of data to store and
# a file object it can use to store the data. Here’s how you can use json.dump() to
# store a list of numbers:

import json
my_list = [1,2,5,63,25,41,0,58]

file_name= 'storingdata.json'

with open(file_name,'w') as file_object:
    json.dump(my_list,file_object)


# Now we’ll write a program that uses json.load() to read the list back into
# memory:

import json

file_name = 'storingdata.json'

with open(file_name) as file_object:
    list = json.load(file_object)

print(list)

# writing a program that ask users for their name, store it in json file

import json

username = input('whats is your name? ')

filname = 'userprogram.json'

with open(filname, 'w') as file_object:
    json.dump(username,file_object)


# writing a program that greets the users we saved from the previous program

import json

with open(filname) as f:
    json.load(f)
    print(f'welcome back {username}')
#####################################################################

import json
file_name = 'program.json'
try:
    with open(file_name) as f:
        json.load(f)
except FileNotFoundError:
    user = input('what is your name and age?')
    with open(file_name,'w') as f:
        json.dump(user,f)
        print('we will remember you when you come back')
else:
    print(f"welcome back {user}")
