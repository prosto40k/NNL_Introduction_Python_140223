# Задача 1: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a=int(input('Введите трехзначное число: '))
# b=a%10
# print(b)
# b=(a//10)%10
# print(b)
# b=(a//100)%10
# print(b)
box4number=int(0)
box4sum=int(0)
while a>0: ## while a:
    box4number=a%10
    box4sum+=box4number
    a=a//10
print(box4sum)