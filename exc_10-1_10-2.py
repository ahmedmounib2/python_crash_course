# exc 10-1 10-2
# 10-1. Learning Python: Open a blank file in your text editor and write a few lines
# summarizing what you’ve learned about Python so far. Start each line with the phrase In Python
# you can. . .. Save the file as learning_python.txt in the same directory as your exercises from this
# chapter. Write a program that reads the file and prints what you wrote three times. Print the
# contents once by reading in the entire file, once by looping over the file object, and once by
# storing the lines in a list and then working with them outside the with block.

file_path = 'C:\\Users\\Admin\\OneDrive\\Pictures\\Screenshots\\exc 10.txt'

with open(file_path) as file_object:
    lines = file_object.read()

print(lines.rstrip())

for x in range(3):
    print(f"\nbelow is the contents of the file 'exc 10':")
    print(lines.strip())

pi_string = ''
for line in lines:
    pi_string += line
print(f"\nlooping over the file:")
print(pi_string)


#

file_path = 'C:\\Users\\Admin\\OneDrive\\Pictures\\Screenshots\\exc 10.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

print(f"\nstored the file in a list with readlines() method")
print(lines)


message = 'i really like dogs'
new_message= message.replace('dog', 'cat')
print(new_message)
print(message.replace('dog','giraffes'))


for line in lines:
    print(line.replace('python','c'))

