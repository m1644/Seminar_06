import sys
import random
import _random


# ------------------------
print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')
print('------------------------')


# ------------------------
print(_random.randint(1, 6))
print(random.randint(1, 6))
print('------------------------')
