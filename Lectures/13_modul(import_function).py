import def_12#Импорт с вызовом 1
print(def_12.max1(5,9))

from def_12 import max1 #Импорт с вызовом 2
print(max1(10,9))

from def_12 import * #Импорт с вызовом 3,все функции
print(max1(10,9))

import def_12 as d1#Импорт с вызовом 4,rename
print(d1.sum_int(1,2,3,4,5))

