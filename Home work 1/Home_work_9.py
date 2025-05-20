#1
num = int(input("Введите число: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i * j, end="\t")
    print()

#2
num = int(input("Введите число: "))

for str in range(1, num + 1):
    for col in range(1, str + 1):
        print(col, end=" ")
    print()

#3
text = input("Введите строку")
result = ""
for sim in text:
    if sim not in result:
        result += sim
print("Результат: ", result)
