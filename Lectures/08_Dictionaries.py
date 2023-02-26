# d={}
# print(f'{d}:\n{type(d)}')
#
# d=dict()
# print(f'---\n{d}:\n{type(d)}')
#
# d['q']='qwerty'
# print(f'---\n{d}:\n{type(d)}')
#
# d['w']='werty'
# print(f'---\n{d}:\n{type(d)}')
#
# print(f'---\n{d["w"]}:\n{type(d)}')

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # del удаление элемента
print("---")
for item in dictionary:
    print('{}: {}:'.format(item,dictionary[item]))

print("---")
for (i,j) in dictionary.items():
    print(i,j)

print(dictionary.items())