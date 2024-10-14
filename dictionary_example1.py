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
