"""
- f-строка, разделитель (sep, end)
- Условия в циклах (and / or)
- continue, break в циклах. выход из цикла естественным образом
- Цикл FOR
- Функция enumerate
- Операции со списками: append(), insert(), len(), remove(), pop()
- Кортежи tuple()
- Срезы
- Словари и методы keys(), values(), items(), get()
"""

# f строка, разделитель (sep)
name = "Bob"
city = "Moscow"
print(f'{name} живет в {city}')

print(name, city, sep='+++')
print(name, city, sep='+++', end='===')
print(name, city, sep='+++', end='===')

print(name, city, sep='+++', end='\n')
print(name, city, sep='+++', end='\n')



# Условия в циклах (and / or)
age = 20

while age >= 10:
    if age % 2 == 0 and age % 8 != 0 or age % 10 != 0:
        print(age)
    age -= 1
print('END')


# or - Хотя бы 1 из условий должно быть истинным
"""
1 or 1 = 1
1 or 0 = 1
0 or 1 = 1
0 or 0 = 0
"""

# and - Все условия должны быть истинными
"""
1 and 1 = 1
1 and 0 = 0
0 and 1 = 0
0 and 0 = 0
"""

# continue в циклах
age = 20

while age >= 5:
    age -= 1
    if age == 10:
        continue #не выводит age = 10, а переходит в начало цикла
        # break - прерывает цикл полностью (лучше не злоупотреблять, стараться выходит из цикла естественным образом
    print(age)
else:
    print('Я вышел из цикла естественным образом') #при break не сработает

print('END')

# Цикл FOR
for item in 1, 2, 3, 4, 6, True, "Строка":
    print(item)

#PEP8 - правило написания понятных названия для переменной, которая перебирается

names =['Bob', 'Ann', 'John']
for name in names:
    print(name)

for i in range(10): # генератор чисел от 0 до 9
    print(i)

print('range(start, stop, step)')
for i in range(2, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

# Функция enumerate( )
numbers = [1, 2, 3, 4, 5]
for i in enumerate(numbers):
    print(i)
"""
Возвращает кортеж
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 5)
может быть полезным в качестве счетчика
"""

for i, num in enumerate(numbers, start=5):
    print(i, num)


# Операции со списками
numbers = [1, 2, 3, 4, 5]
numbers.append(10) #добавляет значение в конец списка
print(numbers)

numbers.insert(0, 15) #добавляет значение в указанное место в списке
numbers.insert(4, -2) #вставили значение -2 на позицию 4
print(numbers)

numbers.remove(2) # удаляет первый попавшийся элемент по значению
numbers.pop(1) # удаляет значение элемент по индексу

print(len(numbers)) # len () количество значений в списке

print(names) # ['Bob', 'Ann', 'John']
names[0] = "Marry"
print(names) # ['Marry', 'Ann', 'John']

# Кортежи tuple() - список с неизменяемым типом данных за счет чего работает немного быстрее
tuple()

# Срезы
names = ['Bob', 'Ann', 'John', 'Mish', 'Rob']
names[0:3] # ['Bob', 'Ann', 'John'] - вывод элементов от 0 до 2 индекса
names[2:] # ['John', 'Mish', 'Rob']
# names[start, stop, step]
names[1::2] # ['Ann', 'Mish'] - с первого индекса с шагом 2
names[::-1] # ['Rob', 'Mish', 'John', 'Ann', 'Bob'] - reverse

# Словари {key:value}
names_dict = {'fr1':'Bob',
              'fr2':'Ann',
              'fr3':'John'
              }
names_dict['fr1'] # Bob
names_dict.keys() # dict_keys(['fr1', 'fr2', 'fr3'])
names_dict.values() # dict_values(['Bob', 'Ann', 'John'])

# items() - получить все значения в виде кортежа
names_dict.items() # dict_items([('fr1', 'Bob'), ('fr2', 'Ann'), ('fr3', 'John')])
for key,value in names_dict.items():
    print(key,value)

"""
fr1 Bob
fr2 Ann
fr3 John
"""
# get() - более безопасный метод. если ключ отсутствует в словаре, выведет None
# names_dict['fr10'] # Error
names_dict.get('fr10') # None