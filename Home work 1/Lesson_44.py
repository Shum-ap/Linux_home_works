# def function_name(param1, param2):
#  """
#  Описание функции.
#  :param param1: Описание первого параметра.
#  :param param2: Описание второго параметра.
#  :return: Описание возвращаемого значения.
#  """
#  pass
# print(function_name.__doc__)
#
# (name):input()
# def function_name(name):
#  """
#  Функция принимает имя и возвращает строку приветствия.
#
#  :param name: Имя пользователя.
#  :return: Приветственное сообщение.
#  """
#  return f"Hello, {name}!"
#  print(function_name.__doc__)
#  help()
#
# def add(a: int, b: int) -> int:
#  return a + b
# num: int = 10

# def modify_value(n: int) -> None:
#  """Изменяет значение переменной внутри функции (не влияет на оригинал)."""
#  print(f"До изменения в функции: {n}, id: {id(n)}")
#  n += 1 # Создаётся новый объект
#  print(f"После изменения в функции: {n}, id: {id(n)}")
# num = 10
# modify_value(num)
# print(f"Вне функции: {num}, id: {id(num)}")
#
# def modify_list(lst: list) -> None:
#  """Добавляет элемент в список (изменяет оригинальный объект)."""
#  print(f"До изменения в функции: {lst}, id: {id(lst)}")
#  lst.append(99) # Изменение оригинального списка
#  print(f"После изменения в функции: {lst}, id: {id(lst)}")
# my_list = [1, 2, 3]
# modify_list(my_list)
# print(f"Вне функции: {my_list}, id: {id(my_list)}")

# def safe_modify_list(lst: list) -> list:
#  """Работает с копией списка, оставляя оригинальный неизменным."""
#  copy_lst = lst.copy()
#  copy_lst.append(99)
#  return copy_lst
# original_list = [1, 2, 3]
# new_list = safe_modify_list(original_list)
# print(f"Оригинал: {original_list}")
# print(f"Копия: {new_list}")

def modify_string(text: str) -> str:
 text += "!"
 return text
original = "Hello"
modify_string(original)
print(original)