# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

# list_1=['A','E','I','O','U','L','N','S','T','R','D','G','B','C','M','P','F','H','V','W','Y','K','J','X','Q','Z']
dictionary = {}
dictionary = {1: 'A''E''I''O''U''L''N''S''T''R', 2: 'D''G', 3: 'B' 'C' 'M' 'P',4:'F' 'H' 'V' 'W' 'Y', 5: 'K',
8:'J' 'X', 10:'Q' 'Z'}

word=str(input('Input word'))
score=0
item=0

for i in word:

    if word[i] == dictionary[i]:
        score += 1
        print(score)










# word=str(input('Input word'))
# word=str(input())
# word=word.upper()
# score=0
# box41score=0
# box42score=0
# box43score=0
# box44score=0
# box45score=0
# box48score=0
# box410score=0
#

# list_1=['A','E','I','O','U','L','N','S','T','R']
# if list_1[0]==word:
#     score+=1
# print(score)


# for i in range(len(word)):
#     # print(i)
#     if list_1[0]==word[i]:
#         score+=1
#         print(f"1 очко:{list_1[i]}")
#     elif list_1[9:10]==word[i]:
#         score += 2
#         print(f"2 очко:{list_1[i]}")
#     # elif 11<=i<=15:
#     #     print(f"3 очко:{list_1[i]}")
#     # elif 15 <= i <= 20:
#     #     print(f"4 очко:{list_1[i]}")
#     # elif 20 <= i <= 21:
#     #     print(f"5 очко:{list_1[i]}")
#     # elif 21 <= i <= 23:
#     #     print(f"8 очко:{list_1[i]}")
#     # elif 23 <= i <= 25:
#     #     print(f"10 очко:{list_1[i]}")
#
# print(score)
# print(word[i])
# print(list_1[i])
# print(word)









