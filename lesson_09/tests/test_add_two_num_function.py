import unittest

from lesson_09.src.homeworks import add_two_num


class TestAddTwoNumFunction(unittest.TestCase):
    def test_add_two_num_positive(self):
        result = add_two_num(20, 18)
        expected = 38
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_add_two_num_negative(self):
        result = add_two_num(-20, -18)
        expected = -38
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_add_two_num_fractional(self):
        result = add_two_num(20.7, 18.4)
        expected = 39.1
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_add_two_num_combine(self):
        result1 = add_two_num(-20, 18)
        expected1 = -2
        message1 = f"Test failed. The result '{result1}' not equals expected '{expected1}'"

        result2 = add_two_num(20, 18.4)
        expected2 = 38.4
        message2 = f"Test failed. The result '{result2}' not equals expected '{expected2}'"

        result3 = add_two_num(-20, 18.4)
        expected3 = -1.6
        message3 = f"Test failed. The result '{result3}' not equals expected '{expected3}'"

        self.assertEqual(result1, expected1, msg=message1)
        self.assertEqual(result2, expected2, msg=message2)
        self.assertEqual(result3, expected3, msg=message3)
