# Пользователь вводит число, необходимо найти минимальный делитель данного числа

n = int(input())
flag = True
i = 2
while flag:#цикл будет выполнятся пока flagг=true
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False#вместо break(break-плохой тон(в ООП не исп-ся))
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1