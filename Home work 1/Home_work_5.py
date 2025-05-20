#1
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b

print("Числа в порядке возрастания: ",a,b,c, sep=",")

#2
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Год является высокосным.")

else:
    print("Год не является высокосным.")


