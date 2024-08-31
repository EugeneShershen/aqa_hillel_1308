# separated line
def sep_line():
    print('-' * 100)


# homework 6.1
def homework_6_1():
    sep_line()

    input_string = input('Enter anything: ')
    set_string = set(input_string)

    count_set_string = 0
    for element in set_string:
        count_set_string += 1

    if count_set_string > 10:
        print('Result: True')
    else:
        print('Result: False')

    sep_line()


# call a function 'homework_6_1()'
homework_6_1()
