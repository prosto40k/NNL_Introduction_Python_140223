# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8
n=int(input('Max: '))
numbers=0
k=0

for i in range(1000):
    numbers=2**k
    if  numbers>n:
        break
    k+=1
    print(numbers)
