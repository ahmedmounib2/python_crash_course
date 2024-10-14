# looping through a dictionary
# You can loop through all of a dictionary’s key-value pairs, through its
# keys, or through its values.
#
# (looping through all key-values)

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")
# The second half of the for statement includes the name of the
# dictionary followed by the method items(), which returns a list of key-value
# pairs. The for loop then assigns each of these pairs to the two variables
# provided.

favorite_languages= {
    'ahmed': 'python',
    'ola': 'c',
    'khaled': 'english',
    'susu': 'ruby',
    }


for name, language in favorite_languages.items():
    print(f"{name.title()} favorite language is {language.title()}\n")

# looping through all keys in a dictionary (useful when you don’t need to work with all of the
# values in a dictionary)

best_languages= {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'arabic',
    }

for name in best_languages.keys(): # its also same as when your write (for name in best_languages), as looping through keys is the default with python
    print(name.title())

friends = ['phil', 'sarah']

for name in best_languages:
    if name in friends:
        print(f"\n{name.title()} i see you prefer {best_languages[name]}\n")
    else:
        print(f"Hi {name}")

# You can also use the keys() method to find out if a particular person was
# polled. This time, let’s find out if Erin took the poll:

if 'erin' not in best_languages.keys(): # will work the same as (if 'erin' not in best_languages)
    print('erin, please take the poll')

# Looping Through a Dictionary’s Keys in a Particular
# Order

for name in sorted(best_languages):
    print(f"thank you {name.title()}, for taking the poll, now we know your preffered language is {best_languages[name]}")

# looping through all values in a dictionary
# we can use the values() method if we are primarily interested in the values in a dictionary

favorite_languages = {
    'jen': 'english',
    'sarah': 'spanish',
    'edward': 'english',
    'phil': 'french',
    'farida': 'english'
    }

print("the following languages has been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# this approach pulls all the values without checking for duplicates
# to remove duplicates we can use a set, A set is a collection were each item must be unique:

print("\nthe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items.

#You can build a set directly using braces and separating the elements with commas:
# t’s easy to mistake sets for dictionaries because they’re both wrapped in
# braces. When you see braces but no key-value pairs, you’re probably looking at a
# set. Unlike lists and dictionaries, sets do not retain items in any specific order.

