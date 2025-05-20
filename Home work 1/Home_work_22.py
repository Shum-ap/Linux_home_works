'''Выбор заказов
У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:

Отбирает заказы дороже 500.

Создаёт список названий отобранных продуктов в алфавитном порядке.

Возвращает итоговый список названий.'''

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

def filter_orders(orders):
    filtered = [order for order in orders if order["price"] > 500]
    product_names = sorted([order["product"] for order in filtered])
    return product_names

result = filter_orders(orders)
print(result)

'''Статистика продаж
Дан список продаж в виде кортежей (товар, количество, цена).
Напишите программу, которая:

Вычисляет общую выручку для каждого товара.

Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.'''

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]
def filter_sales(sales):
    product_sales = {}
    for product, quantity, price in sales:
        product_sales.setdefault(product, 0)
        product_sales[product] += quantity * price
    return sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
print(filter_sales(sales))

