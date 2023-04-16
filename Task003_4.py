# Способ 1

import random

N = int(input("Введите натуральное число N: "))
A = [0] * N
for i in range(N):
    A[i] = random.randint(1, N + 1)
X = int(input("Введите число X: "))
count_X = 0
for i in A:
    if X == i:
        count_X += 1
print(f'Число {X} в массиве {A} встречается {count_X} раз.')

# Способ 2

N = int(input('Введите натуральное число N: '))
A = list(range(1, N + 1))
X = int(input('Введите число X: '))
print(f'Число {X} в массиве {A} встречается {A.count(X)} раз.')
