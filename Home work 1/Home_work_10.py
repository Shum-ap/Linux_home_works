# #!
#
# coins = [50, 10, 5, 2, 1]
#
# vvod = int(input("Введите стоимость товара: "))
#
# print("Для оплаты внесите следующие монеты: ")
#
# for coin in coins:
#     count = vvod // coin
#     if count > 0:
#         print("Внесите монеты номиналом: ", coin, ":", count, sep="")
#         vvod -= count * coin

#2

numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]

print("Изначальный список:", numbers)

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = numbers[i] ** 2

print("Измененный список: ", numbers)
