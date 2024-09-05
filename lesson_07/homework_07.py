def sep_line():
    """Create separated line"""
    print('-' * 100)


# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    """Print the multiplication table of a given number.
    :param number: the given number
    """
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

    sep_line()


sep_line()
print('Task 1\n')
multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def add_two_num(num1, num2):
    """Adds two numbers.
    :param num1: the first number
    :param num2: the second number
    """
    print('The adds of two numbers:', num1 + num2)

    sep_line()


sep_line()
print('Task 2\n')
add_two_num(3, 5)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_mean_of_list(num_list):
    """Calculates an arithmetic mean of the number's list.
    :param num_list: list of numbers
    """
    sum_num = 0
    for num in num_list:
        sum_num += num

    arithmetic_mean = sum_num / len(num_list)
    print('The arithmetic mean of number\'s list:', arithmetic_mean)

    sep_line()


sep_line()
print('Task 3\n')
arithmetic_mean_of_list([4, 5, 6, 7, 8, 9])

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverted_string(string):
    """Reverts the string.
    :param string: input string
    """
    return string[::-1]


sep_line()
print('Task 4\n')
print('The reverted string:', reverted_string('Hellow, user!'))
sep_line()

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_in_list(word_list):
    """Return the longest word in the list.
    :param word_list: list of words
    """
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


sep_line()
print('Task 5\n')
fruit_list = ['apple', 'pear', 'banana', 'plum', 'peach']
print('The longest word in the list:', longest_word_in_list(fruit_list))
sep_line()

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1: str, str2: str):
    """Finds the substring in the string.
    :param str1: the main string
    :param str2: the substring
    """
    first_index = str1.find(str2)
    if first_index == -1:
        return -1
    else:
        return first_index


sep_line()
print('Task 6\n')

string1 = "Hello, world!"
string2 = "world"
print(f'The result of searching "{string2}" in "{string1}":', find_substring(string1, string2)) # поверне 7

string1 = "The quick brown fox jumps over the lazy dog"
string2 = "cat"
print(f'The result of searching "{string2}" in "{string1}":', find_substring(string1, string2)) # поверне -1

sep_line()

# task 7
def count_unique_symbol():
    """Counts the unique symbols in the input string.
    """
    input_string = input('Enter anything: ')
    set_string = set(input_string)

    count_set_string = len(set_string)
    print('\nIs the unique symbols more than 10?')

    if count_set_string > 10:
        print('Yes')
    else:
        print('No')

    sep_line()


sep_line()
print('Task 7\n')
count_unique_symbol()

# task 8
def check_h_in_word():
    """Checks the letter 'h' in input word.
    """
    input_string = ''
    in_while = True

    while in_while:
        input_string = input('Enter a word with the letter "h": ')
        if input_string.find('h') != -1 or input_string.find('H') != -1:
            in_while = False

    print('The word you entered:', input_string)

    sep_line()

sep_line()
print('Task 8\n')
check_h_in_word()

# task 9
def create_string_list(orig_list):
    """Creates a new list from the original list only with 'string' elements.
    :param orig_list: original list
    """
    filtered_list = [element for element in orig_list if isinstance(element, str) is True]

    print('Original list:', orig_list)
    print('Result:', filtered_list)

    sep_line()

sep_line()
print('Task 9\n')
list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
create_string_list(list1)

# task 10
def sum_even_number(list_numbers):
    """Sums up all even numbers from number's list.
    :param list_numbers: list of numbers
    """
    sum_even_numbers = 0

    for num in list_numbers:
        if num % 2 == 0:
            sum_even_numbers += num

    print('List with numbers:', list_numbers)
    print('Sum of all even numbers in list:', sum_even_numbers)

    sep_line()

sep_line()
print('Task 10\n')
list2 = [1, 14, 22, -4, 8, 31, 0, 29, 431, -81, 68, 50]
sum_even_number(list2)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""