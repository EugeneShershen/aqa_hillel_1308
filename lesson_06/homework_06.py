# separated line
def sep_line():
    print('-' * 100)


# homework 6.1
def homework_6_1():
    sep_line()

    input_string = input('Enter anything: ')
    set_string = set(input_string)

    count_set_string = 0
    for _ in set_string:
        count_set_string += 1

    if count_set_string > 10:
        print('Result: True')
    else:
        print('Result: False')

    sep_line()


# homework 6.2
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


# homework 6.3
def homework_6_3():
    sep_line()

    list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    list2 = [element for element in list1 if isinstance(element, str) is True]

    print('Original list:', list1)
    print('Result:', list2)

    sep_line()


# homework 6.4
def homework_6_4():
    sep_line()

    list_numbers = [1, 14, 22, -4, 8, 31, 0, 29, 431, -81, 68, 50]
    sum_even_numbers = 0

    for num in list_numbers:
        if num % 2 == 0:
            sum_even_numbers += num

    print('List with numbers:', list_numbers)
    print('Summary of all even numbers in list:', sum_even_numbers)

    sep_line()


# call functions 'homework_6_1()', 'homework_6_2()', 'homework_6_3()', 'homework_6_4()'
homework_6_1()
homework_6_2()
homework_6_3()
homework_6_4()
