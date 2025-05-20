# 3 Из чисел в слова
# Напишите программу, которая заменяет числовые значения в словаре на их
# строковое представление (например, 1 → "один").
# Используйте заранее подготовленный словарь чисел.
# Данные:
# # Словарь сопоставлений
# number_to_word = {1: "один", 2: "два", 3: "три"}
# # Исходные данные
# data = {"x": 1, "y": 2, "z": 3}
# Пример вывода:
# {'x': 'один', 'y': 'два', 'z': 'три'}
'''Решить без вывода ошибки в случае если нету перевода в словаре number_to_word
3 Из чисел в слова
Напишите программу, которая заменяет числовые значения в словаре на их строковое представление (например, 1 → "один").
Используйте заранее подготовленный словарь чисел. Решить без вывода ошибки в случае если нету перевода в словаре number_to_word

Данные:
Словарь сопоставлений
number_to_word = {1: "один", 2: "два", 3: "три"}

Исходные данные
data = {"x": 1, "y": 2, "z": 3, "a": 4, "b": 1}

Пример вывода:
{'x': 'один', 'y': 'два', 'z': 'три', "b": "один"}'''

# my_dict = {"name": "Alice", "age": 30}
# result = my_dict.setdefault("age", 25)
# print(result)
# print(my_dict)

#
# def greet(name):
#  print(f"Привет, {name}!")
# greet("Алиса")
#
# def calculate_sum(*args):
#  print("Аргументы:", args)
#  print("Сумма:", sum(args))
# calculate_sum(1, 2, 3)
# calculate_sum(5, 6, 7)

# def print_user_info(**kwargs):
#     print("Информация о пользователе:")
#     for key, value in kwargs.items():
#         print(f"\t{key}: {value}")
# print_user_info(name="Alice", age=25, city="New York")
# print_user_info()

# def show_full_info(name, *args, age=25, **kwargs):
#  print(f"Name: {name}")
#  print(f"Other details: {args}")
#  print(f"Age: {age}")
#  print(f"Additional info: {kwargs}")
# show_full_info("Alice", "Developer", age=30, city="New York", hobby="Reading")
#
# def convert_temperature(temp: float, scale: str) -> float:
#  """
#  Конвертирует температуру из Цельсия в Фаренгейт и наоборот.
#
#  :param temp: Температура (float)
#  :param scale: 'C' для Цельсия или 'F' для Фаренгейта
#  :return: Конвертированная температура (float)
#  """
#  if scale.upper() == 'C':
#   return temp * 9 / 5 + 32
#  elif scale.upper() == 'F':
#   return (temp - 32) * 5 / 9
#  else:
#   raise ValueError("Шкала должна быть 'C' или 'F'.")
#
# temp = 100
# scale = "C"
# converted = convert_temperature(temp, scale)
# print(f"{temp}°{scale} = {converted:.2f}°{'F' if scale == 'C' else 'C'}")

def check_number_sign(num: float) -> str:
 """
 Проверяет знак числа и возвращает строку с результатом.

 :param num: Число (int или float)
 :return: Строка с описанием знака числа
 """
 if num > 0:
  return "Число положительное"
 elif num < 0:
  return "Число отрицательное"
 else:
  return "Число равно нулю"


# Пример использования
num = -3
result = check_number_sign(num)
print(result)
