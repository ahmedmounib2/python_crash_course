# Exceptions using try-except to deal with erros that might stop the program from running

try:
    print(5/0)
except ZeroDivisionError:
    print('you cant divide a number by 0')

print("Give me two numbers and i will divide them.")
print("enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('\nCant divide by 0')
    else:
        print('\n',first_number,'/',second_number,'=',answer)


filename= 'alice.txt'

try:
    with open(filename, encoding= 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'sorry, the {filename} doesnot exist')

# Analyzing Text
# The split() method separates a string into parts wherever it finds a space
# and stores all the parts of the string in a list

title = 'alice in wonder land'

print(title.split())

from pathlib import Path
path = 'alice.txt'
try:
    with open(path, encoding= 'utf-8') as f:
        content= f.read()
except FileNotFoundError:
    print(f"{path}, doesnt exist")

else:
    words = content.split()
    num_words = len(words)
    print(f"the {path} has about {num_words} words.")
