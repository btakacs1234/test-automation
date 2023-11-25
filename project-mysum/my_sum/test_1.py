# Can import from init like this: target = __import__('my_sum.py') \ sum = target.sum , instead of the usual from x import y
# Before testing, determine what is to be tested and what kind of test, unit or integration or what

# Structure:
# Create inputs, execute code being tested, capture output, compare output with an expected result

import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """

        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main