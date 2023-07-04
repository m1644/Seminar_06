import random as rnd


# ------------------------
print(f'{rnd.random() = }')
rnd.seed()
state = rnd.getstate()
print(f'{state = }')
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
rnd.setstate(state)
