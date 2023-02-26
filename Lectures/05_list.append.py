list_1=[] #Пустой список
print(f'{list_1} - Тип данных: {type(list_1)}')
list_1=list() #Пустой список
print(f'{list_1} - Тип данных: {type(list_1)}')
list_1=[9,2,3,8]
print(*list_1,f' - Тип данных: {type(list_1)}')

for i in list_1:
    print(i)
print(f'\nДлина списка:\n{len(list_1)}')
print(f'Первый элемент списка:\n{list_1[0]}')

list_1.append(8)
print(f'.append - добавить в конец:\n{list_1}')

for i in range(5):
    list_1.append(i)
    print(f'.append - добавить в конец {i} через for:\n{list_1}')