# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

n=int(input())
i=2
result=int(1)
if n==0:
    print(1)
else:
    while i!=n+1:
        result=i*result
        i+=1
    print(result)