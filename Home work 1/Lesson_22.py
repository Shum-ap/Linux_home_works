# # name = "Alice"
# # age = 30
# # text = "My name is {} and I am {} years old."
# # print(text.format(name, age))
# # print(text.format(age, name))
# # print(text.format(age)) # error
#
# text = "My name is {name} and I am {age} years old. Are you also {age} years old?"
# print(text.format(name="Bob", age=25))
# # print(text.format(age=25, name="Bob"))
#
# text = "Her name is {0} and she is {1} years old. {0} loves Python."
# #                         0      1
# print(text.format("Anna", 28))
#
# text = "The {} is {color}."
# print(text.format("sky", color="blue"))
# # print(text.format(color="blue", "sky")) # error\
#
# # number = 40
# # text = 'hi'
# # # f-строки
# # text_fstring = f"start_{number:5}_end"
# # # Метод format()
# # text_format = "start_{:5}_end"
# # print(text_fstring)
# # print(text_format.format(text))
#
# # Заполнение нулями
# # number = 40
# # text = f"{number:0>5}"
# # print(text)
# #
# # # Заполнение нижним подчеркиванием
# # text = f"{'Python':_^13}"
# # print(text)
#
# text = "Python"
#
# # ljust(): выравнивание по левому краю
# print(text.ljust(15))
# print(text.ljust(15, '-'))
# # rjust(): выравнивание по правому краю
# print(text.rjust(15))
# print(text.rjust(15, '-'))
# # center(): выравнивание по центру
# print(text.center(15))
# print(text.center(5, '-'))
'''
Формат даты
Напишите программу, которая принимает дату в виде числа, месяца и года,
а затем выводит её в формате "dd/mm/yyyy", где день и месяц всегда состоят из двух цифра.

Пример вывода:
    Введите день: 3
    Введите месяц: 7
    Введите год: 2024
    Дата: 03/07/2024
'''

# day = int(input("Введите день: "))
# month = int(input("Введите месяц: "))
# year = int(input("Введите год: "))
#
#
# full_date = "{}/{}/{}".format(day, month, year)
#
# print("Дата:", full_date)
#


'''
Счетчик слов
Напишите программу, которая обрабатывает строку и выводит её, добавив к каждому
слову его порядковый номер, выравнивая текст по левому краю с длиной в 15 символов.
Слова выводите с большой буквы.

Пример вывода:
    Введите строку: Hello world Python is great
    1. Hello
    2. World
    3. Python
    4. Is
    5. Great
'''

# text = input("Введите строку: ")
text = "Hello world Python is great"
words = text.split()
index = 0
count = 1

while index < len(words):
    word = words[index].capitalize()
    print(f"{count}. {word.ljust(15)}")
    index += 1
    count += 1

# # text = input("Введите строку: ").split()
# text = "Hello world Python is great".split()
# for i in range(len(text)):
#     new=f"{i+1}. {text[i].capitalize()}"
#     print(f"{new:<15}")
#     print(f"{i+1}. {text[i].capitalize():<15}")