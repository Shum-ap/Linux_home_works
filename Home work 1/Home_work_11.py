'''
1. Звёздочки вместо чисел
Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"
'''
txt = "My number is 123-456-789"
result = ""

for i in txt:
    if i.isdigit():
        result += "*"
    else:
        result += i

print(result)


'''
2. Количество символов
Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести
только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите
повторяющиеся символы только один раз.
text = "Programming in python"
'''
txt = "Programming in python"
print("Строка: ", txt)
txt = txt.lower()
result = ""
for i in txt:
    if txt.count(i) > 1 and i not in result:
        print("Символ ", "'" + i + "'", "встречается", txt.count(i), "раз(а)")
        result += i


'''
3. Увеличение чисел
Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.
'''


txt = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split()
tx = ""

for i in txt:
    if i.replace('.', '', 1).isdigit():
        num = float(i) * 10
        tx += str(num) + " " if num.is_integer() else num + " "
    else:
        tx += i + " "

print("Результат:", tx.strip())


text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split()
tx = ""

for i in text:
    if i.replace('.', '', 1).isdigit():
        tmp = float(i) * 10
        tx += str(tmp) + " "
    else:
        tx += i + " "

print("Результат:", tx.strip())

