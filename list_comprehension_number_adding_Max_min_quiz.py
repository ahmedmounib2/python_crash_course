#slicing a list, to work with part of a big list
players=['charles', 'mohamed','farida','ahmed','morsy', 'rasha']
print(players[0:3]) #this is how you slice to do an action for a part of the list
print(players[1:4])
print(players[:4]) #if you omit the first index in a slice, python starts the slice at the beginning of the list
print(players[2:]) # if you omit the last index, python prints from the 1st index to the end of the list
print(players[-3:]) #to print the last 3 values in a list
#looping through a slice
print('here are the 1st 3 players in the team')
for player in players [:3]:
    print(player.title())
#copying a list
my_food= ['pizza','kofta','spinach','pasta','lahma']
friend_food = my_food[:] #copying a list with [:]
print('my favorite foods are:')  #adding different items to each list to prove they are too different lists
print(my_food)
print('\n my friend favorite food are:')
print(friend_food)
my_food.append('cannoloni')
friend_food.append('molokhya')
print('my favorite foods are:')
print(my_food)
print('\n my friends favorite foods are:')
print(friend_food)
