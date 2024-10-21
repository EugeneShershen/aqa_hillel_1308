import pytest
from pytest import mark

from lesson_18.src.generators import even_numbers_generator


def test_even_numbers_generator_positive():
    finite_number = 15
    expected_result = [0, 2, 4, 6, 8, 10, 12, 14]
    result = []

    gen = even_numbers_generator(finite_number)
    for _ in range(len(expected_result)):
        result.append(next(gen))

    assert result == expected_result, f"Expected list {expected_result}, but got {result}"


def error_message(error):
    if error == 'type':
        return 'The finite number must be integer'
    elif error == 'value':
        return 'The finite number must be greater than 0'


@mark.parametrize('finite_number, error, expected_result', [
    ('15', TypeError, error_message('type')),
    (12.3, TypeError, error_message('type')),
    ([1, 2, 3], TypeError, error_message('type')),
    (0, ValueError, error_message('value')),
    (-28, ValueError, error_message('value')),
])
def test_even_numbers_generator_negative(finite_number, error, expected_result):
    with pytest.raises(error) as info:
        gen = even_numbers_generator(finite_number)
        next(gen)
    result = str(info.value)

    assert result == expected_result
