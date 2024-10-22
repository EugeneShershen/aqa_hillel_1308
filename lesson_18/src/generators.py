def even_numbers_generator(finite_num):
    """ Returns every even number up to the finite number.
    :param finite_num: a finite number
    """
    if isinstance(finite_num, int) is not True:
        raise TypeError("The finite number must be integer")

    if finite_num <= 0:
        raise ValueError("The finite number must be greater than 0")

    current_num = 0
    while current_num < finite_num:
        if current_num % 2 == 0:
            yield current_num

        current_num += 1


def fibonacci_generator(finite_num):
    """Returns sequences of fibonacci numbers up to the finite number.
    :param finite_num: a finite number
    """
    if isinstance(finite_num, int) is not True:
        raise TypeError("The finite number must be integer")

    if finite_num <= 0:
        raise ValueError("The finite number must be greater than 0")

    a, b = 0, 1
    while a <= finite_num:
        yield a
        a, b = b, a + b
