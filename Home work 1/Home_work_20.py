'''Простое число
Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя) и возвращает булевый результат.
Данные:
n = 17
Пример вывода:
Число 17 является простым
'''
def is_prime(n: int) -> bool:

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = 17
print(f"Число {n} {'является' if is_prime(n) else 'не является'} простым")

'''
Фильтрация чисел по чётности
Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел, возвращая только те, которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
'''
def filter_numbers(filter_type, *args):
    if filter_type == "even":
        return [x for x in args if x % 2 == 0]
    elif filter_type == "odd":
        return [x for x in args if x % 2 != 0]
    else:
        return "Некорректный фильтр"
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

'''
Объединение словарей
Напишите функцию, которая принимает любое количество словарей и объединяет их в один. Если ключи повторяются, используется значение из последнего словаря.
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
Пример вызова:
print(merge_dicts(dict1, dict2, dict3))
Пример вывода:
{'a': 1, 'b': 3, 'c': 4, 'd': 5}
'''
def merge_dicts(*dicts: dict) -> dict:

    merged = {}
    for d in dicts:
        merged.update(d)
    return merged

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
print(merge_dicts(dict1, dict2, dict3))