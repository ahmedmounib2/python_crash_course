# 2 dimentional lists
# a list where ever item in the list is another list
# a list within a list

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix [0][1])
matrix[0][1]= 20

print(matrix [0][1])

print(matrix)

for row in matrix:
    for item in row:
        print(item)

# append add a value to the end of the list
numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers)

# adding a value to the middle of the list
numbers.insert(0,10)
print(numbers)

# removing a number from a list
numbers.remove(5)
print(numbers)

# removing all the numbers in a list
numbers.clear()
print(numbers)


numbers = [5,2,1,7,4]

# removing the last number from a list
numbers.pop()
print(numbers)

# get the index number of an item in a list
print(numbers.index(7))
# using this with an item that is not in the list will generate error

#check for the existence of 50 in the list with the in operator is better as it wont generate error
print(50 in numbers)

# check how many 5 is in the list
numbers = [5,2,1,7,5,4]
print(numbers.count(5))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#copying a list to a different list
numbers2= numbers.copy()
numbers.append(10)
print('\n',numbers)
print(numbers2)

# a program that remove duplicates from a list
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
