def sep_line():
    """Create separated line.
    """
    print('-' * 100)


def sum_num_each_string(string_list):
    """Prints the sum of numbers for each string-element.
    :param string_list: a list with string-elements
    """
    try:
        for element in string_list:
            num_list = [int(num) for num in element.split(', ')]
            print(f'The sum of all numbers in the string #{string_list.index(element) + 1}: {sum(num_list)}')
    except ValueError:
        print('The current string does not consist only of numbers!')
    except AttributeError:
        print('Non-string elements can not be used in the list!')


sep_line()
list1 = ['1, 2, 3, 4', '1, 2, 3, 4, 50', 'qwerty1, 2, 3', '1, 2, 3, 4, 50']
sum_num_each_string(list1)
sep_line()

list2 = ['1, 2, 3, 4', (1, 2, 3), '1, 2, 3, 4, 50', '1, 2, 3, 4, 50']
sum_num_each_string(list2)
sep_line()

list3 = ['1, 2, 3, 4', '1, 2, 3, 4, 50', '1, 2, 3, 4, 70']
sum_num_each_string(list3)
sep_line()
