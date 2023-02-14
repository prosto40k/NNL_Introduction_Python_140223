# 5.С клавиатуры вводятся три числа. Найти максимальное из трех чисел
a=int(input('Введите a число: '))
b=int(input('Введите b число: '))
c=int(input('Введите c число: '))

max=a

if max>b:
    max=a
if b>max:
    max=b
if c>max:
    max=c
print(max)