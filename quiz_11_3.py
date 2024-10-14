# ex 11-3

import unittest


from employee_class import Employee

class TestEmployee(unittest.TestCase):
    """check if the employee class is working properly"""
    def test_give_default_raise(self):
        """test for give_raise method in Employee class"""
        ahmed = Employee('ahmed','medhat', 1000)
        ahmed.give_raise()
        self.assertEqual(6000, ahmed.salary)

    def test_custom_raise(self):
        ahmed = Employee('ahmed', 'medhat', 1000)
        ahmed.give_raise(20000)
        self.assertEqual(21000,ahmed.salary)



if __name__ == '__main__':
    unittest.main()



#
# the book solution



import unittest


from employee_class import Employee

class TestEmployee(unittest.TestCase):
    """test if the class works with the book solution"""

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        employee = Employee('eric', 'matthes', 65_000)
        employee.give_raise()
        assert employee.salary == 70_000

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        employee = Employee('eric', 'matthes', 65_000)
        employee.give_raise(10000)
        assert employee.salary == 75_000


if __name__ == '__main__':
    unittest.main()
