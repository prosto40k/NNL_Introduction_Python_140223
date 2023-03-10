# # #First answer
from random import randint
#
# list_nums = [randint(1, 21) for _ in range(int(input()))]#range - размер списка;randint - диапозон цифор
# #_ - безымянная переменная
# print(list_nums)
# num = int(input())
# right_num = list_nums[0]
#
# for i in list_nums:
#     if abs(num - i) < abs(num - right_num):
#         right_num = i
#
# print(right_num)

##Second answer

n = int(input())
list_nums = [randint(1, 50) for _ in range(n)]

print(list_nums)

b = int(input())
m = min(list_nums, key=lambda x: abs(x - b))

print(m)