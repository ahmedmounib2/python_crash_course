
# Working with Multiple Files
# Let’s add more books to analyze. But before we do, let’s move the bulk of
# this program to a function called count_words(). By doing so, it will be easier to
# run the analysis for multiple books:

def count_word(filename):
    """read the number of words in a file"""
    try:
        with open(filename, encoding= 'utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"{filename} doesnot exist")
    else:
        words = content.split()
        words_num = len(words)
        print(words_num)

filename = 'alice.txt'

count_word(filename)


filenames = [ 'programming.txt','dictionaries.txt', 'alice.txt','lino.txt']

for filename in filenames:
    count_word(filename)

# Failing Silently
# In the previous example, we informed our users that one of the files was
# unavailable. But you don’t need to report every exception you catch.
# Sometimes you’ll want the program to fail silently when an exception occurs
# and continue on as if nothing happened. To make a program fail silently,
# you write a try block as usual, but you explicitly tell Python to do nothing in
# the except block. Python has a pass statement that tells it to do nothing in a
# block:

