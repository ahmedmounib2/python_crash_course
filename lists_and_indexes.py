# lists are grouped in []
bicycles= ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# this way you ll print the whole list as is

#if you want to print an item in a list print(bicycles[0])
print(bicycles[0])

print(bicycles[0].title()) #this way its formatted nice with a capital T
# the first item in a list is always 0, if you request number 5 then subtract 1 , its position is 4 , since the 1st item is 0.
print(bicycles[1]) #this print bicycle 2
print(bicycles[2]) #this prints bicycle 3
print(bicycles[-1]) #-1 always return the last item in a list
print(bicycles[-2]) #The index -2 returns the second item from the end of the list, and so on
print(bicycles[-3])
message= f"my first bicycel was {bicycles[0].title()} "
print(message)
