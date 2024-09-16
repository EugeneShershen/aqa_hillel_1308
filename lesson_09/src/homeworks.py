def add_two_num(num1, num2):
    """Adds two numbers.
    :param num1: the first number
    :param num2: the second number
    """
    return round(num1 + num2, 5)


def arithmetic_mean_of_list(num_list):
    """Calculates an arithmetic mean of the number's list.
    :param num_list: list of numbers
    """
    sum_num = sum(num_list)
    arithmetic_mean = sum_num / len(num_list)

    return round(arithmetic_mean, 5)


def reverted_string(string):
    """Reverts the string.
    :param string: input string
    """
    return string[::-1]
