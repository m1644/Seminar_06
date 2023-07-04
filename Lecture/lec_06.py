from mathematics import _basic_mat
from mathematics._advanced_mat import div, exp


# ------------------------
x = _basic_mat.mul  # Плохой пример! (Передача имени в другую переменную)
y = _basic_mat._START_MULT  # Плохой пример! (Обращение к защищённой или приватной переменной)
z = _basic_mat.sub(73, 42)

print(x(2, 3))
print(y)
print(z)
print('------------------------')


# ------------------------
print(f'{div(4, 2) = }')
print(f'{exp(4, 2) = }')
