# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение,
# пересечение и разность. Давайте разберем их.

colors = {'red', 'green', 'blue'}
print(f"{colors} \n{type(colors)}") # {'red', 'green', 'blue'}

colors.add('red')
print(f"---\n.add-добовляет(нельзя добавить то что уже есть)\n{colors} \n{type(colors)}") # {'red', 'green', 'blue'}

colors.add('gray')
print(f"---\n{colors} \n{type(colors)}") # {'red', 'green', 'blue'} # {'red', 'green', 'blue','gray'}

colors.remove('red')
print(f"---\n.remove-удалить значение\n{colors} \n{type(colors)}") # {'red', 'green', 'blue'} # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'

colors.discard('red') # ok
print(print(f"---\n.discard-проверяет есть ли это значение,а затем удаляет значение\n{colors} \n{type(colors)}"))
colors.clear()
print(print(f"---\n.clear-чистит \n{colors} \n{type(colors)}"))

q=set()#объявдение множества