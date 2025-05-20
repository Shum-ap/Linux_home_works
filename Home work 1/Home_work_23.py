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

''''''

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]
def filter_sales(sales):
