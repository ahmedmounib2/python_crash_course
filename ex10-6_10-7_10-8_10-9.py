# exc 10-6 10-7
# 10-6. Addition: One common problem when prompting for numerical input occurs when
# people provide text instead of numbers. When you try to convert the input to an int, you’ll get
# a ValueError. Write a program that prompts for two numbers. Add them together and print
# the result. Catch the ValueError if either input value is not a number, and print a friendly error
# message. Test your program by entering two numbers and then by entering some text instead
# of a number.
# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user
# can continue entering numbers even if they make a mistake and enter text instead of a number.


while True:
    print(f"enter two digits and get the sum of them")

    first_number = input('First number: ')
    if first_number.lower() == 'q':
        break
    second_number = input('Second number: ')
    if second_number.lower() == 'q':
        break
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print('make sure you entered a number')
    else:
        print(first_number,'+',second_number,'=',result)


# exc 10-8
# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in
# the first file and three names of dogs in the second file. Write a program that tries to read these
# files and print the contents of the file to the screen. Wrap your code in a try-except block to
# catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the
# files to a different location on your system, and make sure the code in the except block
# executes properly

try:
    with open('cats.txt') as file_object:
        content = file_object.read()
        print(content)
except FileNotFoundError:
    print('No such file found')

def open_file(filename):
    """open a file"""
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print('\nno such file')
    else:
        print(content)

file= 'dogs.txt'

open_file(file)


# ex 10-9
# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if
# either file is missing.

try:
    with open('cats.txt') as file_object:
        content = file_object.read()
        print(content)
except FileNotFoundError:
    pass  #pass will make it fail without a message or error


def open_file_silently(filename):
    """open a file fail silently"""
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(content)

file = 'dogs.txt'
open_file_silently(file)

file = 'exct10_file.txt'
open_file_silently(file)

