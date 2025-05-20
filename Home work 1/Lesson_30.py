'''Замена слов на основе условий.

Если длина слова больше 5 символов, оставить его без изменений. Если длина слова от 3 до 5 символов,
заменить слово на 'medium'. Если длина слова меньше 3 символов, заменить его на 'short'.'''

# words = ["hi", "apple", "banana", "cat", "blueberry", "on"]
# new_words= [word if len(word) > 5 else("medium" if len(word) <= 3 else "short") for word in words]
# print(new_words)

# names = ["John", "Anna", "Zoe", "Mark"]
# formatted_names = [name.lower() if len(name) > 3
# else name.upper() for name in names]
# print(formatted_names)

# matrix = [[7, 8], [9, 10], [11, 12]]
# flattened = [value * 2 for row in matrix for
# value in row]
# print(flattened)


# code = '''
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
#
# for name, age in zip(names, ages):
#     hex_age = format(age, 'x')
#     print(f"{name} - hex age: {hex_age}")
#     print(f"{name} is {hex_age} years old.")
# '''
#
# # Конвертация текста в байты, затем в hex
# hex_output = code.encode('utf-8').hex()
#
# print(hex_output)

'''Напишите программу, которая создает список из всех уникальных символов строки, 
за исключением пробелов.
Данные:
text = "hello world"
Пример вывода:
Уникальные символы: ['l', 'r', 'd', 'h', 'o', 'w', 'e']'''

# text = "hello world"
# text2 = list(set(text.replace(" ", "")))
# print("Уникальные символы:", text2)
#
# set1 = {10, 20, 30}
# set2 = {20, 30, 40}
# result = set1 - set2
#
# print(result)
#
#
# set1 = {1, 2, 3}
# set2 = {4, 5, 6, 1}
# print(set1 != set2)

'''
Напишите программу, которая создаёт новый словарь, где значения из исходного
 словаря становятся ключами, а ключи — значениями.
Данные:
original_dict = {"a": 1, "b": 2, "c": 3}
Пример вывода:
Инверсированный словарь: {1: 'a', 2: 'b', 3: 'c'}
'''
original_dict = {"a": 1, "b": 2, "c": 3}
i = dict(zip(original_dict.values(), original_dict.keys()))
print("Инверсированный словарь:", i)

''''''
original_dict = {"a": 1, "b": 2, "c": 3}

inverted_dict = {}

for key, value in original_dict.items():
    inverted_dict[value] = key

print("Инверсированный словарь:", inverted_dict)
