# Задача №25. Решение в группах

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

text = 'a a a b c a a d    c d d'.split()
my_dict = {}

for i in text:
    if i in my_dict:
        print(f'{i}_{my_dict[i]}', end=' ')
    else:
        print(i, end=' ')
    my_dict[i] = my_dict.get(i, 0) +1

# dict.get(key[, value])
# Параметры get() в Python принимает максимум два параметра:
# key ‒ ключ для поиска в словаре;
# value (необязательно) ‒ значение, которое будет возвращено, если ключ не найден.
# Значение по умолчанию — Нет.
# Источник: https://pythonstart.ru/dictionary/get-python

strings = 'a a a b c a a d    c d d'.split()
dict_strings = {}.fromkeys(strings, 0)

for i in strings:
    print(f'{i}_{dict_strings[i]}' if dict_strings[i] else i, end=' ')
    # if dict_strings:
    #     print(f'{i}_{dict_strings[i]}', end=' ')
    # else:
    #     print(i, end=' ')
    dict_strings[i] += 1

# dictionary.fromkeys(sequence[, value])
# Параметры:
# fromkeys() в Python принимает два параметра:
# последовательность ‒ последовательность элементов, которая будет использоваться как ключи для нового словаря;
# value (необязательно) ‒ значение, которое устанавливается для каждого элемента словаря.
# Возвращаемое значение:
# Метод возвращает новый словарь с заданной последовательностью элементов в качестве ключей словаря. Если аргумент значения установлен, каждый элемент вновь созданного словаря устанавливается на предоставленное значение.
# Источник: https://pythonstart.ru/dictionary/fromkeys-python