#1
value1 = bool(int(input("Enter first value (1 = True, 0 = False): ")))
value2 = bool(int(input("Enter second value (1 = True, 0 = False): ")))
print("and:", value1 and value2)
print("or:", value1 or value2)
print("not:", not value1)
print("equal:", value1 == value2)
print("not equal:", value1 != value2)
#2

light_on = bool(int(input("Свет включен? (1 = да, 0 = нет): ")))
window_open = bool(int(input("Окно открыто? (1 = да. 0 = нет): ")))
both_cond = light_on and window_open
at_last_one = light_on or window_open
print("Оба условия выполнены: ", both_cond)
#3
cost = 30
mb = 500
dop_cost = 0.2
mb_oll = int(input("Введите использованные мегабайты: "))
dop_cost = (mb_oll - 500) * dop_cost
vsego_cost = cost + (mb_oll >= mb) * dop_cost
print("Общая стоимость:", vsego_cost)