#tuple-не поддерживает преобразование элементов после ввода
t=()
print(f'{t}:\n{type(t)}')

t=(1, 5, 3)
print(f'---\n{t}:\n{type(t)}')

v=[1,8,7]
print(f'---\n{v}:\n{type(v)}')

v=tuple(v)
print(f'---\n{v}:\n{type(v)}')

a,b=1,2
print(f'---\n{a},{b}\n{type(b)}')

a,b,c=v

print(f'---\n{a},{b},{c}\n{type(a)}')

print(f"{v[1]}\n")

for i in v:
    print(i)
print()
for i in range(len(v)):
    print(v[i])



