# 1
a = int(input("Введите четырехзначное число: "))
print("Сумма цифр числа: ", a %10 + a %100 //10 + a %1000 //100 + a %10000 //1000)
# 2
cool1 = int(input("Введите первое число: "))
cool2 = int(input("Введите второе число: "))
print('Результат: ',end="")
print(cool1 * cool2, cool1,cool2, sep="-")
# 3
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
zeloe = int(a / b)
ost = a - (zeloe * b)
print("Остаток от деления:", ost)
print("Целочисленное деление:", zeloe)