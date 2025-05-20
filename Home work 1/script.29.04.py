# new_set = {item ** 0 for item in range(10)}
# print(new_set, type(new_set))
#
# immutable_set = frozenset([1, 2, 3, 4, 5])
# print(immutable_set)
# immutable_from_range = frozenset(range(10))
# print(immutable_from_range)

# # Создание frozenset
# frozen_set1 = frozenset([1, 2, 3])
# frozen_set2 = frozenset([4, 5, 6])
#
# # Создание множества, содержащего frozenset
# set_of_frozensets = {frozen_set1, frozen_set2}
# print(set_of_frozensets)
""""""

# my_dict = {1: "one", 1.0: "float one", True: "boolean one"}
# print(my_dict)
"""
2. Какой результат будет выведен при выполнении следующего кода?

a) {1: "one", 1.0: "float one", True: "boolean one"}
b) {1: "one"}
c) {1: "boolean one"}
d) {1.0: "float one"}

"""
# user = {1: "", 2.0: 2, False: 123, (1, 23): 1234, frozenset([2, 3]): "YEAH"}
# print(user)

# my_set = {} # dict
# print(type(my_set))
# # my_set = set() # set
# # print(type(my_set))
# empty_dict = dict()
# print(empty_dict)
#
# person = {"name": "Alice", "age": 30, "city": "New York"}
# print(person, type(person))
#
# hash(2)

"""
Метод разрешения коллизий в Python: цепочки (chaining)
Python использует метод цепочек для разрешения коллизий в словарях (dict) и множествах (set). Давайте разберем, как это работает:

Принцип работы метода цепочек

Каждая ячейка хеш-таблицы содержит не один элемент, а связный список (цепочку) элементов
При коллизии новый элемент просто добавляется в конец соответствующей цепочки
При поиске элемента, Python сначала вычисляет хеш, находит соответствующую корзину, а затем последовательно просматривает все элементы в цепочке
"""

# print(hash(1))
# print(hash(1.0))
# print(hash(True))
#
# # my_dict = {1.0: "float", 1: "integer", True: "boolean"}
# my_dict = {0: "float", False: "integer"}
# print(my_dict.pop(0))
# print(my_dict)
#
# my_set = {True, 1, 1.0}
# print(my_set)

# # Словарь с использованием функции dict()
# person = dict(name="Bob", age=25, city="London")
# print(person)
#
# # Список кортежей
# pairs = [("name", "Charlie"), ("age", 35), ("city", "Paris")]
# person = dict(pairs)
# print(person)
#
# # Список списков
# pairs = [("name", "Charlie"), ["age", 35], ["city", "Paris"]]
# person = dict(pairs)
# print(person)

# Несоответствующее количество элементов
# not_pairs = [("name", "Charlie"), ["age", 35], ["city", "Paris", "Berlin"]]
# person = dict(not_pairs)  # Вызовет ошибку
# print(person)

# Нехешируемый ключ
# pairs = [(["name", "surname"], "Charlie"), ["age", 35], ["city", "Paris"]]
# person = dict(pairs)  # Вызовет ошибку
# print(person)


# my_dict = {"name": "Alice", "age": 30}
# print(my_dict["name"])
# age = my_dict["age"]
# print(age)
# print(my_dict["city"])  # KeyError: Вызовет ошибку

"""
1. Какой результат будет выведен при выполнении следующего кода?

not_pairs = [("name", "Charlie"), ["age", 35], ["city", "Paris", "Berlin"]]
person = dict(not_pairs)
print(person)

a) {"name": "Charlie", "age": 35, "city": "Paris"}
b) {"name": "Charlie", "age": 35, "city": ["Paris", "Berlin"]}
c) {"name": "Charlie", "age": 35, "city": "Berlin"}
d) Ошибка
"""

# my_dict = {"name": "Alice", "age": 30}
#
# if "name" in my_dict:
#     print(my_dict["name"])  # Выведет значение по ключу 'name'
# if "city" in my_dict:
#     print(my_dict["city"])  # Не выполняется, так как ключ 'city' отсутствует

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for key in my_dict:
#     print(f"Ключ={key}, значение={my_dict[key]}")


# my_dict = {"name": "Alice", "age": 30}
# my_dict["city"] = "New York"  # Добавление нового элемента
# print(my_dict)
#
# my_dict = {"name": "Alice", "age": 30}
# my_dict["age"] = 31  # Обновление значения по ключу "age"
# print(my_dict)

# # Обновление значений и добавление новых ключей
# my_dict = {"name": "Alice", "age": 30}
# my_dict.update({"age": 32, "country": "USA"})
# print(my_dict)
#
# # Обновление с использованием списка кортежей
# my_dict.update([("name", "Bob"), ("email", "bob@example.com")])
# print(my_dict)
#
# # Обновление с использованием именованных аргументов
# my_dict.update(city="New York", orders=[])
# print(my_dict)
#
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# del my_dict["age"]
# print(my_dict)
# # del my_dict["email"]  # Вызовет ошибку
#
# my_dict = {"name": "Alice", "age": 30}
# my_dict.clear()
# print(my_dict)

# my_dict = {"name": "Alice", "age": 30}
# age = my_dict.pop("age")
# print(age)
# print(my_dict)
# my_dict.pop("email")  # Вызовет ошибку

# my_dict = {"name": "Alice", "age": 30}
# last_item = my_dict.popitem()
# print(last_item)
# print(my_dict)


"""
Напишите программу, которая создаёт новый словарь, где значения из исходного словаря становятся ключами, а ключи — значениями.
Данные:
original_dict = {"a": 1, "b": 2, "c": 3}
Пример вывода:
Инверсированный словарь: {1: 'a', 2: 'b', 3: 'c'}

"""














