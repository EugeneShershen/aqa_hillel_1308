adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print('-' * 100)
print('Task 01')

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print('-' * 100)
print('Task 02')

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', ' ')
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print('-' * 100)
print('Task 03')

adwentures_of_tom_sawer = adwentures_of_tom_sawer.split('   ')
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('-' * 100)
print('Task 04')

counter_h = adwentures_of_tom_sawer.count('h')
print('Number of a letter "h" in the text: ', counter_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('-' * 100)
print('Task 05')

words_with_capital_letter = 0
for word in adwentures_of_tom_sawer:
    if word.istitle():
        words_with_capital_letter += 1

print('Number of words with capital letter: ', words_with_capital_letter)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print('-' * 100)
print('Task 06')

index_second_time = adwentures_of_tom_sawer.find('Tom', adwentures_of_tom_sawer.find('Tom') + 1)
print('The position index, when "Tom" encountered for the second time: ', index_second_time)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print('-' * 100)
print('Task 07')

temporary_list_text = adwentures_of_tom_sawer.split('. ')
adwentures_of_tom_sawer_sentences = '.\n'.join(temporary_list_text)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print('-' * 100)
print('Task 08')

temporary_list_text = adwentures_of_tom_sawer_sentences.split('.\n')
fourth_sentence = temporary_list_text[3].lower()
print('The fourth sentence in lower register: ', fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print('-' * 100)
print('Task 09')

temporary_index = adwentures_of_tom_sawer_sentences.find('By the time')
if temporary_index != -1:
    print('There is such a sentence.')
else:
    print('There is not such a sentence.')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print('-' * 100)
print('Task 10')

last_sentence = temporary_list_text[-1].split(' ')
print('Number of words in the last sentence: ', len(last_sentence))

print('-' * 100)
