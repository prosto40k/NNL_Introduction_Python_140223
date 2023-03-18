# Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”

# Ваня:
# flag = True
# max_number = 0
# while flag:
#     n = int(input())
#     if max_number < n:
#         max_number = n
#     if n == 0:
#         flag = False
# print(max_number)

# Петя
n = int(input())
max_number = -1
while n != 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)
