"""
- Типы данных
- Математические операции (сложение, вычитание,
умножение, деление, возведение в степень,
равенство, неравенство, деление нацело,
получение остатка от деления)
- Условия (if, цикл while)
- isinstance(date, type) проверка на тип данных
"""

#Типы данных
int()    # 5
str()    # "text"
bool()   # True , False
float()  # 5.0

# 0.1 + 0.2 != 0.3
print(f'0.1 + 0.2 == 0.3', (0.1 + 0.2) == 0.3)
print(f'0.3 == 0.3', (0.3 == 0.3), f', but 0.1 + 0.2 = {0.1+0.2}')
# В дробных числах Python имеет погрешности

a = 20
b = 6

#Математические операции
# + Сложение
print(f'a + b = {a+b}')
# - Вычитание
print(f'a - b = {a-b}')
# * Умножение
print(f'a * b = {a*b}')
# / Деление
print(f'a / b = {a/b}') #type = float
# ^ Возведение в степень
print(f'a^b = {a**b}')
# == Равенство/Неравенство
print(f'a == b', a==b) #type = bool
print(f'a != b', a!=b) #type = bool
# // Деление нацело
print(f'a // b = {a//b}')
# % Получение остатка от деления
print(f'a % b = {a%b}')


#Условия
age = 25
if 18 > age >= 6:
    print('Пора в школу')
elif 22 > age >= 18:
    print('Пора в универ')
elif 60 > age >= 22:
    print("Пора на работу")
else:
    print('Пора на пенсию')

while age >= 18:
    print(age)
    age -= 1
    count = 10
    while count >= 5: #вложенный цикл
        print(f'count = {count}')
        count -= 1
print('END')


isinstance(123, int) #True
isinstance('text', str) #True
isinstance(123.0, int) #False, it is bool
#True == 1
#False = 0
isinstance(True, int) #True
isinstance(False, int) #True

