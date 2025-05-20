# # Список с числами и списками
# list_elements = [[1, 2, 3], [4, 5], 6, [7], [8, 9]]
# print(list_elements)
# # Кортеж со списками
# lists_tuple = ([1, 2], [3, 4], [5, 6])
# print(lists_tuple)
# # Список со списками
# lists = [[1, 2], [3, 4]]
# print(lists)
#
'''Номер покупки
Задача: Дан список покупок. Найдите какой по счету (начиная с единицы) товар с
названием "Milk". Если товара нет, выведите сообщение об отсутствии.
Данные: products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
Пример вывода: Товар "Milk" в списке покупок: 4
'''

# products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
#
# if "Milk" in products:
#     index = products.index("Milk") + 1
#     print(f'Товар "Milk" в списке покупок: {index}')
# else:
#     print('Товар "Milk" отсутствует в списке покупок')

'''Список уникальных слов
Задача: Дан текст. Программа должна:
● Разбить текст на слова.
● Создать список уникальных слов в алфавитном порядке (не учитывая
регистр).
● Вывести количество уникальных слов.
Данные: text = "Python is a great programming language. Python is popular and
powerful."
Пример вывода: Количество уникальных слов: 9 Уникальные слова: ['a', 'and', 'great',
'is', 'language', 'popular', 'powerful', 'programming', 'python']'''


import copy

text = "Python is a great programming language. Python is popular and powerful."

text = text.lower()
for ch in ".!,?:;()\"'":
    text = text.replace(ch, "")

words = text.split()

words_copy = copy.copy(words)

unique_words = sorted(set(words_copy))

print("Количество уникальных слов:", len(unique_words))
print("Уникальные слова:", unique_words)


'''Самое длинное слово
Задача: Дано предложение. Найдите самое длинное слово и выведите это слово с
его длиной.
Данные: sentence = "Programming in Python is both fun and educational"
Пример вывода: Самое длинное слово: Programming Длина слова: 11'''

import copy

sentence = "Programming in Python is both fun and educational"

# Разбиваем предложение на слова
words = sentence.split()

# Копируем список слов
words_copy = copy.copy(words)

# Находим самое длинное слово в копии
longest_word = ""
for word in words_copy:
    if len(word) > len(longest_word):
        longest_word = word

# Вывод
print(f"Самое длинное слово: {longest_word}")
print(f"Длина слова: {len(longest_word)}")

''''''

sentence = "Programming in Python is both fun and educational"
list_of_words1 = sentence.split(" ")
most_lange_word = list_of_words1[0]
for i in list_of_words1:
    if len(i) > len(most_lange_word):
        word = i
print('Слово: ', most_lange_word, ' длина:', len(most_lange_word))


'''Перемещение в конец
Задача: Напишите программу, которая перемещает все элементы списка, меньше 5,
в конец списка, сохраняя порядок остальных элементов.
Данные: numbers = [4, 7, 1, 6, 3, 8, 2]
Пример вывода: Перемещённые элементы: [6, 7, 8, 4, 1, 3, 2]'''

import copy

numbers = [4, 7, 1, 6, 3, 8, 2]
nums_copy = copy.copy(numbers)

main_part = []
moved_part = []

for num in nums_copy:
    if num >= 5:
        main_part.append(num)
    else:
        moved_part.append(num)

result = main_part + moved_part

print("Перемещённые элементы:", result)
