# Проверка знака числа
# Напишите функцию, которая принимает число и возвращает, является ли оно положительным, отрицательным или нулём.
# Данные:
# num = -3
# Пример вывода:
# Число отрицательное

# def solution(num):
#
#     if num > 0:
#         return "Число положительное"
#     elif num < 0:
#         return "Число отрицательное"
#     return "Число равно 0"
#
# num = int(input("Введите число "))
# result = solution(num)
# print(result)
'''
Создайте функцию filter_strings, которая принимает целое число n и любое количество строк (по отдельности, а не как коллекция).
Функция должна возвращать список строк, длина которых больше n.
Данные:
strings = ["apple", "banana", "cherry", "date", "fig"]
n = 5
Пример вывода:
['banana', 'cherry']
'''
def filter_strings(n: int, *args: str) -> list[str]:

    return [s for s in args if len(s) > n]

strings = ["apple", "banana", "cherry", "date", "fig"]
n = 5
result = filter_strings(n, *strings)
print(result)