import random as rnd


# ------------------------
START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 44, 88]

print(f'{rnd.randint(START, STOP) = }')
print(f'{rnd.uniform(START, STOP) = }')
print(f'{rnd.choice(data) = }')
print(f'{rnd.randrange(START, STOP, STEP) = }')
print('------------------------')


# ------------------------
print(f'{data = }')
rnd.shuffle(data)
print(f'{data = }')

print(f'{rnd.sample(data, 4) = }')
print(f'{rnd.sample(data, 4, counts=[1, 1, 1, 1, 1, 100]) = }')
