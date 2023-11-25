import unittest
import pytest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, 'Should be 6')
    
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, 'Should be 6')

def test_sum():
    assert sum([1, 4, 6]) == 10, 'Should be 11'



if __name__ == '__main__':
    # unittest.main()
    test_sum()

# Calling nose2 and pytest from the terminal:
# nose2 - python3 -m nose2, will read test*.py files and test cases inherited from unittest.TestCase in the current directory
# pytest - python3 -m pytest, will run test cases from files starting with test_, uses built-in assert statement, filter test cases, rerun from last failing test