from lec_04 import *


# ------------------------
SIZE = 44

print(f'{SIZE = }')
# print(f'{result = }')
# print(f'{z = }')  # NameError: name 'z' is not defined
print(f'{_secret = }')  # NameError: name '_secret' is not defined
print(f'{func(100, 200) = }')
# print(f'{randint(10, 20) = }')
print('------------------------')


# ------------------------
def func(a: int, b: int) -> int:
    return a + b

print(f'{func(100, 200) = }')
