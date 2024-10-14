# dictionary example 1
# Let’s track the position of an alien that
# can move at different speeds. We’ll store a value representing the alien’s
# current speed and then use it to determine how far to the right the alien
# should move:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'original position: {alien_0['x_position']}')

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'new position is {alien_0['x_position']}')

# removing key value pairs in a dectionary with del statements

alien_0 = {'color': 'green', 'points':5}
print(alien_0)

del alien_0['points']

print(alien_0)

# a dictionary to store one kind of information about many objects as below
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


language= favorite_languages['sarah'].title()
print(f"Sarah's favorite language is  {language}.")


alien_0 = {'color': 'green', 'speed': 'slow'}
# using get () method to get a value from a dictionary will allow you to get another
# message if the key doesnt exist
# The get() method requires a key as a first argument. As a second optional
# argument, you can pass the value to be returned if the key doesn’t exist:
point_value= alien_0.get('points', 'no points value assigned')
print(point_value)
# if there is a chance the key doesnt exist is better to use the get method to avoid errors

# addint new key values to the dectionary

alien_0['x_position'] = 0
alien_0['y_position'] = 251
print(alien_0)


# starting with an empty dictionary and then adding values to it
favorite_books = {}

favorite_books['book 1'] = 'Quraan'
favorite_books['book 2'] = 'Game of thrones'
print(favorite_books)