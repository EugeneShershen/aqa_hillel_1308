def add_two_num(num1, num2):
    """Adds two numbers.
    :param num1: the first number
    :param num2: the second number
    """
    print('The adds of two numbers:', num1 + num2)


def arithmetic_mean_of_list(num_list):
    """Calculates an arithmetic mean of the number's list.
    :param num_list: list of numbers
    """
    sum_num= sum(num_list)

    arithmetic_mean = sum_num / len(num_list)
    print('The arithmetic mean of number\'s list:', arithmetic_mean)


def reverted_string(string):
    """Reverts the string.
    :param string: input string
    """
    return string[::-1]
