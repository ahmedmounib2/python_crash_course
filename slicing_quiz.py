# Tuples are lists with items that never change , its the same as a list but it starts with parenthes () instead of square brackets []
dimensions= (200,50)
print(dimensions[0])
print(dimensions[1])
# tuples must be defined with a comma
x= (3,) #this is how you define x as a tuple having 1 value
for dimension in dimensions:  #using for loops with tuples
    print('\n',dimension)

#modifying tuples
print('\n original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)
print('\n modified dimensions')
for dimension in dimensions:
    print(dimension)
#When compared with lists, tuples are simple data structures. Use them
#when you want to store a set of values that should not be changed
#throughout the life of a program.
