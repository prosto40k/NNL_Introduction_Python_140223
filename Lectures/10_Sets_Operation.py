# Операции со множествами в Python:
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy() # .copy - копирование переменной c = {1, 2, 3, 5, 8}
u = a.union(b) #.union - объеденение(уникальных значений) u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) #.interseaction - пересечения элементов  i = {8, 2, 5}
dl = a.difference(b) # .difference - разность dl = {1, 3}
print(dl)
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}
q=frozenset(q)#.frozenset - замороженное множество
print(q)

