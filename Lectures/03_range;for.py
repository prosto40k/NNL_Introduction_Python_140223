a=range(5)
print(f'Переиенная:{a} \nТип данных:{type(a)}')

r = range(5) # 0 1 2 3 4
print(f'---------\nПереиенная:{r} \nТип данных:{type(r)}')
r = range(2, 5) # 2 3 4
print(f'---------\nПереиенная:{r} \nТип данных:{type(r)}')
r = range(-5, 0) # ----
print(f'---------\nПереиенная:{r} \nТип данных:{type(r)}')
r = range(1, 10, 2) # 1 3 5 7(1 откуда начинаем,10-где заканчиваем не включая число,2-шаг)
print(f'---------\nПереиенная:{r} \nТип данных:{type(r)}')
r = range(100, 0, -20) # 100 80 60 40 20(100 откуда начинаем,0-где заканчиваем не включая число,-20-шаг)
print(f'---------\nПереиенная:{r} \nТип данных:{type(r)}')

for i in r:
    print(i)
print(f'\n')
for i in 'qwerty':
    print(i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
