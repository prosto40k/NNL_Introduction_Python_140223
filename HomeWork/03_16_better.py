# #First answer
# list_nums = [int(input('Элементы списка: ')) for _ in range(int(input('Размер списка: ')))]
# print(list_nums.count(int(input('Ищем: '))))
##Second answer
from random import choices

num = int(input('Размер списка: '))

list_nums = choices(range(num), k=num)# формирование списка чесел;range - диапазон чисел;k - размер списка
print(list_nums)

result = list_nums.count(int(input('Ищем: ')))
print(result)