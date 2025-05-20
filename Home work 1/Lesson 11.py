# text = input("Введите строку: ")
# reversed_text = ""
# index = len(text) - 1
#
# while index >= 0: # -1
#     char = text[index]
#     if not ('0' <= char <= '9'):  # Проверка, что символ не цифра
#         reversed_text += char
#     index -= 1
#
# print("Результат:", reversed_text)
#
# text = input("Введите строку: ")
# reversed_text = ""
#
# for char in reversed(text):
#     if not ('0' <= char <= '9'):
#         reversed_text += char
#
# print("Результат:", reversed_text)

# for i in range(5):
#  print(i)

# for i in range(2, 6):
#  print(i)
#
# for i in range(1, 10, 2):
#  print(i)

# for i in range(10, 0, -2):
#  print(i)
# for i in range(-4, -8, -1):
#  print(i)

# for letter in "Python":
#   if letter == "h":
#    break
#   print(letter)

# for letter in "Python":
#       if letter == "h":
#           continue
#       print(letter)
#
# for letter in "Python":
#  if letter == "h":
#     break # Цикл прерывается на символе "h"
#  print(letter)
# else:
#  print("Цикл завершён нормально.") # Этот блок не выполнится

# for i in "AB":
#  for j in "12":
#   print(i, j)

# for hour in range(24):
#  for minute in range(60):
#   print("Время (часов:минут): ", hour,
# ':', minute, sep='')

# num = int(input("Введите число: "))
#
# if num < 0:
#     print("Факториал определён только для неотрицательных чисел.")
# else:
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     print("Факториал числа", num, "равен", result)

# num = int(input("Введите число: "))
#
# result = 1
# for i in range(1, num + 1):
#     result *= i
# print("Факториал числа", num, "равен", result)
#
# # Запрос ввода размеров у пользователя
# width = int(input("Введите ширину: "))
# height = int(input("Введите высоту: "))
#
# # Внешний цикл отвечает за количество строк (высота)
# for _ in range(height):
#     # Внутренний цикл отвечает за количество символов в строке (ширина)
#     print("*" * width)

size = int(input("Введите размер ромба: "))


for i in range(1, size + 1, 2):
    print(" " * ((size - i) // 2) + "*" * i)

for i in range(size - 2, 0, -2):
    print(" " * ((size - i) // 2) + "*" * i)
