# chapter 11 - Testing code

# def get_formatted_name(first,last):
#     """get a neatly formatted name"""
#     name= f"{first} {last}"
#     return name.title()
# name_function.py


# Unit Tests and Test Cases
# A Passing Test
# The syntax for setting up a test case takes some getting used to, but once
# you’ve set up the test case it’s straightforward to add more unit tests for your
# functions. To write a test case for a function, import the unittest module and
# the function you want to test. Then create a class that inherits from
# unittest.TestCase, and write a series of methods to test different aspects of your
# function’s behavior.
# Here’s a test case with one method that verifies that the function
# get_formatted_name() works correctly when given a first and last name:

import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """test for 'name_function.py'."""
    def test_first_last_name(self):
        """do names like Janis Joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """do names like 'wolfgang amedues mozart' work"""
        formatted_name= get_formatted_name('wolfgang', 'amedues', 'mozart')
        self.assertEqual(formatted_name, 'Wolfgang Mozart Amedues')


if __name__ == '__main__':
    unittest.main()
