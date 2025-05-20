# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# i = 1
# while i <= 10:
#     print(i)
#     if i == 5:
#         break # Прерывание цикла, когда i станет равно 5
#     i += 1

# while True:
#      user_input = input("Введите 'exit', чтобы завершить цикл: ")
#      if user_input == "exit":
#          break
#      print("Вы ввели:", user_input)

# i = 0
# while i < 5:
#     i += 1
#     if i % 2 == 0:
#          continue # Пропускаем итерацию, когда i четное
#     print(i)

result = 1
while True:
    user_input = input("Введите число для перемножения: ")
    if user_input == "0":
        print("Пропуск итерации")
        continue # Пропускаем оставшуюся часть текущей итерации
    if user_input == "exit":
        print("Выход из программы")
        break # Прерывание цикла
    result *= int(user_input)
    print("Результат перемножения:", result)