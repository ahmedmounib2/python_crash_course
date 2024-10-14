favorite_food= ['pizza','burger','pasta','bread','fish','meat']
print('the first 3 items in the favorite food are:')
print(favorite_food[0:3])
print('\nthe last three items in the list are:')
print(favorite_food[-3:])
you_favorite_food= favorite_food[:]
favorite_food.append('hawashi')
you_favorite_food.append('koshary')
print('\n my favorite foods are:')
for value in favorite_food:
    print(value)
print('\n you favorite foods are:')
for value in you_favorite_food:
    print(value)
