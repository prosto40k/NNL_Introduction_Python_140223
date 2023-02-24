# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

counter=int(input())
numbers=[]
for i in range(counter):
    numbers.append(int(input()))

print(numbers)
num_values=len(set(numbers))
print(num_values)