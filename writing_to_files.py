# writing to an empty file:

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("i love programming.\n")
    file_object.write("i love creating new games.\n")

# appending to a file:

filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write('i also love finding meaning in large data sets.\n')
    file_object.write('i love creating apps that can run in a browser.\n')
