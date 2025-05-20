# print(abs(-7)) # Результат: 7
# print(abs(3.5)) # Результат: 3.5
#
# a = 1
# b = 5
# c = 3
# print(max(a, b, c)) # Передаем несколько значений
# print(max([2, 8, 4, 1])) # Передаем в виде коллекции
#
# print(min(1, 5, 3)) # Передаем несколько значений
# print(min([2, 8, 4, 1])) # Передаем в виде коллекции
#
# print(pow(2, 3)) # Передаем сначала число, а после степень
# print(pow(5, 2))
#
# numbers = [1, 2, 3, 4]
# print(sum(numbers))
#
# print(round(4.56)) # Округление до целого
# print(round(4.567, 2)) # Округление до указанного количества знаков)
#
# print(round(3.4)) # Округление в меньшую сторону
# print(round(3.6)) # Округление в большую сторону
#
# print(round(1.5)) # Результат: 2 (округление к ближайшему чётному)
# print(round(2.5)) # Результат: 2 (округление к ближайшему чётному)
# print(round(3.5356, 3)) # Результат: 4 (округление кближайшему чётному)

# print(round(-1.5)) # Результат: -2(округление к ближайшему чётному)
# print(round(-2.5)) # Результат: -2(округление к ближайшему чётному)
#
# print(round(3.5))
#
# import math
# print(math.sqrt(20))
#
# from math import sqrt, pi
# print(sqrt(16)) # Используем функцию sqrt() без указания имени модуля
# print(pi)

# # Импортируем класс Decimal из модуля decimal
# from decimal import Decimal
# # Создаём два объекта класса Decimal с помощью строк '0.1' и '0.2'
# # Это гарантирует, что числа будут точно представлены в десятичном формате
# a = Decimal('0.1')
# b = Decimal('0.2')
# # Сложение без ошибки округления
# c = a + b
# print(c) # Вывод: 0.3

# # Запрашиваем у пользователя входные данные
# price = float(input("Введите цену товара: "))
# quantity = int(input("Введите количество товара: "))
#
# # Вычисляем полную стоимость без скидки
# total = price * quantity
#
# # Определяем размер скидки
# if 10 <= quantity <= 19:
#     discount = 0.05  # 5%
# elif 20 <= quantity <= 49:
#     discount = 0.10  # 10%
# elif 50 <= quantity <= 99:
#     discount = 0.15  # 15%
# elif quantity >= 100:
#     discount = 0.20  # 20%
# else:
#     discount = 0  # Без скидки
#
# # Рассчитываем сумму скидки и итоговую стоимость
# discount_amount = total * discount
# final_total = total - discount_amount
#
# # Выводим результаты
# print(f"Общая стоимость без скидки: {total:.2f}")
# print(f"Скидка: {discount * 100:.0f}% ({discount_amount:.2f})")
# print(f"Итоговая сумма к оплате: {final_total:.2f}")
#
# import math  # Импортируем модуль math для использования числа π
#
# # Запрашиваем радиус у пользователя
# radius = float(input("Введите радиус круга: "))
#
# # Вычисляем площадь круга и длину окружности
# area = math.pi * radius ** 2
# circumference = 2 * math.pi * radius
#
# # Выводим результаты с округлением до сотых
# print(f"Площадь круга: {area:.2f}")
# print(f"Длина окружности: {circumference:.2f}")

price = float(input("Введите сумму товара: "))
quantity = float(input("Введите количество : "))

sale = 0
if 10 <= quantity < 20:
    sale = 0.05
elif 20 <= quantity < 50:
    sale = 0.1
elif 50 <= quantity < 100:
    sale = 0.15
elif quantity >= 100:
    sale = 0.2

total_price = quantity * price * (1 - sale)

print("Итоговая сумма оплаты: ", total_price)

