# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# 1, 2, 3, 4, 5, 6, 7,  8,  9, 10, 11
i=0
j=1
fibo=int(input('Ввод: '))
count=2

while fibo>=j:
    if fibo==j:
        print(count)
        break
    i,j= j, i + j #Левая принимающая, правая отдающая(Способ картеж)
    count += 1
else:
    print(-1)


