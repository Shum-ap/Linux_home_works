'''Список квадратов
Создайте список, содержащий квадраты всех чётных чисел из диапазона от 1 до
заданного пользователем числа включительно.
Пример вывода:
Введите конец диапазона: 20
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]'''

# t = int(input("Введите конец диапазона: "))
# res = [x**2 for x in range(2, t + 1, 2)]
# print(res)
#


'''Фильтрация по символу
Создайте новый список, исключив все строки, содержащие введённый
пользователем символ.
Данные:
words = ["apple", "cherry", "kiwi", "banana", "orange"]
Пример вывода:
Исключить символ: r
['apple', 'kiwi', 'banana']
'''
#
# words = ["apple", "cherry", "kiwi", "banana", "orange"]
# s = input("Исключить символ: ")
#
# res = [x for x in words if s not in x]
#
# print(res)

'''База данных обитателей джунглей
Данные:
animals = ["тигр", "слон", "обезьяна", "змея"]
weights = [250, 4000, 15, 5]
Пример вывода:
['Тигр весит 250 кг', 'Слон весит 4000 кг', 'Обезьяна весит 15 кг', 'Змея весит
5 кг']
Самое лёгкое животное: змея'''

# animals = ["тигр", "слон", "обезьяна", "змея"]
# weights = [250, 4000, 15, 5]
#
# zoo = []
# min_weight = weights.index(min(weights))
# for animal, weight in zip(animals, weights):
#     zoo.append( f"{animal.capitalize()} весит {weight} кг")
#
#
#
# print(zoo)
# print(f"Самое лёгкое животное: {animals[min_weight]}")

'''Группы слов
Группируйте слова по длине в обратном порядке, отсортированные по алфавиту
внутри группы.
Данные:
words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]
Пример вывода:
Группы слов: [['banana', 'cherry'], ['apple', 'grape', 'melon'], ['kiwi',
'pear']]'''


words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]

sorted_words = sorted(words, key=len, reverse=len)

for word in sorted_words:
    print(f"{len(word)}: {word}")

''''''
words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]
words_sorted = sorted(words, key=lambda word: (-len(word), word))

grouped_words = []
current_group = []
current_length = len(words_sorted[0])

for word in words_sorted:
    if len(word) == current_length:
        current_group.append(word)
    else:
        grouped_words.append(current_group)
        current_group = [word]
        current_length = len(word)
grouped_words.append(current_group)

print("Группы слов:", grouped_words)

'''words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]
grouped_by_length = []

# words.sort()
words.sort(key=len, reverse=True)

# Группировка строк по длине
for word in words:
    if not grouped_by_length or len(grouped_by_length[-1][0]) != len(word):
        grouped_by_length.append([])
    grouped_by_length[-1].append(word)

print("Сгруппированные строки по длине:", grouped_by_length)'''


