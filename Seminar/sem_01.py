

''' Задание_1
Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. 
(3-7 строк импорта).
'''

with open('Seminar\my_modules\my_module.py', 'w') as file:
    file.write('from sys import argv as ar\n')
    file.write('from random import randint as rnd\n')
    file.write('from datetime import datetime as dt\n')

print("Файл 'my_module.py' успешно создан.")
