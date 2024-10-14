with open('message.txt') as file_object:
    content = file_object.read()
print(content)

with open('pi text.txt') as file_object:
    content= file_object.read()
print(content.rstrip())

# opening a file inside the file where our project is as below:
with open('text files/ahmed medhat.txt') as file_object:
    content = file_object.read()

print(content)

# using absolute path to open a file anywhere in the computer:
# Absolute paths are usually longer than relative paths, so it’s helpful to
# assign them to a variable and then pass that variable to open():

file_path = 'c:/Users/Admin/OneDrive/Desktop/files/favorite song.txt'
with open(file_path) as file_object:
    content = file_object.read()
print(content)

# NOTE
# If you try to use backslashes in a file path, you’ll get an error because the
# backslash is used to escape characters in strings. For example, in the path
# "C:\path\to\file.txt", the sequence \t is interpreted as a tab. If you need to use
# backslashes, you can escape each one in the path, like this:
# "C:\\path\\to\\file.txt".

filename = 'pi text.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
# rstrip remove the blank line so the output is same as the one inside file

# outside the with block, you can store the file’s lines in a list inside the block
# and then work with that list. You can process parts of the file immediately
# and postpone some processing for later in the program.
# The following example stores the lines of pi_digits.txt in a list inside the
# with block and then prints the lines outside the with block

filename = 'pi text.txt'
with open(filename) as file_object:
    lines= file_object.readlines()

for line in lines:
    print(line.rstrip())

# the readlines() method takes each line from the file and stores it in a
# list. This list is then assigned to lines, which we can continue to work with
# after the with block ends.
print(lines)

filename = 'pi text.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# page 260

file_path = 'C:/Users/Admin/OneDrive/Desktop/files/pi to 1 million.txt'
with open(file_path) as file_object:
    lines = file_object.read()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print(f"your birthday appear in the 1st million digits of pi")
else:
    print(f"your birthday doesnot appear in the 1st 1 million digits of pi")
