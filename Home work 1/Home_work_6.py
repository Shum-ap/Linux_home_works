  # 1.1
num = float(input("Введите вещественное число: "))
if num > 0:
 rounded_num = int(num + 0.5)
else:
 rounded_num = int(num - 0.5)
print("Округленное значение:", rounded_num)

# 1.2
import math
num = float(input("Введите вещественное число: "))
rounded_num = math.floor(num + 0.5) if num > 0 else math.ceil(num - 0.5)
print("Округленное значение:", rounded_num)

# 2
import math
a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))
hypotenuse = math.sqrt(a**2 + b**2)
print("Длина гипотенузы:", hypotenuse)
