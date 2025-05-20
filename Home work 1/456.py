# Напишите программу, которая принимает от пользователя один символ и
# выводит его код в таблице Unicode и его принадлежность к диапазону ASCII
# (True/False).
#
# Пример вывода:
#
# Введите символ: A
#
# Код Unicode: 65
#
# ASCII символ: True


char = input("Введите символ: ")
unicode_code = ord(char)
is_ascii = 0 <= unicode_code <= 127

print("Код Unicode:",unicode_code)
print("ASCII символ:",is_ascii)
