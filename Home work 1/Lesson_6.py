# # print(sum(int(i) for i in input("input: ")))
#
# x =12
# if x == 12: #True
#     print("Hello world")
# summa = x + 12 * 2
#
# print(summa)
#
# if 1:
#     # code
#     print("somehting")
#
# print("Что-то новое")
#
# age = int(input("Input your age"))
#
# if age > 18:
#
#     x = 7
#     if x > 10:
#         print("x больше 10")
#     elif x > 5:
#         print("x больше 5, но меньше или равно 10")
#
# age = 25
# if age < 18:
#     print("Несовершеннолетний")
# elif age < 30:
#     print("Молодой взрослый")
# elif age < 50:
#     print("Взрослый")
#
# age = 25
# if age < 18:
#     print("Несовершеннолетний")
# elif age < 30:
#     print("Молодой взрослый")
# elif age < 50:
#     print("Взрослый")
# else:
#     print("Пожилой")
#
# data = "numbers"
# integers = True
# if data == "numbers":
#     print("Это числовые данные.")
#     if integers:
#         print("Числа целые.")
#     else:
#         print("Числа с плавающей запятой.")
# else:
#     print("Это нечисловые данные.")
#
# vacation_requested = True
# available_days = 5
# required_days = 7
# if vacation_requested:
#     print("Запрос на отпуск получен.")
#     if available_days >= required_days:
#         print("Запрос на отпуск одобрен.")
#     else:
#         print("Недостаточно доступных дней для отпуска.")
# else:
#     print("Отпуск не запрашивался.")
#
# name_filled = True
# email_filled = True
# email_valid = False
# if name_filled:
#     print("Имя заполнено.")
#     if email_filled:
#         print("Email заполнен.")
#         if email_valid:
#             print("Email действителен.")
#         else:
#             print("Email недействителен.")
#     else:
#         print("Email не заполнен.")
# else:
#     print("Имя не заполнено.")
#
# name_filled = True
# email_filled = True
# email_valid = False
# if not name_filled:
#     print("Имя не заполнено.")
# elif not email_filled:
#     print("Имя заполнено.")
#     print("Email не заполнен.")
# elif not email_valid:
#     print("Имя заполнено.")
#     print("Email заполнен.")
#     print("Email недействителен.")
# else:
#     print("Имя заполнено.")
#     print("Email заполнен.")
#     print("Email действителен.")

# age_valid = True
# region_allowed = False
# special_permission = True
#
# if age_valid:
#     if region_allowed or special_permission:
#         print("Доступ разрешен.")
#     else:
#         print("Ваш регион не поддерживается.")
# else:
#     print("Возраст не соответствует требованиям.")
#
# age_valid = True
# region_allowed = True
# special_permission = False
#
# if not age_valid:
#     print("Возраст не соответствует требованиям.")
# elif not (region_allowed or special_permission):
#     print("Ваш регион не поддерживается.")
# else:
#     print("Доступ разрешен.")
#
# age = 18
# status = "Взрослый" if age >= 18 else "Несовершеннолетний"
# print(status)
#
# x = 10
# print("Чётное" if x % 2 == 0 else "Нечётное")
#
# x = 20
# y = 10
# z = 0
# # Сложное условие лучше не помещать в тернарный оператор
# print(x) if (x > 10 and y < 5 or z == 0) else print(0)

# score = 80  # так писать плохо
# grade = "Отлично" if score > 90 else ("Хорошо" if score > 75 else ("Удовлетворительно"
# if score > 50 else "Неудовлетворительно"))
# print(grade)
#
# number = 7
# match number:
#  case 1:
#     print("Это один.")
#  case 2 | 3: # Символ "|" является аналогом оператора "or"
#     print("Это два или три.")
#  case _ if number > 5:
#     print("Число больше 5.")
#  case _:
#     print("Это число меньше или равно 5.")
#
# value = "Hello"
# match value:
#     case int():
#         print("Это целое число.")
#     case str():
#         print("Это строка.")
#     case bool():
#         print("Это логический тип.")
#     case  _:
#         print("Неизвестный тип данных.")

num = float(i)