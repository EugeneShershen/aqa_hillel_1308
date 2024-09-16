import unittest

from lesson_09.src.homeworks import reverted_string


class TestRevertedStringFunction(unittest.TestCase):
    def test_reverted_string_only_letters(self):
        result = reverted_string('AbcdeFgh')
        expected = 'hgFedcbA'
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_reverted_string_only_numbers(self):
        result = reverted_string('87364512')
        expected = '21546378'
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_reverted_string_only_symbols(self):
        result = reverted_string('-=-+* /!/ ?-')
        expected = '-? /!/ *+-=-'
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)

    def test_reverted_string_only_combine(self):
        result = reverted_string('Hellow, user#123!')
        expected = '!321#resu ,wolleH'
        message = f"Test failed. The result '{result}' not equals expected '{expected}'"

        self.assertEqual(result, expected, msg=message)
