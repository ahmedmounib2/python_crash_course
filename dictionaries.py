# Dectionaries
alien_0 = {'color': 'green','points': 5}
# dectionaries are defined by {}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'you just earned {new_points} points!')

# addint new key values to the dectionary

alien_0['x_position'] = 0
alien_0['y_position'] = 251
print(alien_0)


# starting with an empty dictionary and then adding values to it
favorite_books = {}

favorite_books['book 1'] = 'Quraan'
favorite_books['book 2'] = 'Game of thrones'
print(favorite_books)

# modifying items in a dictionary
# changing te alien color from green to yellow
alien_0 = {'color': 'green'}

print(alien_0['color'])

alien_0['color'] = 'yellow'

print(f'the alien is now {alien_0['color']}')
