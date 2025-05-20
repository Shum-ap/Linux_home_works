# fruits = ["apple", "banana", "cherry"] # Список со строками
# print(fruits)
# numbers = [1, 2, 3] # Список с числами
# print(numbers)
#
# mixed_list = [42, "Python", 3.14, True, [1, 2,
# 3]]
# print(mixed_list)
#
# my_list = [1, 2, 3, 4]
# print(my_list)
#
# empty_list = []
# print(empty_list)
#
# my_list = list()
# print(my_list)
#
# my_list = ["apple", "banana", "cherry", "date"]
# # Доступ к первому элементу
# print(my_list[0])
# # Доступ к последнему элементу с положительным индексом
# print(my_list[3])
# # Доступ к последнему элементу с отрицательным индексом
# print(my_list[-1])
# # Доступ к первому элементу с отрицательным индексом
# print(my_list[-4])

# my_list = [0, 1, 2, 3, 4, 5, 6]
# # Срез с 1-го по 4-й элемент (не включительно)
# print(my_list[1:4])
# # Срез каждого второго элемента
# print(my_list[::2])
# # Срез каждого второго элемента в обратном порядке
# print(my_list[::-2])
# # Срез от 4-го элемента до начала
# print(my_list[4::-1])
# # Срез с 3-го элемента до конца
# print(my_list[3:])
# # Копия списка с помощью среза
# print(my_list[:])

# my_list = [0, 1, 2, 3, 4, 5, 6]
# # Срез от -4-го до -1-го элемента
# print(my_list[-4:-1])
# # Срез от -2-го до -5-го элемента
# print(my_list[-2:-5:-1])
# # Срез списка в обратном порядке
# print(my_list[::-1])

# my_list = ["apple", "banana", "cherry"]
# # Изменим второй элемент (с индексом 1)
# my_list[1] = "blueberry"
# print(my_list)

# my_list = [10, 20, 30, 40, 50]
# # Заменим второй и третий элементы
# my_list[1:3] = [200, 300]
# print(my_list)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined_list = list1 + list1 + list2
# print(combined_list)
#
# repeated_list = [0] * 5
# print(repeated_list)
# my_list = [1, 2, 3]
# repeated_list = my_list * 3
# print(repeated_list)

# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)
# print(6 in my_list)
# my_list = ["apple", "banana", "cherry"]
# print("apple" in my_list)
# print("app" in my_list) # Ищет полное совпадение элемента
# print("app" in my_list[0])  # Ищет частичное совпадение

# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))

# word = "python"
# my_list = list(word) # Строка "разбивается" на отдельные символы
# print(my_list)
# print(type(my_list))
#
# my_range = range(1, 11, 2)
# print(my_range)
# print(type(my_range))
# my_list = list(my_range)
# print(my_list)
#
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = [1, 3, 0]
# # Сравнение на равенство
# print(list1 == list2)
# print(list1 == list3)
# # Сравнение на неравенство
# print(list1 != list2)
# print(list1 != list3)
# ### Сравнение на больше/меньше, больше или равно/меньше или равно
# print(list1 < list2)
# print(list3 > list1)
# print(list1 <= list2)
# print(list1 >= list3)



#
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = [1, 3, 0]
# # Сравнение на равенство
# print(list1 == list2)
# print(list1 == list3)
# # Сравнение на неравенство
# print(list1 != list2)
# print(list1 != list3)
# ### Сравнение на больше/меньше, больше или равно/меньше или равно
# print(list1 < list2)
# print(list3 > list1)
# print(list1 <= list2)
# print(list1 >= list3)

# list1 = [1, 2.6, 2]
# list2 = [1, 2, 3]
# # int и float можно сравнивать между собой
# print(list1 < list2)
#
# list1 = [1, 2, "apple"]
# list2 = [1, 2, 3]
# # Попытка сравнить числовое значение с строкой вызовет ошибку TypeError
# print(list1 < list2)
#
# list1 = [1, 2, "apple"]
# list2 = [1, 3, 10]
# print(list1 < list2) # Вернёт True, так как 2 < 3, сравнение остановится до строки "apple"

# my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#  print(item)
#
#  my_strings = ["apple", "banana", "cherry"]
#  for word in my_strings:
#   for letter in word:
#    print("letter:", letter)
#   print()

# my_strings = ["cat", "dog"]
# for word in my_strings:
#     for letter in word:
#         print(letter, end="")
# print()
#
matrix = [
    [2, 3, 4],
    [5, 6, 10],
    [2, 4, 5],
]


for row in matrix:
    for i in range(len(row)):
        if i == len(row) - 1:
            print(row[i], end="")  # последний элемент — без запятой
        else:
            print(row[i], end=", ")  # остальные — с запятой
    print()  # переход на новую строку

for row in matrix:
    for j in row:
        if row == matrix[-1] and row[-1] == j:
            print(j, end="")
            break
        print(j, end=", ")
    print()