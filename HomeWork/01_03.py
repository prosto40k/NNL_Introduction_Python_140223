# Задача 3: Вы пользуетесь общественным транспортом?
# Вероятно,вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

ticket_n=int(385916)
first_half=int(ticket_n/1000)
print(f'Цифры первой половины билета: {first_half}')
second_half=ticket_n%1000
print(f'Цифры второй половины билета: {second_half}')

box4number=int(0)
box4sum1=int(0)
box4sum2=int(0)

while first_half>0:
    box4number=first_half%10
    box4sum1+=box4number
    first_half=first_half//10
print(f'Сумма цифр первой половины билета: {box4sum1}')

while second_half>0:
    box4number=second_half%10
    box4sum2+=box4number
    second_half=second_half//10
print(f'Сумма цифр второй половины билета: {box4sum2}')

if box4sum1!=box4sum2:
    print('No')
else:
    print('Yes')