#class Employee:
#   pass

#emp_1 = Employee()
#emp_2 = Employee()

#print(emp_1)
#print(emp_2)
#emp_1.first = 'corey'
#emp_1.last = 'schafer'
#emp_1.email = 'corey.schafer@company.com'
#emp_1.pay = 50000

#emp_2.first = 'test'
#emp_2.last = 'user'
#emp_2.email = 'test.user@company.com'
#emp_2.pay = 60000

#print(emp_1.email)
#print(emp_2.email)

# use class to make it easy as below

class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first , self.last)


emp_1 = Employee('corey', 'shafer', 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_2.email)
print(emp_1.email)

#below line is to print the full name w ewill do a method to make it easier , a method within the class
print('{} {}'.format(emp_1.first , emp_1.last))

# after we defined the method:

print(emp_1.fullname())
print(emp_2.fullname())

# both of the below lines are the same
# Employee.fullname(emp_1)
# emp_1.fullname()
