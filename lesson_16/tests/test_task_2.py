from pytest import mark

from lesson_16.src.task_2 import Square, Triangle, Circle


def list_of_shapes():
    square = Square(8)
    triangle = Triangle(12, 3, 26)
    circle = Circle(7.3)

    result = [square, triangle, circle]

    return result


@mark.parametrize('shape', list_of_shapes())
def test_print_shapes(shape):
    expected_result = (f'\nArea of the {type(shape).__name__}: {shape.get_area()}\n'
                       f'Perimeter of the {type(shape).__name__}: {shape.get_perimeter()}')
    result = shape.__str__()
    print(shape)

    assert result == expected_result
