import unittest

from lesson_09.src.homeworks import arithmetic_mean_of_list


class TestArithmeticMeanOfListFunction(unittest.TestCase):
    def test_arithmetic_mean_of_list_positive(self):
        result = arithmetic_mean_of_list([11, 12, 13, 14, 15, 16])
        expected = 13.5
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_arithmetic_mean_of_list_negative(self):
        result = arithmetic_mean_of_list([-11, -12, -13, -14, -15, -16])
        expected = -13.5
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_arithmetic_mean_of_list_fractional(self):
        result = arithmetic_mean_of_list([11.3, 12.4, 13.5, 14.6, 15.7, 16.8])
        expected = 14.05
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_arithmetic_mean_of_list_combine(self):
        result = arithmetic_mean_of_list([11.3, 12, -13.5, 14.6, 15, -16])
        expected = 3.9
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)
