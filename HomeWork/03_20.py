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

list_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'D', 'G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']

word = str(input('Enter words on english language: '))
word = word.upper()
score = 0
for i in range(len(word)):
    # print(i)
    if word[i] == list_1[0] or word[i] == list_1[1] or word[i] == list_1[2] or word[i] == list_1[3] or word[i] == list_1[4] or word[i] == list_1[5] or word[i] == list_1[6] or word[i] == list_1[7] or word[i] == list_1[8] or word[i] == list_1[9]:
        score += 1
        print(f"1 очко:{word[i]}")
    elif word[i] == list_1[10] or word[i] == list_1[11]:
        score += 2
        print(f"2 очко:{word[i]}")
    elif word[i] == list_1[12] or word[i] == list_1[13] or word[i] == list_1[14] or word[i] == list_1[15]:
        score += 3
        print(f"3 очко:{word[i]}")
    elif word[i] == list_1[16] or word[i] == list_1[17] or word[i] == list_1[18] or word[i] == list_1[19] or word[i] == list_1[20]:
        score += 4
        print(f"4 очко:{word[i]}")
    elif word[i] == list_1[21]:
        score += 5
        print(f"5 очко:{word[i]}")
    elif word[i] == list_1[22] or word[i] == list_1[23]:
        score += 8
        print(f"8 очко:{word[i]}")
    elif word[i] == list_1[24] or word[i] == list_1[25]:
        score += 10
        print(f"10 очко:{word[i]}")

print(score)










