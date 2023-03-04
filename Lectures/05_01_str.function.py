#Python Console -> dir(str) все функции(методы)
#.split
print('1 2                 3'.split())#split - преобразует строку в список,убирает пробелы
print('1,2,3,,,,,,,,,,,,,,,,'.split(','))
#.join
print('\n'.join(['something', 'and what']))#' ' - чем объеденять
#.title - каждое новое слово с большой буквы
print('сЕрГеЙ сЕрГеЙ'.title())
#.capitalize - как предложение первое слово с большой буквы
print('сЕрГеЙ сЕрГеЙ'.capitalize())
#.count - сколько элементов
print('qwertyuiopq'.count('p'))
#.replace
print('qwertyuiopq'.replace('qw', '').count('q'))#пока это строка к ней можно ладьше применять функции строк
#.index - индекс элемента
print('asfsdfok'.index('sd', 3))
#.find - индекс элемента после запятой с какого индекса ищем
print('asfsdfok'.find('sd',4))
#.strip - убирает указанные символы
print(',//1!sdjgfjksdjklfsd    '.strip(',/1! '))
#.isdigit - это число?(bool)
print('-35646456'.replace('-', '').isdigit())
#.isalpha - это буквы
print('sdfgdfg'.isalpha())