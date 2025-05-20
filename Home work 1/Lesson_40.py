# # Создание frozenset
# frozen_set1 = frozenset([1, 2, 3])
# frozen_set2 = frozenset([4, 5, 6])
# # Создание множества, содержащего frozenset
# set_of_frozensets = {frozen_set1, frozen_set2}
# print(set_of_frozensets)
'''Популярные слова
Реализуйте функцию, которая принимает любое количество строк с текстом.
Функция должна возвращать подсчет самых популярных слов в количестве,
переданном в функцию. Программа должна игнорировать регистр слов. Выведите 5
самых популярных слов и их количество.
Данные:
'''
from collections import Counter

def most_common_words(*texts):
    text = ' '.join(texts).lower()

    for ch in '.,!?;:':
        text = text.replace(ch, '')

    words = text.split()
    counter = Counter(words).most_common(5)

    print("5 самых популярных слов:")
    for word, count in counter:
        print(f"{word}: {count}")

text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."

most_common_words(text1, text2, text3)



'''Группировка задач по категории
Реализуйте функцию, которая принимает словарь задач с категориями и группирует
задачи по их категориям.
Данные:

Пример вывода:
Группировка по категориям:
{
 'работа': ['task1', 'task4'],
 'учёба': ['task2', 'task5'],
 'развлечения': ['task3']
}
'''
from collections import defaultdict

def group_tasks_by_category(tasks):
    grouped = defaultdict(list)
    for task, category in tasks.items():
        grouped[category].append(task)
    return dict(grouped)

tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба",
}

result = group_tasks_by_category(tasks)
print("Группировка по категориям:")
print(result)

