text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # len(str) - ее длина
print('ещё' in text) # True
print(text.lower()) # .lower()-все в мальнекое
print(text.upper()) # .upper -все в большое
print(text.replace('ещё','ЕЩЁ больше')) # .replace('поменять это','на это')

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[len(text)-1]) # к
print(text[-1]) # последняя буква
print(text[:]) # Вывод всех символов
print(text[:2]) # от[0:2]
