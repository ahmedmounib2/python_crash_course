prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f'total: {total}')

for x in range(4):
    for y in range (3):
        print(f'({x},{y})')

numbers= [1,1,1,1,5]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

for x_count in numbers:
    print('x'* x_count )

names = ['jhon', 'bob','mosh', 'sara', 'mary']
print(names[0])
print(names[2:])
print(names[2:4])
print(names[:])
names [0] = 'jon'
print(names)


numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(number)
