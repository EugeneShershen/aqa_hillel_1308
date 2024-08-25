alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"'
                       '\n"That depends a good deal on where you want to get to," said the Cat.'
                       '\n"I don\'t much care where ——" said Alice.'
                       '\n"Then it doesn\'t matter which way you go," said the Cat.'
                       '\n"—— so long as I get somewhere," Alice added as an explanation.'
                       '\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

square_black_sea = 436402
square_azov_sea = 37800
square_both_seas = square_black_sea + square_azov_sea
result_4 = (f'Square of Black Sea: {square_black_sea} km2'
            f'\nSquare of Azov Sea: {square_azov_sea} km2'
            f'\nSquare of both seas: {square_both_seas} km2')

print(result_4)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

all_storages = 375291
storages_1_and_2 = 250449
storages_2_and_3 = 222950
storage_1 = all_storages - storages_2_and_3
storage_3 = all_storages - storages_1_and_2
storage_2 = all_storages - (storage_1 + storage_3)
result_5 = (f'Quantity of goods on the first storage: {storage_1}'
            f'\nQuantity of goods on the second storage: {storage_2}'
            f'\nQuantity of goods on the third storage: {storage_3}')

print(result_5)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_cost = 1179
time_period = 18
whole_price = monthly_cost * time_period
result_6 = (f'Monthly cost: {monthly_cost} UAH'
            f'\nPeriod of time: {time_period} months'
            f'\nWhole price of computer: {whole_price} UAH')

print(result_6)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
result_7 = (f'a) {a}'
            f'\nb) {b}'
            f'\nc) {c}'
            f'\nd) {d}'
            f'\ne) {e}'
            f'\nf) {f}')

print(result_7)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_amount = 4
medium_pizza_amount = 2
juice_amount = 4
cake_amount = 1
water_amount = 3
big_pizza_cost = 274
medium_pizza_cost = 218
juice_cost = 35
cake_cost = 350
water_cost = 21
all_price = ((big_pizza_amount * big_pizza_amount) + (medium_pizza_amount * medium_pizza_cost) +
             (juice_amount * juice_cost) + (cake_amount * cake_cost) + (water_amount * water_cost))
result_8 = f'Amount of money, needed for birthday: {all_price} UAH'

print(result_8)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos_amount = 232
photos_one_page = 8
pages_amount = int(232 / 8)
result_9 = (f'Quantity of photos: {photos_amount}'
            f'\nMaximum quantity photos in one page: {photos_one_page}'
            f'\nQuantity of necessary pages: {pages_amount}')

print(result_9)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_for_100_km = 9
tank_capacity = 48
necessary_fuel = int(distance * fuel_for_100_km / 100)
min_times_for_refuel = int(necessary_fuel / tank_capacity)
result_10 = (f'Quantity of fuel for travel: {necessary_fuel} liters'
             f'\nMinimum quantity of times, needed to refuel: {min_times_for_refuel}')

print(result_10)
