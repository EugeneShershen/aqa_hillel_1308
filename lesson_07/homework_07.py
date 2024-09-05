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

def sum_two_num(num1, num2):
    """Sum of two numbers.
    :param num1: the first number
    :param num2: the second number
    """
    print('Sum of two numbers:', num1 + num2)

    sep_line()


print('Task 2\n')
sum_two_num(3, 5)

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

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
# def find_substring(str1, str2):
#
#     return -1
#
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""