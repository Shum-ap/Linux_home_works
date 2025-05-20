# fruits = ["apple", "banana", "cherry", "banana", ["banana", "banana"]]
# for fruit in fruits:
#     if "banana" == fruit: #
#         fruits.remove(fruit)
#
# print(fruits)
# fruits = ["apple", "banana", "cherry", "banana", ["banana", "ananas"], []]
# search = input("search fruit: ")
#
#
# # удаление и возврат элемента по индексу
# numbers = [10, 20, 30, 40, [2, 3, 4]]
# second_item = numbers.pop()
# print(numbers)
# print(second_item)
# # удаление и возврат последнего элемента
# numbers = [10, 20, 30, 40]
# last_item = numbers.pop() # возвращенный элемент можно присвоить переменной
# print(numbers)
# print(last_item)
#
# # поиск первого вхождения элемента "banana"
# #           0         1
# fruits = ["apple", "banana", "cherry", "banana", "cherry"]
# banana_index = fruits.index("banana")
# print(banana_index)
#
# # поиск первого вхождения "banana", начиная с индекса 2
# #           0       1           2
# fruits = ["apple", "banana", "cherry", "banana", "cherry"]
# banana_index = fruits.index("banana", 2)
# print(banana_index)
#
# # поиск "cherry" в диапазоне индексов от 1 до 4 (не включая 4)
# #           0           1       2       3           4
# fruits = ["cherry", "banana", "cherry", "banana", "cherry"]
# banana_index = fruits.index("cherry", 1, 4)
# print(banana_index)
#
# # поиск индекса элемента, которого нет в списке
# # fruits = ["apple", "banana", "cherry", "banana"]
# # index = fruits.index("orange")  # вызовет ValueError
#
# fruits = ["apple", "banana", "cherry", "banana", ["banana", "ananas"], []]
# search = "banana"
#
# for idx, fruit in enumerate(fruits):
#     if type(fruit) == list:
#         count_of_matches = fruits[idx].count(search)
#         for n in range(count_of_matches):
#             fruits[idx].remove(search)
#     elif search != fruit:
#         fruits.remove(search)
#
# print(fruits)

calendar = [
    ("понедельник", (("8:30", True, 30), ("9:30", False, 0))),
    ("вторник", (("8:30", True, 30), ("9:30", False, 0))),
    ("среда", (("8:30", True, 30), ("9:30", False, 0))),
]

'''
Сегодня понедельник

У вас есть митинги на
- 8:30 с продолжительностью в 30 минут
'''

for day, time in calendar:
    for time1,bo,dauert in time:
        if bo == True:
            print(f"""Сегодня {day}

У вас есть митинги на
- {time1[0]} с продолжительностью в {time1[2]} минут
""")
        else:
            continue

''''''


