#1
char = input("Введите символ: ")
unicode_code = ord(char)
is_ascii = 0 <= unicode_code <= 127

print("Код Unicode:",unicode_code)
print("ASCII символ:",is_ascii)

#2
text = input("Введите строку: ")
start = int(input("Введите начальный индекс: "))
end = int(input("Введите конечный индекс: "))
if end > len(text):
    substring = text[start:] + "_" * (end - len(text))
else:
    substring = text[start:end]
print("Подстрока: " ,substring)

#3

text = input("Введите строку: ")
sim = input("Введите символ: ")
count = 0
index = 0
while index < len(text):
    if text[index]  == sim:
        count += 1
    index += 1
print("Символ", sim, "встречается", count, "раз(a).")

#4
text = input("Введите строку: ")
i = 0
numb = "0123456789"
world = ""
word = text[::-1]

while i < len(text):

    if word[i] not in numb:
        world += word[i]
    i += 1

print("Рузультат: ",world)