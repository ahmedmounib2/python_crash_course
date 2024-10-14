# Functions
# Def function

username = ['ahmed','khaled','ola']

def greet_user():
    """display a simple greeting"""
    print('Hello!')

def write_message(username):
    """write a message to tell everyone what i am learning in this chapter"""
    print(f'Hello {username}, i am learning about Def functions in this chapter.')

list = ['ahmed','khaled','ola']

for name in list:
    write_message(name.title())
write_message('joseph')
write_message('rauel')

def favorite_books(book):
    """write a message about your favorite book"""
    print(f"one of my favorite books is {book}")


books = ['Quran', 'shantaram','Annakarenina','the alchemist','game of thrones']

for book in books:
    favorite_books(book)
favorite_books(books[3])
favorite_books('shantaram')


def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog', 'bluffy')
describe_pet('hamster', 'harry')
describe_pet(pet_name='mestka',animal_type='monkey')

def make_shirt(tshirt_size,tshirt_textt):
    """enter tshirt size at tshirt_size, and text message to print on the shirt at tshirt_text"""
    print(f"\nTshirt size is {tshirt_size},\nThis message was printed on it: {tshirt_textt}")

make_shirt(42,'Fear and Loathing in Las Vegas')
make_shirt(tshirt_textt='Fear and Loathing in Las Vegas',tshirt_size= 28)
make_shirt(tshirt_textt='Chicago Bulls',tshirt_size= 32)

