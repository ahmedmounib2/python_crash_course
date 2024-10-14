# ex 10-10
# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few texts
# you’d like to analyze. Download the text files for these works, or copy the raw text from your
# browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase appears in a
# string. For example, the following code counts the number of times 'row' appears in a string:

filename = 'Moby Dick.txt'
with open(filename) as file_object:
    content= file_object.read()

words = content.split()
print(words.count('whale'))
print(content.lower().count('whale'))
print(len(words))


def count_the_then_there(filename):
    """count the times the word the, then and 'the ' showed up in a text file"""
    try:
        with open(filename) as file_object:
            content= file_object.read()
    except FileNotFoundError:
        print('The file doesnt exist')
    else:
        words = content.split()
        x = content.lower().count('the')
        y = content.lower().count('there')
        z = content.lower().count('the ')
        a = words.count('then')
        b = words.count('Then')
        print(f"\nthe word 'the' was typed in {filename}: {x} times")
        print(f"the word 'there' was typed in {filename}: {y} times")
        print(f"the word 'the ' was typed in {filename}: {z} times")
        print(f"the word 'then' was typed in {filename}: {a} times")
        print(f"the word 'Then' was typed in {filename}: {b} times")
        total = x + y + z + a + b
        print(f"the total numer 'the', 'there',the ', 'Then' and 'then' were typed is {total}")


count_the_then_there(filename)

file_two= 'hellobyeye.txt'

count_the_then_there(file_two)
