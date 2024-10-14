# handling errors with (try ,except), it ll print invalid value instead of crashing the program
try:
    age=int(input('age: '))
    print(age)
except ValueError:
    print('invalid value')

# this program gives a different error, if the age is 0, so we add another exception called zerodivisionerror.
try:
    age=int(input('age: '))
    income= 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age cannot be 0.')
except ValueError:
    print('invalid value')
