#changing an item in a list
motorcycles= ['honda','yamaha','suzuki','halawa200','bmw']
print(motorcycles)

motorcycles[0] = 'dayun'  #like this line to switct the item, you cn change the number if you wish to change a different item
print(motorcycles)

#adding items to a list, the easist way to do this without affecting other items is the append method which add the item to the end of the list
motorcycles.append('vespa')
print(motorcycles)

motorcycles.append('hyunday')
motorcycles.append('mercedes')
print(motorcycles)

#we can add any item to a specific position in a list using insert method
motorcycles.insert(0, 'makana')
print(motorcycles)

#removing an item from a list using del státement
del motorcycles[1]
del motorcycles[2]
del motorcycles[4]
del motorcycles[3]
print(motorcycles)
