'''Одно слово
Напишите программу, которая обрабатывает список из строк и удаляет все строки,
содержащие более одного слова,
 а также преобразует оставшиеся строки к нижнему регистру.
Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']'''

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
new_list = [t.lower() for t in text_list if len(t.split()) == 1]

print("Обработанный список:", new_list)



'''Обновление цен товаров
Дан список товаров с ценами. Программа должна применить скидку к каждому товару
 и добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
Пример вывода:
Введите скидку (в процентах): 17
Товар          Старая цена    Новая цена
Laptop           1200.00$        996.00$
Mouse              25.00$         20.75$
Keyboard           75.00$         62.25$
Monitor           200.00$        166.00$'''


usr_inp = int(input("Введите скидку (в процентах): "))
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

print(f"{"Товар":<10}{"Старая цена":<15}{"Новая цена"}")
for i in products:
    print(f"{i[0]:<10}{i[1]:>10.2f}${(100 - usr_inp) / 100 * i[1]:>13.2f}$")

''''''

import copy
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
disc = float(input("Введите скидку (в процентах): "))

products_copy = copy.deepcopy(products)

for product in products_copy:
    old_price = product[1]
    new_price = old_price * (1 - disc / 100)
    product.append(round(new_price, 2))

print(f"{'Товар':<15}{'Старая цена':<15}{'Новая цена':<15}")
for product in products_copy:
    print(f"{product[0]:<15}{format(product[1], '.2f') + '$':<15}"
          f"{format(product[2], '.2f') + '$':<15}")
''''''
