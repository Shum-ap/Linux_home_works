# # Проверка кодировки
# char = input("Введите символ: ")
# code = ord(char)
# print(f"Код Unicode: {code}")
# print(f"ASCII символ: {code < 128}")
#
# # Подстрока с заполнением
# text = input("Введите строку: ")
# start = int(input("Введите начальный индекс: "))
# end = int(input("Введите конечный индекс: "))
# substring = text[start:end] + "_" * max(0, end - len(text))
# print(f"Подстрока: {substring}")
#
# # Подсчёт символа
# text = input("Введите строку: ")
# char = input("Введите символ: ")
# count = text.count(char)
# print(f"Символ {char} встречается {count} раз(а).")
#
# # Инвертирование строки без цифр
# text = input("Введите строку: ")
# inverted = "".join([c for c in text if not c.isdigit()])[::-1]
# print(f"Результат: {inverted}")

x = 0
while True:
    if x ==10:
        break

    x += 1
    print(x)
else:
    print("success!")
