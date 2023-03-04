# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

list_1 = [1, 4, 2, 2, 5]
x = int(input('Ищем:'))
result = 0
box2el = 0
for i in range(len(list_1)):
    result = x-list_1[i]
    # print(result)
    if result == 0:
        box2el = i
        break
    elif result > 0:
        box2el = i

print(list_1)
if result == 0:
    print(f"Прямое попадание:\n{box2el+1}:{list_1[box2el]}")
else:
    print(f"Ближайшее:\n{box2el+1}:{list_1[box2el]}")

