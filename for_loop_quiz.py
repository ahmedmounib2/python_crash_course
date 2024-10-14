# range function, to generate a series of numbers
for value in range(1,5):  #will print from 1 to 4
    print(value)
# making a list of number
numbers= list(range(1,5))
print(numbers)
# skipping numbers in a given range through range function
even_numbers= list(range(2,11,2))
print(even_numbers)
# making a list of the 1st 10 squares with range function
squares= []
for value in range(1,11):
    squar = value ** 2
    squares.append(squar)
print(squares , '\n')
# To write this code more concisely, omit the temporary variable square and
# append each new value directly to the list:
squares= []
for value in range(1,11):
    squares.append(value**2)
print(squares)
