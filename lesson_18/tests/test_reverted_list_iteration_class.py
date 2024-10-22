import pytest
from pytest import mark

from lesson_18.src.iterators import RevertedListIterator


def test_reverted_list_iteration_positive():
    sample_list = ['apple', 'banana', 'peach', 'pear', 'plum', 'watermelon']
    expected_result = ['watermelon', 'plum', 'pear', 'peach', 'banana', 'apple']
    result = []

    sample_iter = RevertedListIterator(sample_list)
    for stuff in sample_iter:
        result.append(stuff)

    assert result == expected_result, f"Expected list {expected_result}, but got {result}"


@mark.parametrize('input_object', [
    34,
    -41.9,
    'example',
    (1, 2, 3),
    {1, 2, 3},
    {'name': 'some_name', 'address': 'some_address'}])
def test_reverted_list_iteration_negative(input_object):
    expected_result = "The input object type must be a list"

    with pytest.raises(TypeError) as info:
        RevertedListIterator(input_object)
    result = str(info.value)

    assert result == expected_result
