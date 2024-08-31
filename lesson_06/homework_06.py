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


def homework_6_2():
    sep_line()

    input_string = ''
    in_while = True

    while in_while:
        input_string = input('Enter a word with the letter "h": ')
        if input_string.find('h') != -1 or input_string.find('H') != -1:
            in_while = False

    print('The word you entered:', input_string)

    sep_line()


# call functions 'homework_6_1()', 'homework_6_2()'
homework_6_1()
homework_6_2()
