#1
data = {"a": 1, "b": 2, "c": 1, "d": 3}
revers_dikt = {}

for key, value in data.items():
    revers_dikt.setdefault(value, []).append(key)

print("Перевернутый словарь:", revers_dikt)

#2
words = ["anna", "bennet", "john"]
w_leter_count = {}

for word in words:
    leter_count = {}
    for leter in word:
        leter_count[leter] = leter_count.get(leter, 0) + 1
    w_leter_count[word] = leter_count

print(w_leter_count)

#3
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}

groups = {
    "Отличники": {},
    "Хорошисты": {},
    "Троечники": {},
    "Не сдали": {}
}

for name, score in students.items():
    if score >= 85:
        groups["Отличники"][name] = score
    elif score >= 70:
        groups["Хорошисты"][name] = score
    elif score >= 50:
        groups["Троечники"][name] = score
    else:
        groups["Не сдали"][name] = score

print("Распределение по группам:")
print(groups)

''''''
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}

groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
student_groups = {group: {} for group in groups}

for name, score in students.items():
    if score >= 85:
        group_name = "Отличники"
    elif 70 <= score < 85:
        group_name = "Хорошисты"
    elif 50 <= score < 70:
        group_name = "Троечники"
    else:
        group_name = "Не сдали"

    student_groups[group_name][name] = score

print("Распределение по группам:")
print(student_groups)

