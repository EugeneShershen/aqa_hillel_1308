# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = side_1 + side_2 + side_3 + side_4
print(perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
all_tree = apple_tree + pear_tree + plum_tree
result_1 = f"""Quantity of apples: {apple_tree}\nQuantity of peaches: {pear_tree}\nQuantity of plums: {plum_tree}
\nAll trees: {all_tree}"""
print(result_1)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

before_lunch = 5
after_lunch = before_lunch - 10
evening = after_lunch + 4
result_2 = f"""Air temperature before lunch: {before_lunch}°C\nAir temperature after lunch: {after_lunch}°C
Air temperature in the evening: {evening}°C"""
print(result_2)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boy = 24
girl = boy // 2
today_boy = boy - 1
today_girl = girl - 2
today_children = today_boy + today_girl
result_3 = f"""Boys in a circle: {boy}\nGirls in a circle: {girl}
\nBoys in a circle today: {today_boy}\nGirls in a circle today: {today_girl}
\nChildren in a circle today: {today_children}"""
print(result_3)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
all_books = book_1 + book_2 + book_3
result_4 = f"""Price of the first book: {book_1} UAH
Price of the second book: {book_2} UAH
Price of the third book: {book_3} UAH
\nPrice of all books: {all_books} UAH"""
print(result_4)
