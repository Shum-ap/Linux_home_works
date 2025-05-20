# # # Создание frozenset
# # frozen_set1 = frozenset([1, 2, 3])
# # frozen_set2 = frozenset([4, 5, 6])
# # # Создание множества, содержащего frozenset
# # set_of_frozensets = {frozen_set1, frozen_set2}
# # print(set_of_frozensets)
# '''Популярные слова
# Реализуйте функцию, которая принимает любое количество строк с текстом.
# Функция должна возвращать подсчет самых популярных слов в количестве,
# переданном в функцию. Программа должна игнорировать регистр слов. Выведите 5
# самых популярных слов и их количество.
# Данные:
# '''
# from collections import Counter
#
# def most_common_words(*texts):
#     text = ' '.join(texts).lower()
#
#     for ch in '.,!?;:':
#         text = text.replace(ch, '')
#
#     words = text.split()
#     counter = Counter(words).most_common(5)
#
#     print("5 самых популярных слов:")
#     for word, count in counter:
#         print(f"{word}: {count}")
#
# text1 = "This is a sample text with some repeated words."
# text2 = "Another sample text with different words."
# text3 = "Text processing is fun when words repeat."
#
# most_common_words(text1, text2, text3)
#
#
#
# '''Группировка задач по категории
# Реализуйте функцию, которая принимает словарь задач с категориями и группирует
# задачи по их категориям.
# Данные:
#
# Пример вывода:
# Группировка по категориям:
# {
#  'работа': ['task1', 'task4'],
#  'учёба': ['task2', 'task5'],
#  'развлечения': ['task3']
# }
# '''
# from collections import defaultdict
#
# def group_tasks_by_category(tasks):
#     grouped = defaultdict(list)
#     for task, category in tasks.items():
#         grouped[category].append(task)
#     return dict(grouped)
#
# tasks = {
#     "task1": "работа",
#     "task2": "учёба",
#     "task3": "развлечения",
#     "task4": "работа",
#     "task5": "учёба",
# }
''''''
from traceback import print_list

#
# def add(x, y):
#     return x + y
#
#
# def multiply(x, y):
#     return x * y
#
#
# # Функции можно хранить в списках, словарях и передавать их динамически
# operations = {
#     "+": add,
#     "*": multiply
# }
# # choice = input("Выберите операцию (+, *): ")
# # Из словаря получена функция и скобки с аргументами запускают её
# print(operations["+"](10, 5))
# print(operations["*"](10, 5))
#
#
# def add(x, y):
#  return x + y
# print((lambda f, a, b: f(a, b))(add, 3, 4))
# def last_char_len(s):
#     return s[-1], len(s)
#
# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# # Сортировка по последнему символу и длине (последовательно)
# result = sorted(words, key=last_char_len)
# result = sorted(words, key=lambda x: (x[-1], len(x)))
# print(result)
'''
1. Список квадратов чисел
Напишите функцию, которая сформирует список квадратов из полученного списка, без 
использования циклов или списковых включений.
Данные:
numbers = [1, 2, 3, 4, 5]
Пример вывода:
[1, 4, 9, 16, 25]
'''

# numbers = [1, 2, 3, 4, 5]
# def square_numbers(numbers):
#     return map(lambda n: n**2, numbers)
# print(list(square_numbers(numbers)))

'''
Сортировка по возрасту
Отсортируйте список кортежей (имя, возраст) по возрасту.
Данные:
people = [
    ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
    ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
    ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
]
Пример вывода:
[('Mike', 19), ('Isabella', 19), ('Henry', 19), ('Bob', 20), ('Charlie', 23),
 ('Jack', 24), ('Alice', 25), ('Grace', 27), ('Kevin', 28), ('Eve', 29), 
 ('Diana', 30), ('Laura', 31), ('Oscar', 33), ('Frank', 33), ('Nancy', 35)]
'''
#
# people = [
#     ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
#     ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
#     ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
# ]
# def sort_by_age(people):
#     return sorted(people, key=lambda p: p[1])
# print(sort_by_age(people))

'''ортировка по возрасту и имени
Отсортируйте список кортежей (имя, возраст) по убыванию возраста, в рамках одинакового
 возраста отсортируйте также по имени по алфавиту.

Пример вывода:
[('Nancy', 35), ('Frank', 33), ('Oscar', 33), ('Laura', 31), ('Diana', 30), 
('Eve', 29), ('Kevin', 28), ('Grace', 27), ('Alice', 25), ('Jack', 24), ('Charlie', 23),
 ('Bob', 20), ('Henry', 19), ('Isabella', 19), ('Mike', 19)]'''

people = [
    ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
    ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
    ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
]
def sort_by_age_name(people):
    return sorted(people, key=lambda p: (-p[1], p[0]))
print(sort_by_age_name(people))